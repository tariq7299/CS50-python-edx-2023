import sys
import csv

# Check the number of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Get the input and output file names from command-line arguments
inputfile = sys.argv[1]
outputfile = sys.argv[2]

new_students_data = []

try:

    with open(inputfile, "r") as infile:
        students = csv.DictReader(infile)
        for student in students:
            name = student["name"].split(",")
            last_name = name[0].strip()
            first_name = name[1].strip()
            house = student["house"]

            new_student_data = {
                "first": first_name,
                "last": last_name,
                "house": house
            }

            new_students_data.append(new_student_data)

    with open(outputfile, "w", newline="") as outfile:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(new_students_data)
        
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")
