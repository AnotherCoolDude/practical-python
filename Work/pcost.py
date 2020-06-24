# pcost.py
#
# Exercise 1.27

f = open("Data/portfolio.csv", "rt")
next(f)
total = 0.0
for row in f: 
    data = row.split(",")
    total += int(data[1]) * float(data[2])

f.close()
print(f"Total cost {round(total, 2)}")

