numberOne = float(input('Enter the first number: '));
numberTwo = float(input('Enter the second number: '));

def sum(numberOne, numberTwo):
    return numberOne + numberTwo

def subtract(numberOne, numberTwo):
    return numberOne - numberTwo

def multiply(numberOne, numberTwo):
    return numberOne * numberTwo

def divide(numberOne, numberTwo):
    return numberOne / numberTwo

select = input('Select the operation(+, -, *, /): ')

if(select == '+'):
    print('Result: ' , numberOne, '+', numberTwo, '=', sum(numberOne,numberTwo))
elif(select == '-'):
    print('Result: ' , numberOne, '-', numberTwo, '=', subtract(numberOne,numberTwo))
    
elif(select == '*'):
    print('Result: ' , numberOne, '*', numberTwo, '=', multiply(numberOne, numberTwo))
    
elif(select == '/'):
    print('Result: ' , numberOne, '/', numberTwo, '=', divide(numberOne, numberTwo))

else:
    print('Invalid Input!')
    
