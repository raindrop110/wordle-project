#===========================================================================
# Description: WordleWord(word)
# Inherits from the FancyWord class and adds methods for the Wordle game
#
# Methods
#    isCorrect(pos) - boolean - return True if character at pos is correct
#    isMisplaced(pos) - boolean - return True if character at pos is misplaced
#    isNotUsed(pos) - boolean - return True if character at pos is not in word
#    setCorrect(pos) - integer - set character are pos correct and colors accordingly
#    setMisplaced(pos) - integer - set character are pos misplaced and colors accordingly
#    setNotUsed(pos) - integer - set character are pos misplaced and colors accordingly
#===========================================================================
from tkinter import W
from fancyword import FancyWord

#wordle word class with methods to set green, gray, and yellow, and we also wrote some new colors in here that the word could have, purple and pink
class WordleWord(FancyWord):
    def __init__(self, word):
        super().__init__(word)

    def __str__(self):
        formattedWord = ""
        for i in range(len(self.word)):
            if self.color[i] == 'green':
                # bold green
                formattedWord += u'\u001b[1m\u001b[38;5;34m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == 'yellow':
                # bold yellow
                formattedWord += u'\u001b[1m\u001b[38;5;214m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == 'red':
                # bold red
                formattedWord += u'\u001b[1m\u001b[38;5;196m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == 'blue':
                # bold blue
                formattedWord += u'\u001b[1m\u001b[38;5;20m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == 'gray':
                # light gray
                formattedWord += u'\u001b[38;5;250m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == "pink":
                #pink
                formattedWord +=u'\u001b[1m\u001b[38;5;200m{}\u001b[0m'.format(self.word[i])
            elif self.color[i] == "purple":
                #purple
                formattedWord +=u'\u001b[1m\u001b[38;5;140m{}\u001b[0m'.format(self.word[i])
            else:
                formattedWord += self.word[i]

        return formattedWord

    def isCorrect(self,pos):
        if self.colorAt(pos) == "green":
            return True
        return False
         
    def isMisplaced(self,pos):
        if self.colorAt(pos) == "yellow":
            return True
        return False

    def isNotUsed(self,pos):
        if self.colorAt( pos) == "gray":
            return True
        return False

    def setCorrect(self,pos):
        self.setColorAt(pos, 'green')

    def setMisplaced(self,pos):
        self.setColorAt(pos, 'yellow')

    def setNotUsed(self, pos):
        self.setColorAt(pos, 'gray')

