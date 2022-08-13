import requests

URL = 'https://random-word-api.herokuapp.com/word'
response = requests.get(URL)
correct_word = response.text


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
        |                |
        |                
        |               
       / \
      /   \
     /     \
    /       \
       
        ''')

    if n == 3:
        print(r''' 
<<<<<<< HEAD
=======
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> windows
        
>>>>>>> 6c0dbf3035c433bf69076122c38f8e34b9a694b9
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
<<<<<<< HEAD

    if n == 4:
        print(r'''    
=======
<<<<<<< HEAD
=======
       
>>>>>>> 6c0dbf3035c433bf69076122c38f8e34b9a694b9
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
<<<<<<< HEAD
=======
>>>>>>> 7f697ec4332dbfd30665455ce8aaf6b77e6f50dc
=======
>>>>>>> windows
>>>>>>> 6c0dbf3035c433bf69076122c38f8e34b9a694b9

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
        |               / 
       / \
      /   \
     /     \
    /       \
        
        ''')

    if n == 6:
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
    for c, letter in enumerate(correct_word):
        if letter == char:
            idx.append(c)
    for i in idx:
        right_guesses[i] = char


def game(correct_word, right_guesses, wrong_guesses, get_char, print_wrong, insert_correct_choice):
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
            print(
                f'Right guesses: {right_guesses}\n \nWrong guesses: {wrong_guesses}')
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


game(correct_word, right_guesses, wrong_guesses,
     get_char, print_wrong, insert_correct_choice)
