# Piglatin

# Piglatin is a common language game to convert English to Piglatin
# the first letter is moved to the end of the word and then 'ay' is added


#normal to piglatin
def piglatin(word):
    word += word[0]     #add first letter
    word = word[1:]     #removes first letter from beginning
    return word+'ay'    #add the 'ay' and return it

#piglatin to normal
def normal(word):
    word = word[:-2]        #remove the 'ay' - the function assumes the input is always valid (in pig latin)
    word = word[-1]+word    #add the last letter at the start
    return word[:-1]        #return word without the last letter
