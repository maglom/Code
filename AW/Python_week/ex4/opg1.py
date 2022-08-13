

try:
    input1 = float(input('input number'))
    input2 = float(input('input another number'))
    input3 = input('input operator')
    if input3 not in '/*+-' and len(input3) == 1:
        raise ValueError
except:
    print('Wrong input')

try:
    if input3 == '+':
        print(input1 + input2)
    elif input3 == '-':
        print(input1 - input2)
    elif input3 == '/':
            print(input1 / input2)
    elif input3 == '*':
        print(input1 * input2)
except ZeroDivisionError:
        print('You cant divide by zero')

        
 