# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    # print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    # print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'


def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''



    permutations = []


    if len(sequence) != 1: 
        add_letter = sequence[0]
        x = len(sequence)
        new_sequence = sequence[1:x]
        permutations = permutations + get_permutations(new_sequence)
        new_permutations = []
        for combo in permutations: 
            for letter_index in range(len(combo)+1):
                new_combo = ''
                prior_letters = combo[0:letter_index]
                after_letters = combo[letter_index:len(combo)+1]
                new_combo = prior_letters + add_letter + after_letters
                new_permutations.append(new_combo)
        return new_permutations        
    else:
        derp = ['']
        derp[0] = sequence

        return derp



class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words('words.txt')   

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        shift_dict = {}
        vowels = 'aeiou'
        vowels_upper = vowels.upper()
        upper_perm = vowels_permutation.upper()
        consonants = 'bcdfghjklmnpqrstvwxyz'
        consonants_upper = 'BCDFGHJKLMNPQRSTVWXYZ'

        for letter_index in range(len(vowels)):
            shift_dict[vowels[letter_index]] = vowels_permutation[letter_index]

        for letter in range(len(vowels_upper)):
            shift_dict[vowels_upper[letter]] = upper_perm[letter]

        for letter in consonants:
            shift_dict[letter] = letter

        for letter in consonants_upper:
            shift_dict[letter] = letter 

       



        


        return shift_dict




    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        message = ' '
        
        original = self.get_message_text()

        keys = transpose_dict.keys()

        for letter in original:
            if not letter.isalpha():
                message = message + letter
            else:
                for key in keys:
                    if letter == key:
                        message = message + transpose_dict[key]
        return message 
              
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        
        self.message_text = text
        self.valid_words = load_words('words.txt')



    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        # SMH I need to make a function that gives me all the vowel permutations fml 







        word_list = self.valid_words
        q = 0 
        y = 0 
        message = ''
        permutations = get_permutations('aeiou')
        for perm in permutations:
            y = 0 
            original_message = SubMessage(self.message_text)
            enc_dict = original_message.build_transpose_dict(perm)
            try_message = original_message.apply_transpose(enc_dict)
            for word in try_message.split():
                if is_word(word_list, word):
                    y += 1 
                if y > q:
                    q = y 
                    optimal_permutation = perm
                    message = try_message


        return message

        # for shift in shifts:
        #     print shift
        #     y = 0 
        #     decript_shift = 26 - shift 
        #     z = x.apply_shift(shift)
        #     print z
        #     for word in z.split():
        #         if is_word(word_list, word):
        #             y = y + 1
        #             print z
        #     if y > q:
        #         q = y 
        #         optimal_shift = decript_shift
        #         message = z
        #         print message
        #         print optimal_shift
        # return_val = []
        # return_val.append(message)
        # return_val.append(optimal_shift)
        # return return_val
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
