import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r'(\d+):(\d+)\s(am|pm)\s?to\s?(\d+):(\d+)\s(am|pm)', s, re.IGNORECASE):

        hours_1 = int(matches.group(1))
        minutes_1 = int(matches.group(2))
        period_1 = matches.group(3).lower()
        hours_2 = int(matches.group(4))
        minutes_2 = int(matches.group(5))
        period_2 = matches.group(6).lower()

        if 0 <= hours_1 <= 12 and 0 <= hours_2 <= 12 and 0 <= minutes_1 < 60 and 0 <= minutes_2 < 60:

            if period_1 == 'pm' and hours_1 != 12:
                hours_1 += 12
            if period_1 == 'am' and hours_1 == 12:
                hours_1 = 0

            if period_2 == 'pm' and hours_2 != 12:
                hours_2 += 12
            if period_2 == 'am' and hours_2 == 12:
                hours_2 = 0

            return f'{hours_1:02d}:{minutes_1:02d} to {hours_2:02d}:{minutes_2:02d}'
        else:
            raise ValueError("Invalid time range")
        
    elif matches := re.search(r'(\d+)\s(am|pm)\s?to\s?(\d+)\s(am|pm)', s, re.IGNORECASE):

        hours_1 = int(matches.group(1))
        period_1 = matches.group(2).lower()
        hours_2 = int(matches.group(3))
        period_2 = matches.group(4).lower()

        if 0 <= hours_1 <= 12 and 0 <= hours_2 <= 12 :

            if period_1 == 'pm' and hours_1 != 12:
                hours_1 += 12
            if period_1 == 'am' and hours_1 == 12:
                hours_1 = 0

            if period_2 == 'pm' and hours_2 != 12:
                hours_2 += 12
            if period_2 == 'am' and hours_2 == 12:
                hours_2 = 0
            return f'{hours_1:02d}:00 to {hours_2:02d}:00'
        else:
            raise ValueError("Invalid time range")

    else:
        raise ValueError("Invalid time range")





# Some experiments
# import re

# def convert(time_str):
#     # Extract hour, minute, second, and AM/PM parts
#     hour1, minute1, am_pm1, to, hour2, minute2, am_pm2 = re.findall(r'\d+|\w+', time_str)
#     hour1 = int(hour1)
#     hour2 = int(hour2)

#     # Convert AM/PM to 24-hour format
#     if am_pm1 == 'PM' and hour1 != 12:
#         hour1 += 12
#     elif am_pm1 == 'AM' and hour1 == 12:
#         hour1 = 0

#     # Convert AM/PM to 24-hour format
#     if am_pm2 == 'PM' and hour2 != 12:
#         hour2 += 12
#     elif am_pm2 == 'AM' and hour2 == 12:
#         hour2 = 0

#     # Format the time
#     return f'{hour1:02d}:{minute1} to {hour2:02d}:{minute2}'


# import re

# def convert_time(time_str):
#     match = re.match(r'(\d+):(\d+) (\w+)', time_str)
#     if match:
#         hour, minute, period = match.groups()
#         hour = int(hour)
#         if period.lower() == 'pm':
#             hour += 12
#         return f'{hour:02}:{minute}'

# # Test the function
# print(convert_time("02:30 PM"))  # Output: 14:30

if __name__ == "__main__":
    main()
