def greet():
    # Review:
    # Create a function called greet().
    # Write 3 print statements inside the function.
    # Call thegreet() function and run your code.

    print("Good morning sunshine")
    print("The earth")
    print("Says hello")

def greet_with_name(name):
    print(f"Good morning {name}")
    print("The earth")
    print("Says hello")

def greet_with(name, location):
    print(f"Good morning {name}")
    print(f"How's the weather in {location}?")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    greet_with(location="Munich", name="Kat")
