def add(first_number, second_number) :
    return int(first_number) + int(second_number)

def subtract(first_number, second_number) :
    return int(first_number) - int(second_number)

def multiply(first_number, second_number) :
    return int(first_number) * int(second_number)

def divide(first_number, second_number) :
    return int(first_number) / int(second_number)

operator = {
    '+' : add,
    '-' : subtract,
    '*' : multiply,
    '/' : divide
}
def calculator() :
    num1 = int(input('Enter the first number : '))
    for symbol in operator :
        print(symbol)
    should_continue = True
    while should_continue == True :
        operation_symbol = input('Choose an operator from the above : ')
        num2 = int(input('Enter the next number : '))
        calculation = operator[operation_symbol]
        first_answer =  calculation(num1,num2)
        print(f'{num1} {operation_symbol} {num2} = {first_answer}')
        calcagain = input(f'Type yes to continue calculating with {first_answer} ,no to start again and exit to exit : ')
        if calcagain == 'yes' :
            num1 = first_answer
        elif calcagain == 'no' :
            should_continue = False
            calculator()
        else :
            should_continue = False
        
calculator()

