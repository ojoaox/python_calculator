import os

def soma(x, y):
    print(f' {x} + {y} = {x+y}')
def subtracao(x, y):
    print(f' {x} - {y} = {x-y}')
def multiplicacao(x, y):
    print(f' {x} x {y} = {x*y}')
def divisao(x, y):
    print(f' {x} : {y} = {x/y}')
def potenciacao(x, y):
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
        soma(number_1, number_2)
    elif operador == '-':
        subtracao(number_1, number_2)
    elif operador == '*':
        multiplicacao(number_1, number_2)
    elif operador == '/':
        divisao(number_1, number_2)
    elif operador == '**':
        potenciacao(number_1, number_2)
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
