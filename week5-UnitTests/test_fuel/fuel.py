
def main():
    # Calling get_fuel_percent() function which will convert the fuel iputed to a percent
   # This will keep prpmtoing the user as long as on of the three errors (ZeroDivisionError, ValueError, IndexError) keep rising.

    while True:
        fuel = input("What's fuel? ")
        # This will split the user input upon the char "/" into two numbers

        try:
            fuel_percent = convert(fuel)
            print(fuel_percent)
            indicator = gauge(fuel_percent)
            print(indicator)
            break
        except (ZeroDivisionError, ValueError, IndexError):
            pass




def convert(fraction):

    try:
        nominator, denominator = map(int, fraction.split("/"))
        # This will check whether the number inputed ny user is float or the nominator (x) is bigger than the denominator (z), if so it will raise a ValueEror, then the program will prpmt the user again

        if denominator == 0:
            raise ZeroDivisionError()

        if nominator > denominator:
            raise ValueError()

        fuel_percent = round((nominator/denominator) * 100)
        return fuel_percent

    except ValueError as e:
        # Re-raise the exception with some additional information.
        raise ValueError() from e

    except ZeroDivisionError as e:
        # Re-raise the exception with some additional information.
        raise ZeroDivisionError() from e

    except IndexError as e:
        # Re-raise the exception with some additional information.
        raise IndexError() from e


def gauge(percentage):

    if percentage == 100 or percentage >= 99:
        return "F"
    elif percentage == 0 or percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
