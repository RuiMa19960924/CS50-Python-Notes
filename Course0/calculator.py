# Get 2 input from user and convert them into integer
x = int(input("What is x? "))
y = int(input("What is y? "))

#print result
print(x + y)

"""
float number

x = float(input("What is x? "))
y = float(input("What is y? "))
z = round(x + y)

# using f (a feature of python) to make bigger number more official format
print(f"{z:,}")
# Results will be 1,000 not 1000, etc..

"""

# division and floating
a = int(input("What is a? "))
b = int(input("What is b? "))
z = a / b

# using F string to print the result of a rounded number with 2 decimal digits
print(f"{z:.2f}")


# Creat  main function
def main():
    number = int(input("What's the number? "))
    print("number squared is", square(number))
    
# Define a function called square
def square(n):
    return n * n
    # return n ** 2
    # return pow(n, 2)

# Call the main function
main()
