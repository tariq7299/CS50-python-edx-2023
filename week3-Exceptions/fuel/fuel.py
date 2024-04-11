def main():
    # Calling get_fuel_percent() function which will convert the fuel iputed to a percent
    fuel_percent = get_fuel_percent()

    if fuel_percent == 100 or fuel_percent >= 99:
        print("F")
    elif fuel_percent == 0 or fuel_percent <= 1:
        print("E")
    else:
        print(f"{fuel_percent}%")

def get_fuel_percent():
    # This will keep prpmtoing the user as long as on of the three errors (ZeroDivisionError, ValueError, IndexError) keep rising.
    while True:
        fuel = input("What's fuel? ")
        # This will split the user input upon the char "/" into two numbers
        try:
            nominator, denominator = map(int, fuel.split("/"))
            # This will check whether the number inputed ny user is float or the nominator (x) is bigger than the denominator (z), if so it will raise a ValueEror, then the program will prpmt the user again
            if nominator > denominator:
                raise ValueError()
            fuel_percent = round((nominator/denominator) * 100)
            return fuel_percent

        except (ZeroDivisionError, ValueError, IndexError):
            pass

main()
