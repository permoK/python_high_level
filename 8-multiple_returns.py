#this functions returns a tuple with the length of a string and its first character
def multiple_returns(sentence):

    #find the length of the sentence
    length = len(sentence)

    #get the first character of the sentence
    first_character = sentence[0]

    #condition to check whether there is a sentence and returns none when there is no sentence
    if length == 0:
        first_character = None

    #else return the length and the first character of the sentence
    print("Length: {:d} - First character: {}".format(length, first_character ))

#sample sentence
sentence = "At school, I learnt C!"

#calling the function
multiple_returns(sentence)