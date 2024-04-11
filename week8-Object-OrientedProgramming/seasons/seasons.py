from datetime import date
import operator
import inflect
import sys


def main():

    try:
        birthdate = input("Date of Birth: ")

        # Get the age and also get check whether birthdate is a valid or not
        difference = operator.sub(date.today(), date.fromisoformat(birthdate))
        # Print date in minutes
        print(convert(difference.days))
    except ValueError:
        sys.exit("Invalid date")

# Convert the date into minutes
def convert(time):
    p = inflect.engine()
    minutes = time * 24 * 60
    return f"{(p.number_to_words(minutes, andword='')).capitalize()} minutes"


if __name__ == "__main__":
    main()



## Another solution

# from datetime import date, datetime
# from num2words import num2words
# import re

# class Person:

#     def __init__(self, birthdate):
#         self.birthdate = birthdate

#     def __str__(self):
#         return f"Your birthdate is {self._birthdate}"

#     @property
#     def birthdate(self):
#         return self._birthdate

#     @birthdate.setter
#     def birthdate(self, birthdate):
#         try:
#             if not birthdate:
#                 raise ValueError("Please provide a birthdate")
#             birthdate = datetime.strptime(birthdate, "%Y-%m-%d")
#             self._birthdate = birthdate
#         except ValueError:
#             raise ValueError("Invalid format")

#     @classmethod
#     def get_birthdate(cls):
#         birthdate = input("Enter birthdate: ")
#         return cls(birthdate)

#     def convert(self):
#         now = date.today()
#         age = now - self.birthdate.date()  # Convert datetime to date
#         minutes = int(age.total_seconds() / 60)
#         print(minutes)
#         minutes_text = re.sub("\band\b", ", ", num2words(minutes))
#         return minutes_text

# def main():
#     birthdate = Person.get_birthdate()
#     birthdate_in_minutes = birthdate.convert()
#     print("birthdate in minutes: ", birthdate_in_minutes.capitalize())

# if __name__ == "__main__":
#     main()
