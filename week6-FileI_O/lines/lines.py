import sys

if len(sys.argv) != 2:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if ".py" not in filename:
    sys.exit("Not a Python file")

try:
    with open(filename, 'r') as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

counter = 0

for line in lines:
    stripped_line = line.strip()
    if stripped_line and not stripped_line.startswith("#"):
        counter += 1

print(counter)
