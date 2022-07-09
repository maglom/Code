import random


with open('stuff\words.txt') as f:
    correct_word = random.choice(f.readlines())
print(correct_word)

right_guesses = ['_' for x in range(len(correct_word))]
wrong_guesses = []

print(f'Welcome to Hangman. The word you are looking for has {len(correct_word)} characters.')

def get_char():
    while True:
        guess = input('Input your guess, 1 char: ')
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

while True:
    char = get_char() 
    if char in correct_word:
        right_guesses[correct_word.index(char)] = char
        print('Correct! ')
        if right_guesses == correct_word:
            print('You won the game!')
            break
        print(right_guesses)
    else:
        print('Wrong guess!')
        wrong_guesses.append(char)
        print_wrong(len(wrong_guesses))
        if len(wrong_guesses) == 5:
            print('You lost the game')
            break
        print(f'Right guesses: {right_guesses}')
        print(f'Wrong guesses: {wrong_guesses}')


        

