import os

def addition(x, y):
    print(f' {x} + {y} = {x+y}')
def subtraction(x, y):
    print(f' {x} - {y} = {x-y}')
def multiplication(x, y):
    print(f' {x} x {y} = {x*y}')
def division(x, y):
    print(f' {x} : {y} = {x/y}')
def exponentiation(x, y):
    print(f' {x} ^ {y} = {x**y}')

calculator = True
while calculator:
    try:
        number_1 = float(input('Enter a number: '))
        number_2 = float(input('Enter another number: '))
        print('Which operation do you want to do?')
        operador = input('addition[+] subtraction[-] multiplication[*] division[/] exponentiation[**]: ')
    except:
        os.system('cls')
        print(10*'-')
        print('Error. Try again.')
        print(10*'-')
        continue 
    print(10*'-')
    if operador == '+':
        addition(number_1, number_2)
    elif operador == '-':
        subtraction(number_1, number_2)
    elif operador == '*':
        multiplication(number_1, number_2)
    elif operador == '/':
        division(number_1, number_2)
    elif operador == '**':
        exponentiation(number_1, number_2)
    else:
        print('Error identifying the operator. Please try again.')
        calculator = True
    print(10*'-')
    print('Do you want to use the calculator again?')
    continue_calculation = input('[y]es [n]o: ')
    print(10*'-')
    if continue_calculation.startswith('y'):
        calculator = True
        os.system('cls')
    else:
        os.system('cls')
        print('See you later :D')
        break
