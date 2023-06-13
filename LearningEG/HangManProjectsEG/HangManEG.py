import random
from EnglishWordListEG import words
import string
from HangManVisualEG import lives_visual_dict

def get_valid_word(words):
    word = random.choice(words) #Randomly chooses something from the EnglishWordListEG
    while '-' in word or ' ' in word:
        word = random.choice(words) #If there are any '-' or ' ' it will choose a new word

    return word.upper()
    
    #Next would be to keep track of which letters have guessed and which letters in the word we correctly guessed
    #Also to keep track of valid letters and what is it

def hangman():
    word = get_valid_word(words) #Now word = all the function in get_valid_word
    word_letters = set(word) #Saves all the letters in a word as a set to keep track of what have already been guessed, removes duplicates
    alphabet = set(string.ascii_uppercase) #Predertermine list of uppercase charc in the English dictionary. Only letters can be used.
    used_letters = set() #Empty so that can keep track of what the user has guessed

    lives = 7

    #Getting user input + lives
    while len(word_letters) > 0 and lives > 0: #Continues until no more letters
        print('You have', lives, 'lives left. You have used these letters: ', ' '.join(used_letters)) #' '.join(['A', 'B', 'C']) --> A B C turns list into strings seperated by what is before the .join which is ' ' so all the letters are seperated by a space
        
        #What current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper() #All the inputs in upper automatically to prevent errors
        if user_letter in alphabet - used_letters: #If its a valid charac in the alphabet that havet use yet-
            used_letters.add(user_letter) #-then will add it to used_letters set
            if user_letter in word_letters: #If what ever the user input letter is in word_letters the word_letters will remove the user_letter
                word_letters.remove(user_letter) #If user guess correctly the word_letters which keep track of all the letters in a word decreases in size(Removes the letter in the word of the list)
                print('')  

            else:
                lives -= 1 #Takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Please try again.')
        else:
            print('Invalid letter. Please try again')
# would only gets here when len(word_letters) == 0 or when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died, sorry. The word was:', word)
    else:
        print('You gussed the word:', word, '!!')

if __name__ == '__main__':
    hangman()