# CLAUDE.md

This file guides Claude Code when working in this repository.

## Project overview

`bitmart-python-sdk-api` is BitMart Exchange's official Python client for the **BitMart Cloud API**. It is a thin, hand-written wrapper over BitMart's REST endpoints and WebSocket streams. Every public method maps 1:1 to an endpoint documented at the official API docs — keep them in sync.

- Online API docs: https://developer.bitmart.com/spot (and https://developer-pro.bitmart.com/en/spot/#change-log)
- PyPI package: `bitmart-python-sdk-api`
- Version source of truth: `bitmart/__version__.py` (currently `2.5.0`)
- Python support: 3.7+ (classifiers list 3.7–3.10)
- License: MIT

## Layout

```
bitmart/
  __version__.py            # __version__ string (single source of version truth)
  api_spot.py               # APISpot      — /spot/* REST (24 methods)
  api_contract.py           # APIContract  — /contract/* futures REST (39 methods)
  api_account.py            # APIAccount   — /account/* REST (13 methods)
  api_spot_sub_account.py   # APISpotSubAccount     — /account/sub-account/* spot (8 methods, api-cloud domain)
  api_contract_sub_account.py # APIContractSubAccount — /account/contract/sub-account/* futures (6 methods, api-cloud-v2 domain)
  api_margin_loan.py        # APIMarginLoan — /spot/v1/margin/isolated/* (6 methods)
  api_broker.py             # APIBroker    — /spot/v1/broker/* (3 methods)
  api_system.py             # APISystem    — /system/* (3 methods)
  lib/
    cloud_client.py         # CloudClient base — HTTP request/sign/response handling
    cloud_consts.py         # ALL endpoint paths, WS URLs, channel names, Auth enum
    cloud_utils.py          # sign(), pre_substring(), headers, gzip inflate, config_logging
    cloud_exceptions.py     # APIException, RequestException, ParamsException
    cloud_log.py
  websocket/
    spot_socket_client.py   # SpotSocketClient   (op-based protocol)
    futures_socket_client.py# FuturesSocketClient (action-based protocol)
    socket_manager.py       # SocketManager — threaded ws-client, reconnect, ping
examples/                   # runnable examples mirroring the API surface
  config.py                 # API_KEY / SECRET_KEY / MEMO placeholders for examples
  spot/ futures/ websocket/
tests/                      # pytest tests, one file per API module
  data.py                   # test credentials + base url (gitignored secrets)
requirements/
  common.txt                # runtime deps: requests, websocket-client
  requirements-test.txt     # pytest
```

## Architecture

### REST clients
All REST API classes inherit from `CloudClient` (`bitmart/lib/cloud_client.py`). Construction is uniform:

```python
APISpot(api_key="", secret_key="", memo="", url=API_URL, timeout=TIMEOUT, headers=None, logger=None)
```

- `CloudClient._request()` builds the URL (GET/DELETE append query string; POST sends a JSON body), applies auth headers, sends via a shared `requests.Session`, and on non-200 raises `APIException`.
- **Every method returns a 2-tuple `(result, rate_limit)`** — `result` is the parsed JSON dict, `rate_limit` is a dict with `Remaining/Limit/Reset/Mode` from the `X-BM-RateLimit-*` response headers. Callers use `response[0]` for the body and `response[1]` for rate-limit metadata. Preserve this contract.
- A successful BitMart call has `result['code'] == 1000`.
- Helpers: `_request_without_params(method, path, auth)` and `_request_with_params(method, path, params, auth)`.

### Authentication (three levels — `Auth` enum in `cloud_consts.py`)
- `Auth.NONE` — public, no headers.
- `Auth.KEYED` — sends `X-BM-KEY` only.
- `Auth.SIGNED` — sends `X-BM-KEY`, `X-BM-SIGN`, `X-BM-TIMESTAMP`.

Signing (`cloud_utils.py`): `sign = HMAC_SHA256(secret_key, "{timestamp}#{memo}#{body}")` hex digest, where for POST the body is the JSON string and for GET/DELETE it is the empty string. The signing string is built by `pre_substring(timestamp, memo, body)`.

### WebSocket clients
Two clients backed by a shared threaded `SocketManager` (auto-reconnect, periodic ping, resubscribe on reconnect). **The two protocols differ — do not mix them up:**

| | Spot (`SpotSocketClient`) | Futures (`FuturesSocketClient`) |
|---|---|---|
| Subscribe key | `{"op": "subscribe", ...}` | `{"action": "subscribe", ...}` |
| Login key | `{"op": "login", "args": [key, ts, sign]}` | `{"action": "access", "args": [key, ts, sign, "web"]}` |
| Ping frame | `"ping"` | `{"action":"ping"}` |
| Public URL | `SPOT_PUBLIC_WS_URL` | `FUTURES_PUBLIC_WS_URL` |
| Private URL | `SPOT_PRIVATE_WS_URL` | `FUTURES_PRIVATE_WS_URL` |

WS login signs the fixed string `"bitmart.WebSocket"`: `sign = HMAC_SHA256(secret, "{ts}#{memo}#bitmart.WebSocket")`. Channel names (e.g. `spot/ticker`, `futures/klineBin1m`) are constants in `cloud_consts.py`. Incoming binary frames may be gzip-deflated — `cloud_utils.inflate()` handles decompression.

### Constants
**All endpoint paths, WS URLs, and channel names live in `bitmart/lib/cloud_consts.py`.** Domains: spot REST `https://api-cloud.bitmart.com` (`API_URL`); futures REST often uses `https://api-cloud-v2.bitmart.com` (`API_V2_URL`). When adding an endpoint, add its path constant here first, then the method that references it.

## Conventions

- **One method per endpoint**, named `get_*` / `post_*` after the HTTP verb and resource. Each method's docstring states the HTTP method and full URL — keep this format.
- Endpoint paths are referenced via the `cloud_consts.py` constants (imported with `from bitmart.lib.cloud_consts import *`), never hard-coded inline.
- Pass the correct `Auth` level for each endpoint (public vs keyed vs signed).
- Mirror new endpoints in three places: the API module, an example under `examples/`, and a test under `tests/`.
- Keep parameter names aligned with the online API docs.

## Adding / updating an endpoint (typical workflow)

1. Confirm the spec against the online docs / changelog.
2. Add the path constant to `bitmart/lib/cloud_consts.py`.
3. Add the method to the matching `api_*.py` class, using the right `Auth` level and a `_request_*` helper. Include a docstring with `METHOD https://.../path`.
4. Add an example under the matching `examples/` subfolder.
5. Add a test in the matching `tests/test_api_*.py`.
6. Update `CHANGELOG.md` and bump `bitmart/__version__.py` when releasing.

## Development

```bash
# Install runtime + test deps
pip install -r requirements/requirements-test.txt

# Run the test suite (pytest)
pytest                      # all tests
pytest tests/test_api_spot.py

# Build/install locally
pip install -e .
```

Tests hit the **live BitMart API** and require real credentials. They read `url`, `api_key`, `secret_key`, `memo` from `tests/data.py` (keep secrets out of commits). Network is required; expect failures offline.

## Notes & gotchas

- Methods return `(body, rate_limit_dict)` tuples — indexing `[0]` for the body is intentional, not a bug.
- Spot uses `op`, Futures uses `action` for WebSocket control messages.
- Timestamps are epoch milliseconds as a string (`cloud_utils.get_timestamp()`).
- Custom request headers are allowed, but never override `X-BM-KEY`, `X-BM-SIGN`, or `X-BM-TIMESTAMP`.
- Enable request/response debug logging with `config_logging(logging, logging.DEBUG)` from `cloud_utils`.
