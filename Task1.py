'''
DESCRIPTION:
In this kata, your job is to create a class Dictionary which you can add words to and their entries.
'''


class Dictionary:
    def __init__(self):
        self.entries = {}

    def newentry(self, word, definition):
        self.entries[word] = definition

    def look(self, word):
        return self.entries.get(word, "Can't find entry for {}".format(word))
