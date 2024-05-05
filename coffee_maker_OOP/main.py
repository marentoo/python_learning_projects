from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe = CoffeeMaker()
menu = Menu()
money_machine.report()


ordering = True
while ordering:
    options = menu.get_items()

    user_choice = input(f"What would you like? ({options}): ")
    if user_choice == "off":
        ordering = False
        print("That's all. Thank You!")
    elif user_choice == "report":
        coffe.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_choice)
        if coffe.is_resource_sufficient(drink) is True and money_machine.make_payment(drink.cost) is True:
            coffe.make_coffee(drink)
