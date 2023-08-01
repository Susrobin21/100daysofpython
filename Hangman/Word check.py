import random
my_list = ['aragon', 'frodo', 'samwiese','saruman']
chosen_word = random.choice(my_list)
input_letter = input('Enter a letter : ').lower()

for i in range(0,len(chosen_word)) :
    if chosen_word[i] == input_letter:
        print('Right')
    else :
        print('Wrong')
