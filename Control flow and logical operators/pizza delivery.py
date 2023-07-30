#pizza delivery
print("Welcome to Castlevania pizza")
size = input("What size pizza do you want? S, M, or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
extra_cheese = input("Do you want extra cheese? Y or N : ")
bill = 0
if size == 'S':
    bill += 250
elif size =='M':
    bill += 300
elif size == 'L':
    bill += 300
if add_pepperoni =='Y':
    if size == 'S':
        bill += 3
    else :
        bill += 5
if extra_cheese == 'Y':
    if size == 'S':
        bill += 10
    else :
        bill += 15
print(f'Your final bill is {bill}')