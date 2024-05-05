def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")
        
def is_even(n):
    """
    if n % 2 == 0:
        return True
    else:
        return False
    """
    
    # Pythonic Expression
    return True if n % 2 == 0 else False
    
main()

# Quick note: using the dot of a function(like .strip()) is only avalible for strings or if the function returns a string.