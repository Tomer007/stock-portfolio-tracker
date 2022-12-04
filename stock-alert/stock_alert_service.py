from stock_alert_model import load_user_portfolio_from_csv
import yfinance as yf

import logging

logger = logging.getLogger('stock_alert')
logging.basicConfig(level=logging.INFO)


def get_market_stock_price(stocks):
    stocks_price_dic = {}
    # stocks_price_dic = {"JKS": 1, "NIO": 2, "SEDG": 3}
    for row in stocks:
        stock_info = yf.Ticker(row).info
        market_price = stock_info['regularMarketPrice']
        stocks_price_dic[row] = market_price
    print(f"stock Market price are: {stocks_price_dic}")
    return stocks_price_dic


def run_user_portfolio_analysis(name):
    print(f"run stock analysis for user {name} ")
    user_portfolio = load_user_portfolio_from_csv(name)
    request_stocks = extract_requested_stock_list(user_portfolio)
    market_stocks_price = get_market_stock_price(request_stocks)
    return portfolio_analysis(market_stocks_price, user_portfolio)


def extract_requested_stock_list(user_portfolio):
    request_stocks = []
    for sub_list in user_portfolio:
        request_stocks.append(sub_list['stock symbol'])
    print(f"requested stocks are: {request_stocks} ")
    return request_stocks


def portfolio_analysis(market_stocks_price, user_portfolio):
    print(market_stocks_price)
    print(user_portfolio)
    portfolio_analysis_result = []
    for row in user_portfolio:
        stock_symbol = row["stock symbol"]
        buy_price = row["buy price"]
        quantinity = row["quantinity"]
        market_price = market_stocks_price[stock_symbol]
        profit = (float(market_price) - float(buy_price)) * int(quantinity)
        stock_dic = {"stock symbol": stock_symbol, "buy price": buy_price, "quantinity": quantinity,
                     "PNL": round(profit, 2)}
        portfolio_analysis_result.append(stock_dic)
    print(f"portfolio analysis result {portfolio_analysis_result}")
    return portfolio_analysis_result


class ServiceStockAlert:
    pass
