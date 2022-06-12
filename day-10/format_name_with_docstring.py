# Docstrings are the small descriptions appearing for a function (like javadoc)

def format_name (f_name, l_name):
    if f_name == "" or l_name == "":
        """Take the first and last name and format it to return the capitalized version of the name"""
        return "You didn't provide valid inputs"
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()

    return f"Result: {formatted_f_name} {formatted_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))
