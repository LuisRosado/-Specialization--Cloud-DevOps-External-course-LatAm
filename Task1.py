'''
DESCRIPTION:
In this kata, your job is to create a class Dictionary which you can add words to and their entries.
'''

# La clase Dictionary permite agregar nuevas entradas de palabras con sus definiciones y buscar definiciones de palabras. Si la palabra no se encuentra, devuelve un mensaje indicando que no se encontró la entrada.
class Dictionary:
    def __init__(self):
        self.entries = {}

    def newentry(self, word, definition):
        self.entries[word] = definition

    def look(self, word):
        return self.entries.get(word, "Can't find entry for {}".format(word))
