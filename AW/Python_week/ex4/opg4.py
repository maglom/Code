current_number = 250
total_numb = 375
progress = current_number/total_numb
bar_length = 100

bar = '=' * round((progress * bar_length))
space = ' ' * int((bar_length-round(progress * bar_length)))

if current_number == total_numb:
    print(f'|{bar}{space}|')
    print('Done')
else:
    print(f'|{bar}>{space}|', end='')

