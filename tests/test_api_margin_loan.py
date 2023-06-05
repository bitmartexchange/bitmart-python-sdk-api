from bitmart.api_margin_loan import APIMarginLoan
from tests import data as data

# margin loan api
marginLoanAPI = APIMarginLoan(data.api_key, data.secret_key, data.memo, data.url, timeout=data.timeout)


def test_margin_borrow_isolated():
    """Test POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/borrow"""
    assert marginLoanAPI.margin_borrow_isolated(symbol='BTC_USDT', currency='BTC', amount='1')[0][
               'code'] == 1000


def test_margin_repay_isolated():
    """Test POST https://api-cloud.bitmart.com/spot/v1/margin/isolated/repay"""
    assert marginLoanAPI.margin_repay_isolated(symbol='BTC_USDT', currency='BTC', amount='1')[0][
               'code'] == 1000


def test_get_borrow_record_isolated():
    """Test GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/borrow_record"""
    assert marginLoanAPI.borrow_record_isolated(symbol='BTC_USDT')[0]['code'] == 1000
    assert marginLoanAPI.borrow_record_isolated(symbol='BTC_USDT', borrow_id='ES16612345642160qnqR1ce')[0][
               'code'] == 1000
    assert marginLoanAPI.borrow_record_isolated(
        symbol='BTC_USDT', start_time=1664607368000, end_time=1665989933000)[0]['code'] == 1000


def test_get_repayment_record_isolated():
    """Test GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/repay_record"""
    assert marginLoanAPI.repayment_record_isolated(symbol='BTC_USDT')[0]['code'] == 1000
    assert marginLoanAPI.repayment_record_isolated(
        symbol='BTC_USDT', repay_id='be7e0117-5bc9-8475-8e27-567cfa567af7')[0]['code'] == 1000
    assert marginLoanAPI.repayment_record_isolated(
        symbol='BTC_USDT', start_time=1664607368000, end_time=1665989933000)[0]['code'] == 1000


def test_get_trading_pair_borrowing_rate_and_amount_by_symbol():
    """Test GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/pairs"""
    assert marginLoanAPI.trading_pair_borrowing_rate_and_amount(symbol='BTC_USDT')[0]['code'] == 1000


def test_get_trading_pair_borrowing_rate_and_amount():
    """Test GET https://api-cloud.bitmart.com/spot/v1/margin/isolated/pairs"""
    assert marginLoanAPI.trading_pair_borrowing_rate_and_amount()[0]['code'] == 1000
