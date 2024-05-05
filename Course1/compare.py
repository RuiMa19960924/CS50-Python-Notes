x = int(input("What's x? "))
y = int(input("Whay's y? "))

# Using keyword 'if' followed by a Boolean expresion
"""
This pattern is repetitive
if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")
    
if x == y:
    print("x is equal to y")
"""

# More efficient way using another keyword "elif", which stands for else if in English or other programming language
"""
    But in this senario, if x is either greater or smaller than y, I don't need to use keyword 'elif', which leads to the third keyword and the final version,using keyword 'else'
if x < y:
        print("x is less than y")
elif x > y:
        print("x is greater than y")
elif x == y:
        print("x is equal to y")      
"""

# Using keyword "else"
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
    
# Using "or" keyword
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
# The previous if statement can be better using conditional symbols such as
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    
# Or
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
