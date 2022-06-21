from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True

# The machine parts and the menu are created once, makes sense semantically plus not recreating resources
# or starting profit from 0

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ").lower()

    menu_item = menu.find_drink(choice)

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
    else:
        if menu_item is None:
            continue
        else:
            if coffee_maker.is_resource_sufficient(menu_item):
                cost = menu_item.cost
                if money_machine.make_payment(cost):
                    coffee_maker.make_coffee(menu_item)
                else:
                    print("There are not enough resources to make your coffee. Money refunded.")
