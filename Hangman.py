import random

words = ['pretty','successful','smart','style']
random_word = list(random.choice[words]) #make it a list to compare each letter with the guessed letter


for i in range(random_word):
    user_input = input('Guess a letter: ')
    if user_input == random_word[i]:
        print(user_input)



Hangman_img = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''
]