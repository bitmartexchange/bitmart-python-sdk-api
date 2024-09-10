Changelog
=========================



### v2.0.0 Release
#### New Features
- New
  - `/spot/v4/batch_orders`
  - `/spot/v4/cancel_orders`
  - `/spot/v4/cancel_all`
  - `/contract/private/position-risk`
  - `/contract/private/current-plan-order`
- Updated 
  - `/account/v1/withdraw/apply`
  - `/account/v2/deposit-withdraw/history`
  - `/contract/private/position`
  - `/contract/private/trades`
  - `/contract/private/submit-order`
- Removed
  - `/spot/v2/ticker`
  - `/spot/v1/ticker_detail`
  - `/spot/v1/steps`
  - `/spot/v1/symbols/kline`
  - `/spot/v1/symbols/book`
  - `/spot/v1/symbols/trades`
  - `/spot/v2/batch_orders`
  - `/spot/v1/cancel_orders`
#### Improvements
- Support Custom Logger Integration
- Support Custom request headers
- Dependency upgrade, websockets used are replaced with websocket-client 
- Remove the asynchronous call mechanism and support customers’ more convenient custom asynchronous subscriptions.
- Log upgrade, replace print with logging
- Add examples directory
- Constants Renamed
  - WS_URL renamed to SPOT_PUBLIC_WS_URL
  - WS_URL_USER renamed to SPOT_PRIVATE_WS_URL
  - CONTRACT_WS_URL renamed to FUTURES_PUBLIC_WS_URL
  - CONTRACT_WS_URL_USER renamed to FUTURES_PRIVATE_WS_URL
#### Bug Fixes

---

### v1.0.0 Release
#### New Features
##### 2023-09-11
- New endpoints for API Spot Market
  - <code>/spot/quotation/v3/tickers</code> Get Ticker of All Pairs (V3)
    <code>/spot/quotation/v3/ticker</code> Get Ticker of a Trading Pair(V3)
    <code>/spot/quotation/v3/lite-klines</code> Get Latest K-Line (V3)
    <code>/spot/quotation/v3/klines</code> Get History K-Line (V3)
    <code>/spot/quotation/v3/books</code> Get Depth(V3)
    <code>/spot/quotation/v3/trades</code> Get Recent Trades(V3)
- New endpoints for API Futures Trading
    - <code>/contract/private/get-open-orders</code>Get All Open Orders (KEYED)
    - <code>/contract/private/submit-leverage</code>Submit Leverage (SIGNED)

##### 2023-05-29
- New endpoints for API Futures Trading
    - <code>/account/v1/transfer-contract</code>Transfer between spot account and contract account
    - <code>/account/v1/transfer-contract-list</code>Query futures account transfer records
- New endpoints for Spot / Margin trading
    - <code>/spot/v4/query/order</code>Query order by id (v4)
    - <code>/spot/v4/query/client-order</code>Query order by client order id (v4)
    - <code>/spot/v4/query/open-orders</code>Current open orders (v4)
    - <code>/spot/v4/query/history-orders</code>Account orders (v4)
    - <code>/spot/v4/query/trades Account</code>trade list (v4)
    - <code>/spot/v4/query/order-trades</code>Order trade list(v4)

##### 2022-11-03
- New endpoints for API Broker
  - <code>/spot/v1/broker/rebate</code>Applicable to query API Broker's rebate records
- Update endpoints for Spot / Margin trading
  - <code>/spot/v3/orders</code> <code>/spot/v2/trades</code>add start_time and end_time field for flexible querying
  - add new order status 11 = Partially filled and canceled


##### 2022-10-28
- contract websocket public channel address<code>wss://openapi-ws.bitmart.com/api?protocol=1.1</code>
- contract websocket private channel address<code>wss://openapi-ws.bitmart.com/user?protocol=1.1</code>


##### 2022-10-20
- Upgrade endpoints for Spot
  - <code>/spot/v1/ticker</code> has been upgraded to <code>/spot/v2/ticker</code> and <code>/spot/v1/ticker_detail</code>
  - <code>/spot/v1/submit_order</code> has been upgraded to <code>/spot/v2/submit_order</code>
  - <code>/spot/v1/batch_orders</code> has been upgraded to <code>/spot/v2/batch_orders</code>
  - <code>/spot/v2/cancel_order</code> has been upgraded to <code>/spot/v3/cancel_order</code>
  - <code>/spot/v1/order_detail</code> has been upgraded to <code>/spot/v2/order_detail</code>
  - <code>/spot/v2/orders</code> has been upgraded to <code>/spot/v3/orders</code>
  - <code>/spot/v1/trades</code> has been upgraded to <code>/spot/v2/trades</code>
- New endpoints for Spot & Margin
  - <code>/spot/v1/margin/isolated/account</code>Applicable for isolated margin account inquiries
  - <code>/spot/v1/margin/isolated/transfer</code>For fund transfers between a margin account and spot account
  - <code>/spot/v1/user_fee</code>For querying the base rate of the current user
  - <code>/spot/v1/trade_fee</code>For the actual fee rate of the trading pairs
  - <code>/spot/v1/margin/submit_order</code>Applicable for margin order placement
  - <code>/spot/v1/margin/isolated/borrow</code>Applicable to isolated margin account borrowing operations
  - <code>/spot/v1/margin/isolated/repay</code>Applicable to isolated margin account repayment operations
  - <code>/spot/v1/margin/isolated/borrow_record</code>Applicable to the inquiry of borrowing records of an isolated margin account
  - <code>/spot/v1/margin/isolated/repay_record</code>Applicable to the inquiry of repayment records of isolated margin account
  - <code>/spot/v1/margin/isolated/pairs</code>Applicable for checking the borrowing rate and borrowing amount of trading pairs


##### 2022-10-18
- New endpoints for Contract Market
  - <code>/contract/public/details</code>Get contract details
  - <code>/contract/public/depth</code>Get contract depth
  - <code>/contract/public/open-interest</code>Get contract open interest
  - <code>/contract/public/funding-rate</code>Get contract funding rate
  - <code>/contract/public/kline</code>Get contract kline
- New endpoints for Contract Account
  - <code>/contract/private/assets-detail</code>Get contract user assets detail
- New endpoints for Contract Trade
  - <code>/contract/private/order</code>Get contract order detail
  - <code>/contract/private/order-history</code>Get contract order history
  - <code>/contract/private/position</code>Get contract position
  - <code>/contract/private/trades</code>Get contract trades
  - <code>/contract/private/submit_order</code>Post contract submit order
  - <code>/contract/private/cancel_order</code>Post contract cancel order
  - <code>/contract/private/cancel_orders</code>Post contract batch cancel orders

##### 2022-01-20
- Update endpoints for Spot
  - <code>/spot/v1/symbols/details</code>Add a new respond parameter trade_status, to show the trading status of a trading pair symbol.


##### 2022-01-18
- websocket public channel address<code>wss://ws-manager-compress.bitmart.com?protocol=1.1</code>will be taken down on 2022-02-28 UTC time,The new address is<code>wss://ws-manager-compress.bitmart.com/api?protocol=1.1</code>


##### 2021-11-24
- New endpoints for Spot
  - <code>/spot/v2/orders</code>Get User Order History V2
  - <code>/spot/v1/batch_orders</code>Batch Order
- Update endpoints for Spot
  - <code>/spot/v1/symbols/kline</code>Add new field 'quote_volume'
  - <code>/spot/v1/symbols/trades</code>Add optional parameter N to return the number of items, the default is up to 50 items
  - <code>/spot/v1/order_detail</code>Add new field 'unfilled_volume'
  - <code>/spot/v1/submit_order</code>The request parameter type added limit_maker and ioc order types
- New endpoints for Account
  - <code>/account/v2/deposit-withdraw/history</code>Get Deposit And Withdraw  History V2
- Update endpoints for Account
  - <code>/account/v1/wallet</code>Remove the account_type,Only respond to currency accounts; you can bring currency parameters (optional)

##### 2021-11-06
- Update endpoints for Spot WebSocket
  - Public-Depth Channel:
    - spot/depth20     20 Level Depth Channel
    - spot/depth50     50 Level Depth Channel
  - User-Trade Channel:
    - Eligible pushes add new orders successfully


##### 2021-01-19
- New endpoints for Spot WebSocket
  - Public - ticket channels
  - Public - K channel
  - Public - trading channels
  - Public - depth channels
  - Login
  - User - Trading Channel

##### 2020-09-21
- Interface Spot API `/spot/v1/symbols/book` add `size` parameter, which represents the number of depths

##### 2020-07-16 
- Interface Spot API `Cancel Order` update to v2 version that is `POST https://api-cloud.bitmart.com/spot/v2/cancel_order`
- UserAgent set "BitMart-Python-SDK/1.0.1


