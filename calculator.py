calculator = True

while calculator:
    input_1 = input('Enter a number: ')
    input_2 = input('Enter another number: ')
    print('Which operation do you want to perform?')
    operator = input('addition[+] subtraction[-] multiplication[*] division[/] exponentiation[**]: ')
    
    try:
        number_1 = float(input_1)    
        number_2 = float(input_2)    
        print(10 * '-')
        if operator == '+':
            print(f'{input_1} + {input_2} = {number_1 + number_2}')
        elif operator == '-':
            print(f'{input_1} - {input_2} = {number_1 - number_2}')
        elif operator == '*':
            print(f'{input_1} x {input_2} = {number_1 * number_2}')
        elif operator == '/':
            print(f'{input_1} : {input_2} = {number_1 / number_2}')
        elif operator == '**':
            print(f'{input_1} ^ {number_2} = {number_1 ** number_2}')
        else:
            print('Error identifying the operator. Please try again.')
            calculator = True
        print(10 * '-')
        print('Do you want to use the calculator again?')
        continue_calculation = input('[y]es [n]o: ').lower()
        print(10 * '-')
        if continue_calculation == 'y':
            calculator = True
        elif continue_calculation == 'n':
            print('See you next time :D')
            break
        else:
            break
    except:
        print('One or both entered numbers are invalid')
        continue
