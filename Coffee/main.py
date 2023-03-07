from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMaker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
def checkCoffee(coffee):
    return coffeeMaker.is_resource_sufficient(coffee)

coffee = True
while(coffee):
    userInput = input("What would you like? (espresso/latte/cappuccino): ")
    if(userInput == "off"):
        print("Goodbye")
        break
    elif(userInput == "report"):
        coffeeMaker.report()
    elif(userInput=="espresso", "latte", "cappuccino"):
        mi = menu.find_drink(userInput)
        #print(mi)
        enoughResources = checkCoffee(mi)
        if(enoughResources) and money_machine.make_payment(mi.cost):
            coffeeMaker.make_coffee(mi)



 

            
    