import sys
import csv
from tabulate import tabulate

if len(sys.argv) != 2:
    sys.exit("Usage: python script.py filename")

filename = sys.argv[1]

if ".csv" not in filename:
    sys.exit("Not a CSV file")

try:
    with open(filename, 'r') as file:

        rows = list(csv.reader(file))
        print("list: ", rows)

        headers = rows[0]
        table = rows[1:]

        print(tabulate(table, headers, tablefmt="grid"))
except FileNotFoundError:
    sys.exit("File does not exist")
