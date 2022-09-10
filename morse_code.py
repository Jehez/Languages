# Morse code

# A common cipher, this program aims to implement it
# Only letters and numbers will be converted
# A period '.' will represent a dot, and a hypher '-' a dash
# a single dash represents break in between letters
# a triple dash represents break in between words

# Both functions work the same way
# a pointer moves through an array and stops when the value macthes the desired value
# the value returned is from the opposite array(same pointer)


normal = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
morse = ['.-','-...','-.-.','-..','.','..-.','--.','....','..','.---','-.-','.-..','--','-.','---','.--.','--.-','.-.','...','-','..-','...-','.--','-..-','-.--','--..','.----','..---','...--','....-','.....','-....','--...','---..','----.','-----']


#normal to morse
def to_morse(sentence):
    new = ''
    for word in sentence.split():
        for letter in word:
            new+=morse[normal.index(letter)]
            new+=' '
        new+='   '
    return new[:-3]

#morse to normal
def to_normal(code):
    new = ''
    for word in code.split('   '):
        for letter in word.split():
            new+=normal[morse.index(letter)]
        new+=' '
    return new[:-1]