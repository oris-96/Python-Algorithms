# Step 1) Create a program that prints the numbers 1 to 100;
# Can be a variable or a function, anything that will print 1-100.
# Step 2) 

# Write a program that prints the numbers from 1 to 100. But for multiples of `3` print “Fizz”
# instead of the number and for the multiples of `5` print “Buzz”. For numbers which are multiples
# of both `3` and `5` print “FizzBuzz”

one_to_hundred=range(1,101)

for number in one_to_hundred:
    if number % 3 ==0 and number % 5 ==0:
        print("FizzBuzz")
    elif number % 3 ==0:
        print("fizz")
    elif number % 5 ==0:
        print("Buzz")




# You need to write a function that reverses the words
# in a given string. A word can also fit an empty string. 
# If this is not clear enough, here are some examples: reverse('Hello World') == "World Hello";
string = 'hello world'   # 'world hello'
def reverse(str):
    word_in_list = str.split(" ")
    reversed_words = word_in_list[::-1]
    print(reversed_words)
    print((" ").join(reversed_words))
reverse(string)

# Write a function that determines how often each character occurs in a given string.

# occurrences "This is an example string." => {"t":2,"h":1,"i":3,"s":3," ":4,"a":2,"n":2,"e":2,"x":1,"m":1,"p":1,"l":1,"r":1,"g":1,".":1}

### RESEARCH ###
# Python Conditional Statements
# Python Control Flow

str = "this is fun" # { 't': 1 } => { 't': 1, 'h': 1 } => { 't': 1, 'h': 1, 'i': 2 } => { 't': 1, 'h': 1, 'i': 2, 's': 2 }
def occurence(str):
    letter_counts = {}
    for letter in str:
        # if letter_counts has letter do this:
        if letter in letter_counts:
            continue
        else:
            counts=str.count(letter)
            letter_counts[letter]= counts
    return letter_counts
print(occurence(str))     

