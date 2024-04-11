def main():

    # Taking input for variables x, y, and z
    Expression = input("Enter values for x, y, and z separated by a space: ")

    result = calculateUserInput(Expression)


    # Printing the result
    print(result)


def calculateUserInput(Expression):

    # Splitting the input string into a list of values
    input_list = Expression.split()

    # Assigning values to variables x, y, and z
    x = float(input_list[0])
    y = input_list[1]
    z = float(input_list[2])

    # Performing the mathematical operation based on the operator
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z

    return result





main()