from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machine_is_on = True

while machine_is_on:
    options = menu.get_items()
    choice: str = input(f"what would you like? {options}: ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machine_is_on = False
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)



# TODO 1. Print Report
# TODO 2. Check Resources Sufficient
# TODO 3. Process Coins
# TODO 4. Check Transaction Successful
# TODO 5. Make Coffee
