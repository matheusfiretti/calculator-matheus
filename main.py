logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calculator(a,b,operator):
    if operator == '+':
        return (a+b)
    elif operator == '-':
        return (a-b)
    elif operator == '*':
        return (a*b)
    else:
        return (a/b)


def calcular():
    print(logo)
    first_number = float(input("What's the first number? "))
    calculando = True

    while calculando:
    
        operation = input(' +\n -\n *\n /\nPick an operation: ')
        second_number = float(input("What's the second number? "))
        resultado = calculator(first_number, second_number, operation)
        print(f'{first_number} {operation} {second_number} = {resultado}')
        continua = input(f'Type "y" to continue calculating with {resultado}, or type "n" to start a new calculation: ')

        if continua == 'y':
            first_number = resultado
        else:
            calculando == False
            calcular()
calcular()
