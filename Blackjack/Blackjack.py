import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
user_score = 0
computer_score= 0
while True :
    def blackjack():
        usercard1 = random.choice(cards)
        usercard2 = random.choice(cards)
        computercard1 = random.choice(cards)
        computercard2 = random.choice(cards)
        user_score = usercard1 + usercard2
        computer_score = computercard1 + computercard2
        print(f'Your draws are {usercard1},{usercard2}')
        print(f"Computer's first card is {computercard1}")
        def final_user_result():
            print(f'You win !')
            print(f'Your score is {user_score} and computer score is {computer_score}')
        def final_computer_result():
            print(f'Computer wins !')
            print(f'Your score is {user_score} and computer score is {computer_score}')
            
        def draw():
            print('Draw match !')
            print(f'Your score is {user_score} and computer score is {computer_score}')
            
        
        another_card = input('Do you want to draw another card ? : ')
        if another_card == 'yes' :
            usercard3 = random.choice(cards)
            user_score += usercard3
            if user_score > computer_score and user_score <= 21 :
                print(f'Your last card is {usercard3}')
                final_user_result()
            elif computer_score > user_score or user_score > 21 or computer_score == 21 :
                print(f'Your last card is {usercard3}')
                final_computer_result()
            elif computer_score == user_score :
                print(f'Your last card is {usercard3}')
                draw()
        else:
            if computer_score <= 16 :
                computercard3 = random.choice(cards)
                computer_score += computercard3
            if user_score == 21 or user_score > computer_score or computer_score > 21:
                final_user_result()
            elif computer_score == 21 or (computer_score > user_score and computer_score <21 ):
                final_computer_result()
            elif user_score and computer_score == 21 :
                draw()
    blackjack()
    play_again = input('Do you want to play again ? : ').lower()
    if play_again == 'yes' :
        blackjack()
    else :
        quit()
