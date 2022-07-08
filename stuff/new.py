from collections import Counter
def anagrams(word, words):
    bs = []
    x = Counter(word)
    for w in words:
        c = Counter(w)
        status = True
        for letter in w:
            if c[letter] != x[letter]:
                status = False
        if status == True:
            bs.append(w)
    return bs

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
