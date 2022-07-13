import random

try:
    with open('stuff/words.txt') as f:
        correct_word = random.choice(f.readlines())
except:
    with open('words.txt') as f:
        correct_word = random.choice(f.readlines())


right_guesses = ['_' for x in range(len(correct_word)-1)]
wrong_guesses = []

print(f'''
Welcome to Hangman. The word you are looking for has {len(correct_word)} characters.''')

def get_char():
    while True:
        guess = input('\nInput your guess, 1 char: ')
        if len(guess) == 1:
            return guess

def print_wrong(n):
    if n == 1:
        print(r''' 
       
        _________________
        |                |
        |                |
        |                |
        |                O
        |
        |
        |
        |
       / \
      /   \
     /     \
    /       \
        
        ''')

    if n == 2:
        print(r''' 
       
        _________________
        |                |
        |                |
        |                |
        |                O
        |                |
        |               /|
        |                
        |               
       / \
      /   \
     /     \
    /       \
       
        ''')
    
    if n == 3:
        print(r''' 
       
        _________________
        |                |
        |                |
        |                |
        |                O
        |                |
        |               /|\
        |                
        |               
       / \
      /   \
     /     \
    /       \
        
        ''')

    if n == 4:
        print(r''' 
       
        _________________
        |                |
        |                |
        |                |
        |                O
        |                |
        |               /|\
        |                |
        |               / 
       / \
      /   \
     /     \
    /       \
        
        ''')

    if n == 5:
        print(r''' 
       
        _________________
        |                |
        |                |
        |                |
        |                O
        |                |
        |               /|\
        |                |
        |               / \
       / \
      /   \
     /     \
    /       \
        
        ''')

def insert_correct_choice(char):
    idx = []
    for c,letter in enumerate(correct_word):
        if letter == char:
            idx.append(c)
    for i in idx:
        right_guesses[i] = char
    

while True:
    char = get_char() 
    if char in correct_word:
        insert_correct_choice(char)
        print('''
        Correct!
         ''')
        if ''.join(right_guesses) == correct_word[:-1]:
            print('You won the game!')
            break
        print(right_guesses)
    else:
        if char in wrong_guesses:
            print('You have already made this guess!')
        else:
            print('Wrong guess!')
            wrong_guesses.append(char)
            print_wrong(len(wrong_guesses))
        if len(wrong_guesses) == 7:
            print('You lost the game')
            print(f'The word was {correct_word}')
            break
        print(f'''Right guesses: {right_guesses}
        ''')
        print(f'''Wrong guesses: {wrong_guesses}
        ''')


        

