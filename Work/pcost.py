# pcost.py
#
# Exercise 1.27
import csv

def portfolio_cost(filepath):
    f = open(filepath, "rt")
    rows = csv.reader(f)
    header = next(rows)
    total = 0.0
    for rowno, row in enumerate(rows): 
        record = dict(zip(header, row))
        try:
            nshares = int(record["shares"])
            price = float(record["price"])
            total += nshares * price
        except ValueError:
            print(f"Row {rowno}: Bad row: {row}")

    f.close()
    print(f"Total cost {round(total, 2)}")

