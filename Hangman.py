import random

#words list
words = ['pretty','successful','smart','style']

#randomly choosing the word
def chose_word():
    random_word = random.choice(words) #make it a list to compare each letter with the guessed letter
    return random_word.upper()

#the game main concept
def play(random_word):
    word_guessed = '_' * len(random_word) # variable with the same length of the random word but underscore values
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6 
    print("Welcome to Hangman game, Let's play")
    print(display_hangman(tries))
    print(word_guessed, "\n")

    while not guessed and tries > 0:
        guess = input("Please Guess a letter or word> ").upper()
        if len(guess) == 1 and guess.isalpha():
            #if the guessed letter is already guessed
            if guess in guessed_letters:
                print("You already guessed this letter")
            #if the guessed letter is not in the word
            elif guess not in random_word: 
                print(guess, "is not in the word, Try again")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job", guess, "is in the the word")
                guessed_letters.append(guess)
                word_as_list = list(word_guessed) #to make the guessed word variable a list
                indices = [i for i, letter in enumerate(random_word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_guessed = ''.join(word_as_list)
                if '_' not in word_guessed:
                    guessed = True
        elif len(guess) == len(random_word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != random_word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_guessed = random_word
        else:
            print("Invalid letter or word")
        
        print(display_hangman(tries))
        print(word_guessed, "\n")

    if guessed:
        print("Congrats, you guessed the word! \n")
    else:
        #if guessed is false and the tries = 0
        print("Sorry you run out of tries, the word is : ",random_word)


#Hangman game display function 
def display_hangman(tries):
    Hangman_img = [
         '''
      +---+
      |   |
      O   |
    / | \  |
    /  \  |
          |
    =========''', '''
      +---+
      |   |
      O   |
    / | \  |
    /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
    / | \  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
    / |   |
          |
          |
    =========''','''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''','''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''','''
      +---+
      |   |
          |
          |
          |
          |
    =========''',
    ]
    return Hangman_img[tries]

def main():
    random_word = chose_word()
    play(random_word)
    #play again 
    while input("Play Again? (Y/N) ").upper() == "Y":
        random_word = chose_word()
        play(random_word)

if __name__ == "__main__":
    main()
    