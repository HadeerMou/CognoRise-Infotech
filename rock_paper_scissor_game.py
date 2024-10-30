import random

print('Welcome to Rock, Paper, Scissor Game \n Game logic:\n Rock beats scissors, scissors beat paper, and paper beats rock.\n Instructions:\n You will play with the computer')
playAgain = 'y' #initialize the variable with this value to start looping
userScore = 0   #variable to store user score
computerScore = 0   #variable to store computer score

#the main loop of the game
while playAgain:
    choice = ['rock', 'paper', 'scissor']
    random_index = random.randrange(len(choice))
    user = input(f'Choose one: {choice} ').lower()
    computer = choice[random_index] # get a random choice for the computer

    print('You choosed: ', user)
    print('The computer choosed: ',computer)

    #tie case
    if user == computer:
        print(f"Both players selected {user}. It's a tie!")

    #computer winning case
    elif user == 'rock' and computer == 'paper' or user == 'paper' and computer == 'scissor' or user == 'scissor' and computer == 'rock':
        print('Computer Wins')
        computerScore += 1
    
    #user winning case
    elif computer == 'rock' and user == 'paper' or computer == 'paper' and user == 'scissor' or computer == 'scissor' and user == 'rock':
        print('You Win')
        userScore += 1

    playAgain = input('Play Again? (y/n) ')
    #printing the score with the winning case
    if playAgain.lower() == 'n':
        if userScore > computerScore:
            print(f'You won with a score of {userScore} and Computer loses with a score of {computerScore}')
        elif computerScore > userScore:
            print(f'Computer won with a score of {computerScore} and You lose with a score of {userScore}')
        break