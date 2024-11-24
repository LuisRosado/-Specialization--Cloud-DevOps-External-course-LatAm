'''
DESCRIPTION:
Complete the function that takes an array of words.
You must concatenate the n th letter from each word to construct a new word which should be returned as a string, where n is the position of the
word in the list.
'''

# La función recorre cada palabra en la lista y concatena la n-ésima letra de cada palabra (donde n es la posición de la palabra en la lista) para construir una nueva palabra.
def concatenate_nth_letters(words):
    result = ""
    for i, word in enumerate(words):
        if i < len(word):
            if word[i] == "":
                result += word[i+1]
            else:
                result += word[i]
    return result
