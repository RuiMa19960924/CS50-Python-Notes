name = input("What's your name? ")

# Using keyword "match" to avoid tedious if statements
match name:
    case "Harry"| "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
# Notice in Python "match", I don't need to have a "default" or "break" like some other languages, the "_" perfromances the similar use as a default value in "Switch" statement.

# Try to figure out the git...not working