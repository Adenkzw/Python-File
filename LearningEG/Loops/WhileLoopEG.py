#1
secret_word = "wei en"
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = input('Enter Guess: ').lower() #when using .lower() or .upper() must have () at the back  
    guess_count += 1
    if guess == secret_word:
        print('Correct')
        break
else:
    print('Wrong')

#2 long winded
secret_word = 'wei en'
guess = ''
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input('Enter Guess: ')
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
        print('Out of guesses, You Lose')
else:
        print('You Win')

#3
secret_num = 2
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Enter guess: "))
    guess_count += 1
    if guess == secret_num:
        print('You Win')
        break
else:
    print('You Lose')
