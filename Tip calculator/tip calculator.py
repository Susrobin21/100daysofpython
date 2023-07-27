#tip calculator

print('Welcome to tip calculator')

bill = float(input('What was the total bill ? : '))
tip = int(input('What percentage tip would you like to give , 10 or 12 or 15 ? : '))
number = int(input('How many people to split the bill ? : '))
split = float(bill/number)
total_tip = (tip*bill)/100
each_tip = total_tip/7
total = split + each_tip
print(f'Each prson should split : {total}')
