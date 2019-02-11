#get user sentence
def get_input():
    sentence = input('Enter a sentence to convert to camel case. Include spaces, no punctuation')
    return sentence

#chop up sentence into words
def split_sentence(sentence):
    word_list = sentence.split(' ')
    return word_list

#capitalize words except for first word
def process_sentence(word_list):
    camelCase_list = (word_list[0] if word_list.index(x) == 0 else x.capitalize() for x in word_list)
    return camelCase_list

def main():
    # welcome message
    print('Welcome User')
    #get user sentence
    sentence = get_input()
    #split the sentence
    splitSentence = split_sentence(sentence)
    #process into a camel cased term
    camelCase_list = process_sentence(splitSentence)
    # print out result
    for string in camelCase_list:
        print(string, end='')

main()