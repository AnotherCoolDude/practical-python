# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    '''Computes the total cost (shares * price) of a portfolio file'''
    portfolio = []

    with open(filename, "rt") as file:
        rows = csv.reader(file)
        header = next(rows)
        for row in rows:
            portfolio.append({header[0]: row[0], header[1]: int(row[1]), header[2]: float(row[2])})
    
    return portfolio


def read_prices(filename):
    f = open(filename, "r")
    rows = csv.reader(f)
    stocks = {}
    for row in rows:
        if not row:
            continue
        stocks[row[0]] = float(row[1])
    
    f.close()
    return stocks

def calculate_stocks(portfolio, prices):
    portfolio = read_portfolio(portfolio)
    prices = read_prices(prices)
    total = 0.0
    for stock in portfolio:
        current_price = stock["price"] - prices[stock["name"]]
        total += current_price * stock["shares"]
    return total
