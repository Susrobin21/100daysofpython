import random
my_list = ['aragon', 'frodo', 'samwiese','saruman']
chosen_word = random.choice(my_list)
end_of_game = False
while end_of_game == False :
    input_letter = input('Enter a letter : ').lower()
    display = []
    for letter in range(len(chosen_word)):
        display += '_'
    print(display)
    for position in range(0,len(chosen_word)) :
        letter = chosen_word[position]
        if letter == input_letter:
            display[position] = letter
    print(display)
    if '_' not in display:
        end_of_game = True
        print('You win')