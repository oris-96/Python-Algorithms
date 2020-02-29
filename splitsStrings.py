"""
    Complete the solution so that it splits the string into pairs of two characters.
    If the string contains an odd number of characters then it should replace the missing
    second character of the final pair with an underscore ('_').

    Examples:

    solution('abc') // should return ['ab', 'c_']
    solution('abcdef') // should return ['ab', 'cd', 'ef']

    Steps:
    1: iterate through the string 
    2: find individual pairs through the string by comparing if its even or not
    3: if even return the pairs in a list 
    4: if odd return pairs in a list and replace the last index with an underscore
    5:
"""

str = 'adef' # returns ['ac', 'vd', 'ef', 'as', 'f_'] - vdefasf

def splitString(input):
    
    # If the input length is 0 return an empty list
    if len(input) == 0:
        return []

    # return list of string pairs
    paired_strings = []
    # iterate through the range of the input length
    for i in range(len(input)):
        if i % 2 == 0:
            paired_strings.append(input[i]+input[i+1])
        #else:
    return paired_strings

print(splitString(str))


"""
idList = [ 2, 4, 6, 1, 3]
        2
       / \
      1   4
     /\   /\
    0  0 3  6
"""