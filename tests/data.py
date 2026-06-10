import os


def _load_env_file(path):
    """Parse a simple KEY=VALUE .env file into a dict (no external dependency)."""
    data = {}
    if os.path.isfile(path):
        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key, _, value = line.partition("=")
                data[key.strip()] = value.strip().strip('"').strip("'")
    return data


# project root = parent directory of tests/
_ENV_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".env")
_ENV = _load_env_file(_ENV_PATH)


def _get(name, default):
    """Priority: .env file > OS environment variable > default placeholder."""
    return _ENV.get(name) or os.environ.get(name) or default


api_key = _get("BITMART_API_KEY", "Your_API_KEY")
secret_key = _get("BITMART_SECRET_KEY", "Your_Secret_KEY")
memo = _get("BITMART_MEMO", "Your_Memo")
url = _get("BITMART_API_URL", "https://api-cloud.bitmart.com")

timeout = (2, 5)  # connection timeout, read timeout
