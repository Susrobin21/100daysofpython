from Report import menu
from Report import resources
from Report import profit

def check_resources(ingrediento):
    enough = True
    for all in ingrediento :
        if ingrediento[all] >= resources[all] :
            print(f'Sorry :( there is not enough {all}')
            enough = False
    return enough

def money():
    total = int(input('Enter the number of tens : '))*10
    total += int(input('Enter the number of twenties : '))*20
    total += int(input('Enter the number of fifties : '))*50
    total += int(input('Enter the number of hundreds : '))*100
    return total
def transaction_successful(paid,costofcoffee) :
    global profit
    if paid >= costofcoffee :
        change = paid - costofcoffee
        print(f'Here is your change {change}')
        profit += costofcoffee
        return True
    else :
        print('Sorry , not enough money, money returned ')
        return False
def make_coffee(name, ingredients):
    for all in ingredients :
        resources[all] - ingredients[all]
    print(f'Here is your {name} !')
while True :
    choice = input('What would you like to have ,cappuccino, espresso or latte ? :').lower()
    if choice == 'off' :
        quit()
    elif choice == 'report' :
        print(f"water : {resources['water']} ml")
        print(f"milk : {resources['milk']} ml")
        print(f"coffee : {resources['coffee']} gms")
        print(f"money : ₹ {profit}")
    else :
        coffee = menu[choice]
        print(coffee)
        if check_resources(coffee['ingredients']) :
            payment = money()
            if transaction_successful(payment,coffee['cost']):
                make_coffee(choice,coffee['ingredients'])
