# Problem Set 4A
# Name: Noah Yoshida 
# Collaborators: 
# Time Spent: A few hours 

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
    

    # if len(sequence) == 1:
    #     for i in range(len(permutaions)):
    #         permutations[i] = sequence + permutaions[i]

    #     permutations = sequence
    #     return permutations
    
    # else: 
    #     x = len(sequence)
    #     get_permutations(sequence[0:x-1]) 
        









if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    x = get_permutations('abc')
    print x
    print len(x) #delete this line and replace with your code here

