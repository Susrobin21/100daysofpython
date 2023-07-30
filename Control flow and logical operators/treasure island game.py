#treasure island game
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    .--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .  `` ,  `"-._"-._   ". '|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,.--o;   |
|___________________|_| ;     (#) -.o "=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('Welcome to treasure island simulation game') 
print('Here you will have to enter choices to proceed in the game , you will either be safe or dead depending upon your choice')

choice1 = (input('You have 2 paths on your front, choose one of them, enter left or right : ')).lower()
if choice1 =='left' :
    print('This trial lead you to a river')
    choice2 = input('Choose if you are willing to swim or not , enter yes or no :').lower()
    if choice2 == 'no' :
        print('A boat is found coming towards you , you got on it and crossed the river ')
        choice3 = input('You came to a mysterious island , choose if you are willing to enter the temple , type yes or no :').lower()
        if choice3 == 'yes':
            print('You can see 3 door now , gold, silver and bronze')
            input('Choose one of them : ').lower()
            if choice3 == 'silver' :
                print('You entered a room with silver coated mayan tribals, GAME OVER ')
            elif choice3 == 'gold':
                print('You see a gold cannon pointed at you, it shoots a cannon ball, BOOM HEADSHOT')
            else :
                print('You see a bronze chest filled with treasure , YOU WIN !')
        else :
            print('You are hunted down by present mayan tribals, GAME OVER')
    else :
        print('The river is filled with swamp puppies, ie crocodiles , GAME OVER')
else :
    print('You fell down in a 20 ft pithole, SOLDIER FELL')
