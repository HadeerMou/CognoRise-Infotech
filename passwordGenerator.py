import secrets
import string

#default value for the value is yes to start the loop
generate = 'yes'

#loop to generate passwords as much as the user wants
while (generate == 'yes'):
    length = int(input('Please Specify the password length: '))
    complexity = str(input('Please specify the complexity of your password (hard/easy)'))
    #generating  complex password
    if complexity == "hard":
        if length >= 12:
            password = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for l in range(length))
        else:
            print('Length should be bigger than 12 to be comples')
            length = int(input('Please Specify the password length: '))
            password = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation) for l in range(length))
    #generating  easy password
    elif complexity == "easy":
        password = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for l in range(length))
    #if the user entered any string other (easy or hard) then this code excutes
    else:
        print('Please choose (hard / easy)?')
        complexity = str(input('Please specify the complexity of your password (hard/easy)'))
    #print the generated password
    print("The generated password is: " + str(password))
    #This code for the user to choose to continue generating other password or exit the loop
    generate = str(input("Want to generate another password? (yes/no) ?")).lower() 
