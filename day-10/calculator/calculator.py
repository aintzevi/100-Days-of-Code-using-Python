from art import logo

def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts two numbers. Might return a negative value"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two numbers."""
    return n1 * n2


def divide(n1, n2):
    """Divides n1 by n2."""
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator():

    operation_str = ""
    for operation_symbol in operations:
        operation_str += operation_symbol + " "

    should_continue = True
    num1 = float(input("What's the first number?: "))

    while should_continue:
        print(operation_str)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or "
                       f"any other character to exit the calculator: ")
        if choice == "y":
            num1 = answer
        elif choice == "n":
            should_continue = False
            calculator()
        else:
            return


print(logo)
calculator()
