import random

roll = 'r'
sides = int(input('How many sides does the dice have? '))
roll_number = int(input('Please specify the number of rolls '))
x = 0
while x in range(roll_number) and roll != 'e':
    number = random.randint(1,sides)
    print('The result: ', number)

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

    roll = input('Press r to roll again Or e to exit> ').lower() 






'''def inputValidation(input_string):
    if input_string.strip() in {'1','2','3','4','5','6'}:
        return int(input_string)
    else:
        print('Please enter a number from 1 to 6')'''