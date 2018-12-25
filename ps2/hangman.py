import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    
    ret = ""
    for char in secret_word:
        if char not in letters_guessed:
            ret = ret + '_ '
        else:
            ret = ret + char
    return ret


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    
    lowercaseStr = string.ascii_lowercase
    ret = ""
    for char in lowercaseStr:
        if char not in letters_guessed:
            ret = ret + char
    return ret
    

def get_unique_num(secret_word):
    '''
    secret_word: string, the word the user is guessing    
    returns: integer, the number unique letters in the secret_word
    '''
    
    list_unique_letters = []
    for char in secret_word:
        if char not in list_unique_letters:
            list_unique_letters.append(char)
    return len(list_unique_letters)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    # Initial the variable and print the greetings 
    print("Welcome to the game Hangman!")
    
    letters_count = len(secret_word)
    guess_count_left = 6
    warning_count_left = 3
    letters_guessed = []    # list of letters guessed
    vowels = ['a', 'e', 'i', 'o', 'u']
    IsVowels = False
    
    print("I am thinking of a word that is", letters_count, "letters long");
    # just for testing
    # print(secret_word)
    print("-------------")
    
    # main loop of the game
    while (not (is_word_guessed(secret_word, letters_guessed))) and (guess_count_left > 0):
        # show the hint message
        print("you have", guess_count_left, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed)) 
        # get a letter from user
        user_input = (str)(input("Please guess a letter:"))
        # is alphabet ???
        if str.isalpha(user_input):
            # vowels or consonants ???
            if str.lower(user_input) in vowels:
                IsVowels = True
            # never guessed before
            if str.lower(user_input) not in letters_guessed:
                letters_guessed.append(str.lower(user_input))
                if str.lower(user_input) in secret_word:
                    # lose no guess if right
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed)) 
                # guess wrong
                else:
                    if IsVowels:
                        guess_count_left -= 2
                    else:
                        guess_count_left -= 1
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            # have guessed before
            else:   
                # have guessed this letter lose a warning or lose a guess when have no warning
                if warning_count_left == 0:
                    guess_count_left -= 1
                    print("Oops! You've already guessed that letters, you now have no warnings, so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                else:
                    warning_count_left -= 1
                    print("Oops! You've already guessed that letters, you now have", warning_count_left, "warnings:", get_guessed_word(secret_word, letters_guessed))
        # have guessed this letter lose a warning or lose a guess when have no warning
        else:
            if warning_count_left == 0:
                guess_count_left -= 1
                print("Oops! That is not a vaild letter. You have no warning left, so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                warning_count_left -= 1
                print("Oops! That is not a vaild letter. You have", warning_count_left, "warning left:", get_guessed_word(secret_word, letters_guessed))
        print("-------------")
        # clear the flag of Vowels
        IsVowels = False
    # exit of the game
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won")
        print("Your total score of this game is:", guess_count_left * get_unique_num(secret_word))
    else:
        print("Sorry, you ran out of guesses, The word is", secret_word)

# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # !!! strip() can only remove the whitespace in the heading and trailing 
    real_word = my_word.replace(' ', '')
    # print(real_word)
    len1 = len(real_word)
    len2 = len(other_word)
    if len1 != len2:
        return False
    else:
        for i in range(len1):
            if real_word[i] != '_' and real_word[i] != other_word[i]:
                return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    possible_word_list = []
    IsWordFind = False
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_word_list.append(word)
            IsWordFind = True
    if not IsWordFind:
        print("No match found")
    else:
        print(possible_word_list)    # may change a emethod would not print [''] but just the possible word


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # Initial the variable and print the greetings 
    print("Welcome to the game Hangman!")
    
    letters_count = len(secret_word)
    guess_count_left = 6
    warning_count_left = 3
    letters_guessed = []    # list of letters guessed
    vowels = ['a', 'e', 'i', 'o', 'u']
    IsVowels = False
    
    print("I am thinking of a word that is", letters_count, "letters long");
    # just for testing
    # print(secret_word)
    print("-------------")
    
    # main loop of the game
    while (not (is_word_guessed(secret_word, letters_guessed))) and (guess_count_left > 0):
        # show the hint message
        print("you have", guess_count_left, "guesses left")
        print("Available letters:", get_available_letters(letters_guessed)) 
        # get a letter from user
        user_input = (str)(input("Please guess a letter:"))
        # is alphabet ???
        if str.isalpha(user_input):
            # vowels or consonants ???
            if str.lower(user_input) in vowels:
                IsVowels = True
            # never guessed before
            if str.lower(user_input) not in letters_guessed:
                letters_guessed.append(str.lower(user_input))
                if str.lower(user_input) in secret_word:
                    # lose no guess if right
                    print("Good guess:", get_guessed_word(secret_word, letters_guessed)) 
                # guess wrong
                else:
                    if IsVowels:
                        guess_count_left -= 2
                    else:
                        guess_count_left -= 1
                    print("Oops! That letter is not in my word:", get_guessed_word(secret_word, letters_guessed))
            # have guessed before
            else:   
                # have guessed this letter lose a warning or lose a guess when have no warning
                if warning_count_left == 0:
                    guess_count_left -= 1
                    print("Oops! You've already guessed that letters, you now have no warnings, so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
                else:
                    warning_count_left -= 1
                    print("Oops! You've already guessed that letters, you now have", warning_count_left, "warnings:", get_guessed_word(secret_word, letters_guessed))
        # give a hint but not minus a guess
        elif user_input == '*':
            print("Possible word matches are:")
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        # have guessed this letter lose a warning or lose a guess when have no warning
        else:
            if warning_count_left == 0:
                guess_count_left -= 1
                print("Oops! That is not a vaild letter. You have no warning left, so you lose one guess:", get_guessed_word(secret_word, letters_guessed))
            else:
                warning_count_left -= 1
                print("Oops! That is not a vaild letter. You have", warning_count_left, "warning left:", get_guessed_word(secret_word, letters_guessed))
        print("-------------")
        # clear the flag of Vowels
        IsVowels = False
    # exit of the game
    if is_word_guessed(secret_word, letters_guessed):
        print("Congratulations, you won")
        print("Your total score of this game is:", guess_count_left * get_unique_num(secret_word))
    else:
        print("Sorry, you ran out of guesses, The word is", secret_word)


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
