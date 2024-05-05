"""

# Ask user for their name
name = input("What's your name? ").strip().title()

#Split method
first, last = name.split(' ')

# Greeting user
print(f"Hello, {name}")

"""

"""

# Define a function called hello and set the default value of its arguement to "world"
def hello(to = "world"):
    print("Hello,", to)
    
hello()
name = input("What's your name? ")
hello(name)

"""
# Main function included
def main():
    # Ask for user's name
    name = input("What's your name? ")
    
    # call greeting function called hello
    hello(name)
    
def hello(to = "world") :
    print("Hello,",to)
    
# Call the main function
main()
    