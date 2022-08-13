def bart_cheat_code_while(punishment_text, numb_of_repetition=10):
    
    n = 0

    while n < numb_of_repetition:
        print(punishment_text.replace(' NOT', '').replace('FLY', 'BOOGIE'))
        n += 1
    print(f'''The number of the word THAT in the original sentence is: {punishment_text.count('that')}''')
        


punishment_text = 'det that er helt sjukt\n'

bart_cheat_code_while(punishment_text)

def bart_cheat_code_for(punishment_text, numb_of_repetition=10):
    
    for i in range(numb_of_repetition):
        print(punishment_text.replace(' NOT', '').replace('FLY', 'BOOGIE'))
    print(f'''The number of the word THAT in the original sentence is: {punishment_text.count('that')}''')
        


punishment_text = 'det that er helt sjukt\n'

bart_cheat_code_for(punishment_text)