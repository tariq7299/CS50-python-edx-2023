
            # The simple version that takes only tiime as 24h format
# def main():
#     time = input("Enter time in 24-hour format (HH:MM): ")
#     newFormatedTime  = convert(time)

#     if  7.0 <= newFormatedTime <= 8.0:
#         print("breakfast time")
#     elif  12.0 <= newFormatedTime <= 13.0:
#         print("lunch time")
#     elif 18.0 <= newFormatedTime <= 19.0:
#         print("dinner time")

# def convert(time):
#     h, m = map(int, time.split(':'))
#     m = (m/6) * 0.1
#     # m = math.trunc(m)
#     time = h + m

#     return time


# if __name__ == "__main__":
#     main()

                                                # challange accepted
#           #       #       This version of program takes two types of inputs 12h and 24h     #       #       #

def main():

    time = input("Enter time in 24-hour format (HH:MM): ").lower()

    if time[-2:] == "am" or time[-2:] == "pm":
        format_12h = time
        format_24h = convert24(format_12h)
        # print(format_12h)
        # print(format_24h)
        format_Float = convert(format_24h)
        # print(format_Float)
    else:
        format_Float = convert(time)
        # print(format_Float)


    if  7.0 <= format_Float <= 8.0:
        print("breakfast time")
    elif  12.0 <= format_Float <= 13.0:
        print("lunch time")
    elif 18.0 <= format_Float <= 19.0:
        print("dinner time")

def convert24(format_12h):

    # Checking if last two elements of time
    # is AM and first two elements are 12
    if format_12h[-2:] == "am" and format_12h[:2] == "12":
        return "00" + format_12h[2:-2]

    # remove the AM
    elif format_12h[-2:] == "am":
        return format_12h[:-2]

    # Checking if last two elements of time
    # is PM and first two elements are 12
    elif format_12h[-2:] == "am" and format_12h[:2] == "12":
        return format_12h[:-2]

    else:

        # add 12 to hours and remove PM
        return str(int(format_12h[:2]) + 12) + format_12h[2:5]

def convert(time):
    h, m = map(int, time.split(':'))
    m = (m/6) * 0.1
    # m = math.trunc(m)
    time = h + m

    return time


if __name__ == "__main__":
    main()
