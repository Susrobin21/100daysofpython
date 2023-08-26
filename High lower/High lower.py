from Gameinfo import data
import random
import os

def clear():
    os.system('cls')

score = 0
end_game = False
b = random.choice(data)
while end_game == False :
    a = b
    b = random.choice(data)
    if a == b :
        b = random.choice(data)
    choice_a = print(f"Choice A : {a['name']} , {a['description']} , {a['country']}")
    choice_b = print(f"Choice B : {b['name']} , {b['description']} , {b['country']}")
    user_input = input('Who has more followers, A or B ? : ').lower()

    def right_choice(user_input) :
        global score
        if a['follower_count'] > b['follower_count'] and user_input == 'a' :
            score += 1
            clear()
            print(f'Correct choice !Your score is {score}')
        elif a['follower_count'] > b['follower_count'] and user_input == 'b' :
            print('Wrong choice ! Game over ')
            print(f'Your score is {score}')
            quit()
        elif a['follower_count'] < b['follower_count'] and user_input == 'b' :
            score += 1
            clear()
            print(f'Correct choice !, Your score is {score}')
        elif a['follower_count'] < b['follower_count'] and user_input == 'a' :
            print('Wrong choice ! Game over ')
            print(f'Your score is {score}')
            quit()
    right_choice(user_input)