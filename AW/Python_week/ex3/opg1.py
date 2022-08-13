

punishment_text = input('Input text')

punishment_text += '\n'

numb_of_repetition = 10

x = {punishment_text.count('that')}

print(punishment_text.replace(' NOT', '').replace('FLY', 'BOOGIE') * numb_of_repetition)

print(f'''The number of the word THAT in the original sentence is: {punishment_text.count('that')}''')
