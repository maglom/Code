<<<<<<< HEAD
def title_case(title, minor_words=''):
    ls = title.split()
    bs = []
    minor_words = minor_words.split()
    for i in ls:
        if i in minor_words[1:]:
            bs.append(i.lower())
        else:
            bs.append(i.capitalize())
    return ' '.join(bs)

title_case('THE WIND IN THE WILLOWS', 'The In')
=======
import random

repetitions = 100000
print('Monty Hall Test:\n')
count_win = 0
count_fail = 0
for i in range(repetitions):
    doors = ['a', 'b', 'c']
    fact = random.choice(doors)
    choice = random.choice(doors)
    if choice == fact:
        count_fail += 1
    else:
        count_win += 1
print(f' Changing choice:')
print(f' wins = {count_win}')
print(f' fails = {count_fail}')
print(f' win% = {(count_win/repetitions) * 100}\n')
count_win = 0
count_fail = 0
for i in range(repetitions):
    doors = ['a', 'b', 'c']
    fact = random.choice(doors)
    choice = random.choice(doors)
    if choice == fact:
        count_win += 1
    else:
        count_fail += 1
print(f' Not changing choice:')
print(f' wins = {count_win}')
print(f' fails = {count_fail}')
print(f' win% = {round(((count_win/repetitions) * 100), 2)}')
>>>>>>> 6eebfeef3e48450e4e3c1eafc994873f68528cbf
