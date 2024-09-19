from resources import resources
from menu import MENU


def report(res, menu, ordered_coffee):
    cost = menu[ordered_coffee]["cost"]

    if res["water"] >= menu[ordered_coffee]["ingredients"]["water"]:
        updated_water = res["water"] - menu[ordered_coffee]["ingredients"]["water"]
    else:
        print("Sorry there is not enough water.")
        cost = 0
        resources_updated = {}
        return resources_updated, cost

    if res["milk"] >= menu[ordered_coffee]["ingredients"]["milk"]:
        updated_milk = res["milk"] - menu[ordered_coffee]["ingredients"]["milk"]
    else:
        print("Sorry there is not enough milk.")
        cost = 0
        resources_updated = {}
        return resources_updated, cost
    
    if res["coffee"] >= menu[ordered_coffee]["ingredients"]["coffee"]:
        updated_coffee = res["coffee"] - menu[ordered_coffee]["ingredients"]["coffee"]
    else:
        print("Sorry there is not enough coffee.")
        cost = 0
        resources_updated = {}
        return resources_updated, cost
    
    resources_updated = {"water": updated_water, "milk": updated_milk, "coffee": updated_coffee}
    return resources_updated, cost


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successfull(money_recieved, drink_cost):
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is change: {change}")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that s not enough money. Money refunded.")
        return False

money = 0
ordering = True
while ordering:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        ordering = False
        print("That's all. Thank You!")
    elif user_choice == "report":
        print(f'Water: {resources["water"]}')
        print(f'Milk:{resources["milk"]},')
        print(f'Coffee: {resources["coffee"]}')
        print(f' Cost is: {money}')
    else:
        resources, price = report(resources, MENU, user_choice)
        payment = process_coins()
        is_transaction_successfull(payment, price)
