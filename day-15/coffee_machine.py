import data


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

QUARTER = 0.25
DIME = 0.10
NICKEL = 0.05
PENNY = 0.01


def print_report():
    """Prints the resources left in the machine, as well as the money inside"""

    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}gr")
    print(f"Money: ${profit}")


def check_resources():
    """Returns True if the resources are sufficient to make the requested coffee or False otherwise"""
    for item in resources:
        if resources[item] <= data.MENU[choice]["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def update_resources():
    """Updates the resources by removing resources needed when making a coffee"""
    resources["water"] -= data.MENU[choice]["ingredients"]["water"]
    resources["milk"] -= data.MENU[choice]["ingredients"]["milk"]
    resources["coffee"] -= data.MENU[choice]["ingredients"]["coffee"]


def insert_money():
    """Handles the coin insertion from the user and returns the overall amount the user has given"""
    print("Please insert coin.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    return quarters * QUARTER + dimes * DIME + nickels * NICKEL + pennies * PENNY


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources():
            change = insert_money() - data.MENU[choice]["cost"]
            if change >= 0:
                profit += data.MENU[choice]["cost"]
                update_resources()
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Enjoy!")

            else:
                print("Sorry that's not enough money. Money refunded.")

    elif choice == "report":
        print_report()
    elif choice == "off":
        is_on = False
    else:
        print("Please select a valid option!")