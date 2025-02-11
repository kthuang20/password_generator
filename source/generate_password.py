### import necessary packages
import random

### define a dictionary to replace letters with numbers and symbols
replacement_key = {
    'a': '@',
    'e': '3',
    'g': '9',
    'i': '1',
    'l': '!',
    'o': '0',
    's': ['5', '$'],
    ' ': ['-', '_', '']
}


### function to ask and store the user input
def input_text():
    ## ask and store the text the user wants to be converted
    text = input("Enter a text with 12+ characters that you want to passwordify: ")
    ## check that it has text has least 12 characters
    while len(text) < 12:
        text = input("Please re-enter text with at least 12 characters: ")
    return text.title()  # returns text with each word capitalized


### function to replace a character
def replace_char(char):
    ## get the replacement values for that character
    chars2replace = replacement_key[char]
    ## if multiple values can replace character
    if len(chars2replace) > 1:
        # randomly choose one to replace the character
        letter = random.choice(chars2replace)
        return letter
    ## otherwise there's only one value to replace,
    else:
        # so replace the character with that value
        return chars2replace


### function to convert to text into a password
def gen_passwords(text):
    ## convert text into a list of characters
    text_list = list(text)
    ## iterate through each character in the text
    for idx, char in enumerate(text_list):
        ## if it is not a capitalized letter,
        if not char.isupper() and char in replacement_key:
            # replace character
            text_list[idx] = replace_char(char)
    ## return the password as a string
    password = "".join(text_list)
    return password
