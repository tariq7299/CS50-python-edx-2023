
# The speed of light as variable "c"
c = 300000000

# The mass value that will be taken from the user as input
# Here I used int() as without the type of the input will be str, and will not be able to do any calculations on !, 
m = int(input("What is the mass in kg ? "))

# The formula that will calculate the energy
E = m * c ** 2

print("The Energy is of the mass you typed is : ", E)