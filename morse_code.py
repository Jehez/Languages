# Morse code

# A common cipher, this program aims to implement it
# Only letters and numbers will be converted
# A period '.' will represent a dot, and a hyphen '-' a dash
# a single dash represents break in between letters
# a triple dash represents break in between words

# Both functions work the same way
# Previously, an array and pointer was used but worked in O(n^2) - 'n' because of the for loop and one 'n' because of the linear search time
# Latest implementation uses 2 hashmaps (dicts in python) so lookup is O(1) and total time is O(n)


normal_hm = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}
morse_hm = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'}


#normal to morse
def to_morse(sentence):
    new = ''
    for word in sentence.split():
        for letter in word:
            new+=normal_hm[letter]
            new+=' '
        new+='   '
    return new[:-3]

#morse to normal
def to_normal(code):
    new = ''
    for word in code.split('   '):
        for single_code in word.split():
            new+=morse_hm[single_code]
        new+=' '
    return new[:-1]
