MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {resources["water"]}")
    print(f"Milk: {resources["milk"]}")
    print(f"Coffee: {resources["coffee"]}")
    print(f"Money: {profit}")


def start_machine():
    choice = input("What would you like? (espresso/latte/cappuccino):")




def is_resources_sufficient(drink):
    water = MENU[drink]["ingredients"]["water"]
    coffee = MENU[drink]["ingredients"]["coffee"]
    milk = MENU[drink]["ingredients"]["milk"]
    message = "“Sorry there is not enough "
    enough = True

    if water > resources["water"]:
        print(message + "water.")
        enough = False
    if milk > resources["milk"]:
        print(message + "milk.")
        enough = False
    if coffee > resources["coffee"]:
        print(message + "coffee.")
        enough = False
    return enough

# def process_coins(choice):
    