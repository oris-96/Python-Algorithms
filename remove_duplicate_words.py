"""
    Task:
    Remove duplicate words from the given string.

    Example:
    'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

    returns => 'alpha beta gamma delta'
"""

"""
    Steps:
    1) split the string based on " " 
    2) iterate over the splitted list of strings
    3) check if the word is more than one
    4) return the word 
    5) join the words together 
"""

sampleStr = 'alpha beta gamma alpha beta gamma xeta beta beta' # 'alpha beta gamma xeta'

def removeDuplicateStrings(str):
    output = [] # returned list of unique strings
    list_of_strings= str.split(" ")
    for word in (list_of_strings):
        if word in output:
            continue
        output.append(word)
    return ",".join(output)

print(removeDuplicateStrings(sampleStr))
