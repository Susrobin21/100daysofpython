#bmi calculator


height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = round(int(weight)/(float(height)**2))
print(bmi)
# if bmi <= 18 :
#     print('You are under weight')
# elif bmi >18 | bmi <= 24 :
#     print('You are of normal weight ')
# else :
#     print('You are overweight') this code comes under flow control and logical operators