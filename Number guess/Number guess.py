import random
easy_level = 10
medium_level = 7
hard_level = 5

def check_answer(guess_number,answer,chances) :
    if answer == guess_number :
        print(f'Yay ! You got the right answer, the number is {answer}')
    elif answer > guess_number :
        print('Too high')
        return chances - 1
    elif answer < guess_number :
        print('Too low')
        return chances - 1

def difficulty():
    hardness = input('Enter a difficulty, easy medium or hard : ').lower()
    global chances
    if hardness == 'easy' :
        return easy_level
    elif hardness == 'medium' :
        return medium_level
    elif hardness == 'hard' :
        return hard_level
    else :
        print('Enter a valid input.')
def game():
    guess_number = random.randint(0,100)
    chances = difficulty()
    answer = 0
    while answer != guess_number :
        print(f'You have {chances} left to guess the number')
        answer = int(input('Guess the number : '))
        chances = check_answer(answer,guess_number,chances)
        if chances == 0 :
            print('Out of chances, Game over !')
            print(f'The answer is {answer}')
            quit()
        elif answer != guess_number :
            print('Guess again')
game()



