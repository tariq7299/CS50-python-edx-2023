# Import necessary libraries
import pyfiglet
import random
import sys

# print (pyfiglet.FigletFont.getFonts())
def main():
    # Check if the user has provided a font option
    if len(sys.argv) == 3:
        # If the option is not -f or --font, exit the program
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")

        # Get the font name from the command line arguments
        font = sys.argv[2]

        for FONT in pyfiglet.FigletFont.getFonts():
            if FONT == font:
                # Create a Figlet object with the specified font
                figlet = pyfiglet.Figlet(font=font)

                # Get user input for the text to be displayed
                text = input("Input: ")

                # Generate and print the ASCII art text
                result = figlet.renderText(text)

                print(result)

                return 0

        sys.exit("Invalid usage")


    # If no options are provided, choose a random font
    elif len(sys.argv) == 1:
        # Get a list of available fonts in pyfiglet
        fonts = pyfiglet.FigletFont.getFonts()

        # Choose a random font from the list
        random_font = random.choice(fonts)

        # Get user input for the text to be displayed
        text = input("Input: ")

        # Create a Figlet object with the random font
        figlet = pyfiglet.Figlet(font=random_font)

        # Generate and print the ASCII art text
        result = figlet.renderText(text)
        print(result)

    # If any other options are provided, exit the program
    else:
        sys.exit("Invalid usage")

main()