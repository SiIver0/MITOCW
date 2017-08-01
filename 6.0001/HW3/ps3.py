# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Noah Yoshida 
# Collaborators : ego 
# Time spent    : too little or mayne not enough 

# Need to make all of the letters appear on the same line 
	# FIXED - use a comma after print statement!
# Need to make sure you only get one wild card per hand 
# Need to fix how the wildcards interact with the program 
# Why are we getting errors when we use wild cards? 
# Quitting with '!!' produces an error. 
# Substitutting for a new letter also breaks it :( so sad 

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*':0
}



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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word_len = len(word)
    first_component = 0    
    word = word.lower()
    for letter in word:
    	for key_letter in SCRABBLE_LETTER_VALUES:
    		if key_letter == letter:
    			first_component = first_component + SCRABBLE_LETTER_VALUES[key_letter]
    second_component = (7 * word_len) - 3 * ( n - word_len)
    if second_component >= 1:
    	score = first_component * second_component
    else:
    	score = first_component
    return score 

    # if the second component is less than or equal to one, then it defauls to one. Since one 
    # times the score is just the score, I return the score. 


    

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    print 'Your hand:'
    for letter in hand.keys():
        for j in range(hand[letter]): # this prints out the letter based on how many times it is repeated in the hand,
        							  # or better said, what the value is at that letter key. 
             print(letter),
             
    print ' '                              # print an empty line

#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = int(math.ceil(n / 3)) - 1 

    print num_vowels
    for i in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    hand['*'] = hand.get('*', 0) + 1 
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = {}
    new_hand = hand.copy()
    word = word.lower()
    for letter in word:
    	for key_letter in new_hand: 
    		if key_letter == letter and new_hand.get(key_letter,0) >= 1: 
    			new_hand[key_letter] = new_hand.get(key_letter,0) - 1
    return new_hand 


  




      # TO DO... Remove this line when you implement this function

#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    valid = False 
    copy = hand.copy()
    word = word.lower()
    word_l = list(word)
    new_words = []
    if word.find('*') == -1:
		for sample_word in word_list: 
			if sample_word == word:
				valid = True 
    else:
    	for vowel_i in range(len(VOWELS)):
    		for letter_i in range(len(word)):
    			if word[letter_i] == '*':
    				word_l = list(word)
    				word_l[letter_i] = VOWELS[vowel_i]
    				new_words.append(''.join(word_l))
    	for new_word in new_words:
    		for sample_word in word_list:
    			if new_word == sample_word:
    				valid = True

      				# for sample_word in word_list: 
    				# 	if sample_word == ''.join(word_l):
    				#  		valid = True 
    for letter in word: 
    	if letter not in hand.keys(): 
    		valid = False 
    		break 
    		

    	for key_letter in hand:
    		if letter == key_letter:
    			copy[key_letter] += -1  
    		if copy[key_letter] < 0:
    			valid = False 
    			break 
    return valid 



      # TO DO... Remove this line when you implement this function

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer

    """
    hand_len = 0
    for value in hand.values():
    	hand_len += value 

    return hand_len   # TO DO... Remove this line when you implement this function

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    
    # BEGIN PSEUDOCODE <-- Remove this comment when you implement this function
    # Keep track of the total score
    
    # As long as there are still letters left in the hand:


    ## This shit is all fucked up :( n does not update when you get an error. !! command does not work 
    ## when you are in the error portion. 

    # score = 0
    # kill = False
    # n = calculate_handlen(hand)
    # while n > 0 and not kill: 
    # 	print n
    # 	display_hand(hand)
    # 	word = raw_input('Please enter your word here: ')
    # 	if word == '!!':
    # 		kill = True 
    # 		break
    # 	elif is_valid_word(word,hand,word_list):
    # 		hand = update_hand(hand,word)
    # 		n = calculate_handlen(hand)
    # 		score += get_word_score(word, n)
    # 		print score 
    # 		print n 
    # 		if n <= 0:
    # 			break
    # 		display_hand(hand)
    # 		word = raw_input('Please enter your new word here: ')
    # 	else:
    # 		hand = update_hand(hand, word)
    # 		print score 
    # 		word = raw_input('Error, please enter new word: ')
    # print 'Your score is', score,'!'
    # return score 
    score = 0
    n = calculate_handlen(hand)
    while n > 0:
    	word = raw_input('Word here: ')
    	if word == '!!':
    		break
    	else:
    		if is_valid_word(word, hand, word_list):
    			
    			score += get_word_score(word,n)
    			print score
    			print 'word is valid!'
    			print ' '
    			print n
    		else:
    			print 'bad word fam'
    			print n
    		hand = update_hand(hand, word)
    		n = calculate_handlen(hand)
    		display_hand(hand)
    print 'your score is ',score 
    return score 
    print 'yay'
    print n
	# score = 0 
	# n = calculate_handlen(hand)
	# while n > 0: 
	# 	display_hand(hand)
	# 	word = raw_input('Word here: ')
	# 	if word == '!!':
	# 		break
	# print 'yay'
	# return n

    
        # Display the hand
        
        # Ask user for input
        
        # If the input is two exclamation points:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not two exclamation points):

            # If the word is valid:

                # Tell the user how many points the word earned,
                # and the updated total score

            # Otherwise (the word is not valid):
                # Reject invalid word (print a message)
                
            # update the user's hand by removing the letters of their inputted word
            

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score

    # Return the total score as result of function



#
# Problem #6: Playing a game
# 


#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    
    '''
    - Makes a copy dictionary 
    - Adds all the letters in the alphabet together, randomely choses one 
    - Iterates over the letters in the dictionary 
    - If it finds a letter in the dictionary that is the same as the one you provided, 
    	- stores the value of that (the number of letters in your hand)
    	- deletes that entry from the dictionary 
    	- appends to the dictionary a new entry with the same value, and with the key letter that 
    	we selected randomley earlier
    '''

    copy = hand.copy()
    letters = VOWELS + CONSONANTS
    x = random.choice(letters)
    for i in copy.keys():
    	if letter == i:
    		val = copy[i]
    		del copy[i]
    		copy[x]=val
    return copy
    # for i in range(len(copy.keys())): 
    # 	if letter == copy(i):
    # 		val = copy.value(i)
    # 		del copy[i]
    # 		copy.append(x,val)
    # 		break 
    # return copy   # TO DO... Remove this line when you implement this function
       
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    n_hands = input('Enter total number of hands: ')
    series_score = 0 
    hand = deal_hand(HAND_SIZE)
    score = 0
    while n_hands > 0:
    	good = False 

    	
    	display_hand(hand)
    	sub = raw_input('Would you like to substitute a letter? Y/n? ')
    	while not good: 
    		if sub == 'Y':
    			letter = raw_input('Which letter would you like to replace? ')
    			hand = substitute_hand(hand, letter)
    			good = True 
    		elif sub =='n':
    			score = play_hand(hand, word_list)
    			
    			series_score = series_score + score 
    			n_hands += -1 
    			good = True  
    			hand = deal_hand(HAND_SIZE)
    		else:
    			sub = raw_input('Error, please enter Y or n:')
    			good = False 
    print 'Your score for the series was:',series_score
    print '--'





     # TO DO... Remove this line when you implement this function
    


#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
