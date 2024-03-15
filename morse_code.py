# Morse code

# A common cipher, morse code was invented to communicate efficiently with electric telegraphs

# Only letters and numbers will be converted
# A period '.' will represent a dot, and a hyphen '-' a dash
# a single dash represents break in between letters
# a triple dash represents break in between words

# Both functions work the same way
# Latest implementation uses 2 hashmaps (dicts in python) so lookup is O(1)
# Number if iteration is n - length of string and each iteration is O(1)
# Time complexity is O(n)
# A new string also has to be stored so space complexity is also O(n)

normal_to_morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
morse_to_normal = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}


#normal to morse
def to_morse(sentence):
    converted = '' # initialize empty string to store the result
    for word in sentence.split(): # words are separated by single spaces
        for letter in word:
            converted+=normal_to_morse[letter] + ' ' # for each letter in the word, the appropriate morse is added long with a single space to distinguish between letters
        converted+='   ' # for each word, 3 spaces are added in between to distinguish that a word has ended
    return converted[:-3] # for the last word, 3 spaces will be added that are not necessary so they can be removed

#morse to normal
def to_normal(code):
    converted = '' # initialize empty string to store the result
    for word in code.split('   '): # words in morse are separated by 3 spaces
        for single_code in word.split(): # letters in morse are separated by a single space
            converted+=morse_to_normal[single_code] # for each indiividual morse code, the corresponding letter is added to new string
        converted+=' ' # add single space to separate words
    return converted[:-1] # for the last word, a single space will be added that is not necessary so it can be removed
