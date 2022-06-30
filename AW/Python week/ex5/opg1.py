from numpy import _2Tuple


my_list = ['Marie Per', 'Jens Kurtesen', 'Kurt Ronny', 'Rune Ronny', 'Roger Tønnesen']

print(my_list[2])

print(my_list[2][0])

my_list[2] = 'Ole'

my_list[2] = 'Ole Nordmann'

my_list.append('Kurt Ronny')

my_list.insert(4,'Monty Python')

len(my_list)

my_list.remove('Ole Nordmann')

len(my_list)

my_list.index('Monty Python')

print(my_list[:3])

students_reverse = my_list[::-1]

students_reverse

students_even = my_list[::2]

students_even

students_odd = my_list[1::2]

students_odd

