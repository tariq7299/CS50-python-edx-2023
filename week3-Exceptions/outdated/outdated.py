# I made the MONTHS list global, in order to to accessd any where, and also to make the code more readable
# MONTHS = [
#             "January",
#             "February",
#             "March",
#             "April",
#             "May",
#             "June",
#             "July",
#             "August",
#             "September",
#             "October",
#             "November",
#             "December"
#             ]

# def main():

#     while True:

#         # This is obvious from its name that it will propmt the user for an input and then returns three values
#         user_input = prompt_user_and_return_day_month_year()

#         # If the reurn value is an Exception object then that means that the user input is invalid, so "pass" and repropmt the user again
#         if isinstance(user_input, Exception):
#             pass

#         else:
#             date = user_input
#             month, day, year = date

#             # Keep in mind that we have two conditions here because the program accepts date input in two formates (month(int)/day(int)/year(int)) format OR (month(str) day(int), year(int))

#             # If all retuns values are True then print the date
#             if get_valid_month(month) and get_valid_day(day) and get_valid_year(year):

#                 # If the month is integer, so that means that the user input the date in (month/day/year) format
#                 if isinstance(month, int):
#                     # ":02d" will make the intger as two digit number for ex: 9 is 09
#                     print(f"{year}-{month:02d}-{day:02d}")


#                     # If month is not integer, so that means that the user input the date in (month(str) day, year)
#                 else:
#                     # MONTHS.index(month) + 1, this returns the number of the month as his order number in calender, as the months in MONTHS list is orderd corectly
#                     # So this will convert
#                     month_int = MONTHS.index(month) + 1
#                     print(f"{year}-{month_int:02d}-{day:02d}")

#                 break





# def prompt_user_and_return_day_month_year():
#     try:
#         date = input("Enter date :").strip()

#         # THis will return True or False, if True that will mean that the user input contains a '/', so then it will mean that is (maybe) the user enterd a date in (month(int)/day(int)/year(int)) format
#         if date.find('/') != -1:

#             # Extract month, day, year and then apply int() to each value
#             month, day, year = map(int, date.split("/"))
#             return month, day, year

#         #  THis will return True or False, if True that will mean that the user input contains a '/', so then it will mean that is (maybe) the user enterd a date in month(str) day(int), year(int)) format
#         elif date.find(',') != -1:
#             date = date.split()
#             month = date[0]
#             # We used split(',') agian on as the date[1] equal to "x," x represent a integer number as "day" in month, so we need to split them again, to extract "day" only
#             day = int(date[1].split(',')[0])
#             year = int(date[2])
#         return month, day, year

#     # If any errors raised return it
#     except (ValueError, IndexError, TypeError, UnboundLocalError) as error:
#         return error


#                 # The upcoming functiuons, make sure that month, day, and year are valid date values

# def get_valid_day(day):
#     return 1 <= day <= 31

# def get_valid_month(month):

#     # We have a two conditions here because of the two date format the program accept as input
#     if isinstance(month, int):
#         return 1 <= month <= 12
#     else:
#         if month in MONTHS:
#             return True
#         return False

# def get_valid_year(year):
#     return year >= 1





# main()



"""The second METHOD, much much cleaner and simpler, USING 'datetime' module"""


from datetime import datetime

date_str = input("Enter a date in MM/DD/YYYY or Month DD, YYYY format: ")

try:
    # try to parse the date using the first format
    date = datetime.strptime(date_str, "%m/%d/%Y")
except ValueError:
    try:
        # try to parse the date using the second format
        date = datetime.strptime(date_str, "%B %d, %Y")

    except ValueError:
        # if both formats fail, the input is invalid
        print("Invalid date format")
        exit(1)

# output the date in YYYY-MM-DD format
print(date.strftime("%Y-%m-%d"))

