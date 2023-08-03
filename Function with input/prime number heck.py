def prime_number(number):
    for i in range(2,int(number)):
        prime = True
        if number%i == 0:
            prime = False
    if prime == True :
        print(f'{number} is a prime number')
    else :
        print(f'{number} is not a prime number')

checknumber = int(input('Enter the number to check whether it is prime number or not : '))
prime_number(checknumber)