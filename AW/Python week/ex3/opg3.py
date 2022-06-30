current_number = 100
total_numb = 100
progress = current_number/total_numb
bar_length = 10

bar = '=' * int((progress * bar_length))
space = ' ' * int((9.0-(progress * bar_length)))

if current_number == total_numb:
    print(f'|{bar}{space}|')
    print('Done')
else:
    print(f'|{bar}>{space}|', end='')

