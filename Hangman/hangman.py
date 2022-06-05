'''Simple hangman game.  Guess letters to fill in the blanks of a random word.  5 incorrect guesses is a loss.'''


import random
from words import words

def get_word():
    word = words[random.randint(0, len(words))]
    while "-" in word or " " in word:
        word = words[random.randint(0, len(words))]
    return word

def get_lives_choice():
    try:
        return int(input("\nHow many lives would you like to start with? \n Please choose a number between 1 and 26: "))
    except ValueError:
        return get_lives()

def get_lives():
    choice = get_lives_choice()
    while choice > 26 or choice < 0:
        choice = get_lives_choice()
    return choice

def play_hangman():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    word = get_word().upper() # word for the game
    guessed_characters = [] # letters the user has guessed
    lives_left = get_lives() #user enters number of starting lives
    word_characters = [letter for letter in word] # list of letters in the word
    correct_guesses_removed = [letter for letter in word] # letter in word will be removed when guessed correctly.  Will be used as a win condition
    
    
    while len(correct_guesses_removed) > 0 and lives_left > 0:
        hidden_character_list = [character if character in guessed_characters else "-" for character in word_characters] # building the hidden word

        print("\nYou have " + str(lives_left) + " lives remaining\n")
        print("\nThe word is: " + "".join(hidden_character_list) + '\n')
        print("\nYou have guessed the letters: " + " ".join(guessed_characters) + '\n')
        
        user_guess = input("\nGuess a letter: ").upper()
        
        if user_guess not in alphabet:
            print("\nInvalid character.  Please guess a letter.\n")
        elif user_guess in guessed_characters:
            print("\nYou already guessed that letter.  Please try again.\n")
        else:
            if user_guess not in word_characters:
                print("\nSorry, that letter is not in the word.\n")
                guessed_characters.append(user_guess)
                
                lives_left -= 1
            else:
                print("\n" + user_guess + " is in the word!")
                guessed_characters.append(user_guess)
                while user_guess in correct_guesses_removed:
                    correct_guesses_removed.remove(user_guess)
                
    if lives_left > 0:
        print("\nYou win!!!  The word was " + "".join(word) + "!!!\n\nPlease play again!!!")    
    else:
        print("\nYou lost.  The word was " + "".join(word) + ".\n\nPlease play again!!!")






play_hangman()