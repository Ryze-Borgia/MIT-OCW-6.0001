# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

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
    
    result_list = []
    if len(sequence) == 1:
        result_list.append(sequence)
    else:
        sub_sequence = sequence[1:len(sequence)]    # get the sub_sequence except the first letter
        sub_list = get_permutations(sub_sequence)
        for sub_word in sub_list:
            for i in range(len(sub_word) + 1):      # possible positions is one more than the length of string
                temp_word = sub_word[0:i] + sequence[0] + sub_word[i:len(sub_word)]    # insert the first letter
                result_list.append(temp_word)
    return result_list


if __name__ == '__main__':
#   #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    print("--------------------------")
    print("test 2")
    example_input = 'sf'
    print('Input:', example_input)
    print('Expected Output:', ['sf', 'fs'])
    print('Actual Output:', get_permutations(example_input))
    print("--------------------------")
    print("test3")
    example_input = 'bust'
    print('Input:', example_input)
    print('Expected Output:', ['bust', 'ubst', 'usbt', 'ustb', 'bsut', 'sbut', 'subt', 'sutb', 'bstu', 'sbtu', 'stbu', 'stub', 'buts', 'ubts', 'utbs', 'utsb', 'btus', 'tbus', 'tubs', 'tusb', 'btsu', 'tbsu', 'tsbu', 'tsub'])
    print('Actual Output:', get_permutations(example_input))
    print("--------------------------")
