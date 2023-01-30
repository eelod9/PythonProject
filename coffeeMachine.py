MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

Inventory = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

Coin= {
    'quarters':.25,
    'dimes': .10,
    'nickles': .5,
    'pennies': .1

}
def printInventory():
    for keys, values in Inventory.items():
        print(f"{keys.title()}:  {values} ml ")
    print(f'Money: {money}')


def checkInventory(coffee):
    recipe = MENU[coffee]['ingredients']
    for key, values in recipe.items():
        if(Inventory[key] < values):
            print(f"Sorry there is not enough {key}.")
            return False
        else:
            return True

def calcCoin(money):
    for key, values in Coin.items():
        coinCount = input(f"How many {key}")
        money += float(coinCount) * float(values)    
        cash ="%.2f" % money
        print(f"MOney {cash}")
    return cash

def dispense(coffee):
    recipe = MENU[coffee]['ingredients']
    for key, values in recipe.items():
        temp = Inventory[key]
        Inventory[key] = temp - values
    print(f"Here is your {coffee}")

coffeeMachine = True

while(coffeeMachine):
    coffee = input('What would you like? (espresso/latte/cappuccino): ') #report
    if(coffee == 'report'):
        printInventory()
    elif(checkInventory(coffee)):
        print("Please insert coins.")
        insertedCoin = calcCoin(money)
        change = float(insertedCoin) - float(MENU[coffee]['cost'] )
        if(change< 0): #not enough money
            print("Sorry that's not enough money. Money refunded.")
        else:
            print(f"Here is ${change} in change")
            dispense(coffee)

        
        
   