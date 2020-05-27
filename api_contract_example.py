from bitmart.api_contract import APIContract

if __name__ == '__main__':
    api_key = "80618e45710812162b04892c7ee5ead4a3cc3e56"
    secret_key = "6c6c98544461bbe71db2bca4c6d7fd0021e0ba9efc215f9c6ad41852df9d9df9"
    memo = "test001"

    # contract api
    contractAPI = APIContract(api_key, secret_key, memo)

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/contracts
    print(contractAPI.get_contracts())

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/pnls
    print(contractAPI.get_pnls(contractId=1))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/indexes
    print(contractAPI.get_indexes())

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/tickers
    print(contractAPI.get_tickers(contractId=1))
    print(contractAPI.get_tickers(None))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/quote
    print(contractAPI.get_quote(contractId=1, startTime=1584343602, endTime=1585343602, unit=5, resolution='M'))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/indexquote
    print(contractAPI.get_index_quote(indexId=1, startTime=1584343602, endTime=1585343602, unit=1, resolution='H'))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/trades
    print(contractAPI.get_trades(contractId=1))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/depth
    print(contractAPI.get_depth(contractId=1, count=None))
    print(contractAPI.get_depth(contractId=1, count=10))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/fundingrate
    print(contractAPI.get_funding_rate(contractId=2))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userOrders
    print(contractAPI.get_user_orders(contractId=1, status=0, offset=None, size=None))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userOrderInfo
    print(contractAPI.get_user_order_info(contractId=1, orderId=3816371425))

    # Test POST https://api-cloud.bitmart.com/contract/v1/ifcontract/submitOrder
    # print(contractAPI.post_submit_order(contractId=1, category=1, openType=1, way=1, leverage=50, customId=10, price=8885, vol=10))

    # Test POST https://api-cloud.bitmart.com/contract/v1/ifcontract/batchOrders,
    contractId = 1
    category = 1
    way = 1
    openType = 1
    leverage = 10
    customId = 100
    price = 9000
    vol = 1
    orders = [{
        'contract_id': contractId,
        'category': category,
        'way': way,
        'open_type': openType,
        'leverage': leverage,
        'custom_id': customId,
        'price': price,
        'vol': vol
    }, {
        'contract_id': contractId,
        'category': category,
        'way': way,
        'open_type': openType,
        'leverage': leverage,
        'custom_id': customId,
        'price': price,
        'vol': vol
    }]
    # print(contractAPI.post_submit_batch_order(orders))

    # Test POST https://api-cloud.bitmart.com/contract/v1/ifcontract/cancelOrders
    cancel_orders = [
        {
            "contract_id": 1,
            "orders": [
                3816433968,
                3816433969
            ]
        }
    ]
    # print(contractAPI.post_cancel_order(contractId, cancel_orders))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userTrades
    print(contractAPI.get_user_trades(contractId, None, None))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/orderTrades
    print(contractAPI.get_order_trades(contractId, 3816433969))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/accounts
    print(contractAPI.get_accounts(coinCode='USDT'))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userPositions
    print(contractAPI.get_user_positions(contractId))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/userLiqRecords
    print(contractAPI.get_user_liq_records(contractId, 3816433968))

    # Test GET https://api-cloud.bitmart.com/contract/v1/ifcontract/positionFee
    print(contractAPI.get_position_fee(contractId, 2802613453))

    # Test POST https://api-cloud.bitmart.com/contract/v1/ifcontract/marginOper
    # print(contractAPI.post_margin_oper(contractId, 2802613453, 100, 1))