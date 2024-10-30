import random

roll = 'r'
sides = int(input('How many sides does the dice have? '))
roll_number = int(input('Please specify the number of rolls '))
x = 0
while x in range(roll_number) and roll != 'e':
    number = random.randint(1,sides)
    print('The result: ', number)

    #the dice sides 
    if number == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    if number == 2:
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
    if number == 3:
        print("[-----]")
        print("[0    ]")
        print("[  0  ]")
        print("[    0]")
        print("[-----]")
    if number == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    if number == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    if number == 6:
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")

    # r to roll again or e to exit the game
    roll = input('Press r to roll again Or e to exit> ').lower() 
