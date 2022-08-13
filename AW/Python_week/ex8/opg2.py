target = int(input('Enter a number'))
n_wrong_guesses = int(input('Enter amount of wrong guesses'))

while True:
    
    guess = int(input('Input your guess'))

    n_wrong_guesses -= 1
    if guess != target:
        if n_wrong_guesses == 0:
            print('Incorrect, you have no more guesses')
            break
        if guess > target:
            print(f'Wrong answer. Your guess is too large. You have {n_wrong_guesses} left')
        else:
            print(f'Wrong answer. Your guess is too small. You have {n_wrong_guesses} left')
    else:
        print('You guessed right')
        break


    