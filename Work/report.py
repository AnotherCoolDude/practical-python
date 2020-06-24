# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    '''Computes the total cost (shares * price) of a portfolio file'''
    portfolio = []

    with open(filename, "rt") as file:
        rows = csv.reader(file)
        next(rows)
        for row in rows:
            portfolio.append((row[0], int(row[1]), float(row[2])))
    
    return portfolio



