# Problem Set 2, hangman.py
# Name: Noah Yoshida 
# Collaborators: None 
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
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

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()
letters_guessed = []

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    correct = True 
    for letter in secret_word:
    	if letter not in letters_guessed:
    		correct = False 
    return correct 

    # Should return correct as true unless it detects that there are any letters 
    # in the secret word which are not in the letters_guessed list, then it returns 
    # false.

    
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out_string = ''
    for x in secret_word:
    	if x == '':
    		out_string = out_string + ''
    	elif x in letters_guessed:
    		out_string = out_string + x
    	else:
    		out_string = out_string + '_'
    return out_string

    '''
    Makes an empty string, adds in spaces where there are spaces in the secret word, 
    if that letter in the secret word has not been guessed, adds a '_', and if it 
    has appends that letter to the string 
    '''



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    # FILL IN YOUR CODE HERE AND DELETE "pass"
    out_string = ''
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    for letter in all_letters:
    	if letter not in letters_guessed:
    		out_string = out_string + letter 
    return out_string 

    
    

    
    

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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print '____NEW GAME_____'
    print '_________________'
    print '_________________'
    print '_____HANGMAN_____'
    print 'BY:  NOAH YOSHIDA'
    print '_________________'
    print ''
    x=0
    guesses = 6
    warnings = 3
    letters_guessed = ''
    for letter in secret_word:
    	if letter == '':
    		x += 1 


    print 'There are a total of', (len(secret_word)-x), 'letters in the secret word.'
    
    while not is_word_guessed(secret_word,letters_guessed) and guesses != 0:
    	
    	print 'You have', guesses, 'guesses.'
    	print 'You have not guessed these letters:'
    	print get_available_letters(letters_guessed)
    	print ''
    	print get_guessed_word(secret_word,letters_guessed)
    	print ''
    	y = raw_input("Please guess a letter and hit enter: ")
    	str.lower(y)
    	

    	while (not str.isalpha(y) or y in letters_guessed) and guesses is not 0:

    		warnings = warnings - 1
    		if warnings == 0:
    			print 'You are out of warnings. Subtracting one guess.'
    		else:
    			print 'You have', warnings, 'warnings left.'
    			guesses = guesses - 1 
    		if y in letters_guessed:
    			y = raw_input("Error, please input a letter you have not guessed yet: ")
    		else:
    			y = raw_input("Error, please input a letter and hit enter: ")
    	
    	letters_guessed = letters_guessed + y


    	if y not in secret_word:
    		print 'Sorry! You are wrong. Guess again!'
    		if y in 'aeiou':
    			guesses += -2
    		else:
    			guesses += -1
    	else:
    		print 'Nice guess!'


    	if is_word_guessed(secret_word,letters_guessed):
    		print 'Congrats! You won!'
    		print 'Your score is:', guesses * len(secret_word),''
    		print get_guessed_word(secret_word,letters_guessed) 


    	if guesses <= 0:
    		print 'Darn, you lose! The secret word was:'
    		print secret_word
    		print ''
    		z = raw_input('Play again? Y/n?: ')
    		if z == 'Y':
    			secret_word = choose_word(wordlist)
    			hangman(secret_word)
    			
    	


    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    z = True
    if len(my_word) != len(other_word):
    	z = False 
    else:
    	for x in range(len(my_word)):
    		if my_word[x] == '_':
    			pass 
    		elif my_word[x] != other_word[x]:
    			z = False
    return z 
    



def show_possible_matches(my_word,wordlist):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for x in wordlist:
    	if match_with_gaps(my_word,x):
    		print x

    



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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print '____NEW GAME_____'
    print '_________________'
    print '_________________'
    print 'HANGMAN w/ HINTS'
    print 'BY:  NOAH YOSHIDA'
    print '_________________'
    print ''
    x=0
    guesses = 7
    warnings = 3
    letters_guessed = ''
    for letter in secret_word:
    	if letter == '':
    		x += 1 


    print 'There are a total of', (len(secret_word)-x), 'letters in the secret word.'
    
    while not is_word_guessed(secret_word,letters_guessed) and guesses != 0:
    	
    	print 'You have', guesses, 'guesses.'
    	print 'You have not guessed these letters:'
    	print get_available_letters(letters_guessed)
    	print ''
    	word = get_guessed_word(secret_word,letters_guessed)
    	print word 
    	print ''
    	y = raw_input("Please guess a letter and hit enter: ")
    	str.lower(y)
    	if y == '*':
    		show_possible_matches(word,wordlist)
    		print ''
    		y = raw_input("Please guess a letter and hit enter: ")
    		print ''
    	

    	while (not str.isalpha(y) or y in letters_guessed) and guesses is not 0:
    		
    		if warnings == 0:
    			print 'You are out of warnings. Subtracting one guess.'
    		else:
    			warnings = warnings - 1
    			print 'You have', warnings, 'warnings left.'
    			guesses = guesses - 1 
    		if y in letters_guessed:
    			y = raw_input("Error, please input a letter you have not guessed yet: ")
    		else:
    			y = raw_input("Error, please input a letter and hit enter: ")
    	
    	letters_guessed = letters_guessed + y


    	if y not in secret_word:
    		print 'Sorry! You are wrong. Guess again!'
    		if y in 'aeiou':
    			guesses += -2
    		else:
    			guesses += -1
    	else:
    		print 'Nice guess!'


    	if is_word_guessed(secret_word,letters_guessed):
    		print 'Congrats! You won!'
    		print 'Your score is:', guesses * len(secret_word),''
    		print get_guessed_word(secret_word,letters_guessed) 


    	if guesses <= 0:
    		print 'Darn, you lose! The secret word was:'
    		print secret_word
    		print ''
    		z = raw_input('Play again? Y/n?: ')
    		if z == 'Y' or z == 'y':
    			secret_word = choose_word(wordlist)
    			hangman(secret_word)
    pass



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
