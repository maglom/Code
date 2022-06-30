def my_calculator(first_numb, operator, second_number):
    """Calculator

    Args:
        first_numb (INT): _description_
        operator (STR): _description_
        second_number (INT): _description_

    Raises:
        ValueError: _description_

    Returns:
        _type_: _description_
    """
    try:
        input1 = float(first_numb)
        input2 = float(second_number)
        input3 = operator
        if input3 not in '/*+-' and len(input3) == 1:
            raise ValueError
    except:
        return 'Wrong input'

    try:
        if input3 == '+':
            return input1 + input2
        elif input3 == '-':
            return input1 - input2
        elif input3 == '/':
                return input1 / input2
        elif input3 == '*':
            return input1 * input2
    except ZeroDivisionError:
            return 'You cant divide by zero'

        
input1 = input('input number')
input2 = input('input another number')
input3 = input('input operator')

print(my_calculator(input1, input3, input2))