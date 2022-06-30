def bart_cheat_code(punishment_text, numb_of_repetition=10):
    
    print(punishment_text.replace(' NOT', '').replace('FLY', 'BOOGIE') * numb_of_repetition)

    print(f'''The number of the word THAT in the original sentence is: {punishment_text.count('that')}''')

punishment_text = 'det that er helt sjukt\n'
    
numb_of_repetition = 100

bart_cheat_code(punishment_text)