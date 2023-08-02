import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_pool = ['arrancar','ichigo','quincy','aizen','ikkaku','orihime']
chosen_word = random.choice(word_pool)
length = len(chosen_word)
print(chosen_word)
empty = []
for m in range(length):
    empty += ('_')
lives = 7
end_game = False
while end_game == False :
    guess = input('Enter the letter : ').lower()
    for i in range(0,length):
        if guess == chosen_word[i]:
            empty[i] = chosen_word[i]
    if guess not in chosen_word:
        lives -=1
        print(stages[lives])
        if lives == 0 :
            end_game = True
            print('You lost :(')
    print(empty)

    if '_' not in empty:
        end_game = True
        print('You won !!')