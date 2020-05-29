from bitmart.api_spot import APISpot

if __name__ == '__main__':
    api_key = "80618e45710812162b04892c7ee5ead4a3cc3e56"
    secret_key = "6c6c98544461bbe71db2bca4c6d7fd0021e0ba9efc215f9c6ad41852df9d9df9"
    memo = "test001"

    spotAPI = APISpot(api_key, secret_key, memo)

    symbol = 'BTC_USDT'

    # Test GET https://api-cloud.bitmart.com/spot/v1/currencies
    print(spotAPI.get_currencies())

    # # Test GET https://api-cloud.bitmart.com/spot/v1/symbols
    # print(spotAPI.get_symbols())

    # Test GET https://api-cloud.bitmart.com/spot/v1/symbols/details
    # print(spotAPI.get_symbol_detail())

    # Test GET https://api-cloud.bitmart.com/spot/v1/ticker
    # print(spotAPI.get_ticker())
    # print(spotAPI.get_symbol_ticker(symbol))

    # Test GET https://api-cloud.bitmart.com/spot/v1/steps
    # print(spotAPI.get_steps())

    # Test GET https://api-cloud.bitmart.com/spot/v1/symbols/kline
    # print(spotAPI.get_symbol_book(symbol, 1525760116000, 1525769116000, 1440))

    # GET https://api-cloud.bitmart.com/spot/v1/symbols/book
    # print(spotAPI.get_symbol_book(symbol, None))

    # GET https://api-cloud.bitmart.com/spot/v1/symbols/trades
    # print(spotAPI.get_symbol_trades(symbol))

    # Test GET https://api-cloud.bitmart.com/spot/v1/wallet
    # print(spotAPI.get_wallet())

    # Test POST https://api-cloud.bitmart.com/spot/v1/submit_order

    # print(spotAPI.post_submit_limit_buy_order(symbol, size=0.01, price=8800))
    # print(spotAPI.post_submit_limit_sell_order(symbol, size=0.01, price=8800))

    # print(spotAPI.post_submit_market_buy_order(symbol, notional=1))
    # print(spotAPI.post_submit_market_sell_order(symbol, size=10))

    # Test POST https://api-cloud.bitmart.com/spot/v1/cancel_order
    # print(spotAPI.post_cancel_order(symbol, 2147484355))

    # Test GET https://api-cloud.bitmart.com/spot/v1/order_detail
    # print(spotAPI.get_user_order_detail(symbol, 2147484353))

    # Test GET https://api-cloud.bitmart.com/spot/v1/orders
    # print(spotAPI.get_user_orders(symbol, offset=1, limit=10, status="2"))

    # Test GET https://api-cloud.bitmart.com/spot/v1/trades
    # print(spotAPI.get_user_order_trades(symbol, 2147484351))
    # print(spotAPI.get_user_trades(symbol, offset=1, limit=10))
