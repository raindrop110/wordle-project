#===========================================================================
# class FancyWord
# Description: a colored word - each letter has a color attribute
#
# Methods
#    updateStats(won, tries) - 'won' - True if guessed word correctly
#                            - 'tries' - number of tries it took to guess word
#                            - This is called at the end of each game to update
#                              the game stats for this player
#    winPercentage() - returns % of how many games were won over all time
#    gamesPlayed() - returns the number of games played over all time 
#    currentStreak() - returns the current win streak; it will return 0 if
#                      the last game was lost
#    maxStreak() - returns the longest winning streak
#    displayStats() - prints out nice display of all the Wordle player stats
#    
#    Games Played: 3
#    Win %: 100.00
#    Current Streak: 3
#    Max Streak: 3
#    Guess Distribution
#      1: ########### 1
#      2: # 0                        <-- min bar length is 1
#      3: # 0
#      4: ##################### 2    <-- max bar length is 21
#      5: # 0
#      6: # 0
#=============
from player import Player

class WordlePlayer(Player): #wordle player class with the required functions that help keep track of stats and display stats

    def __init__(self, name, maxTry):
        super().__init__(name)
        self.max = maxTry
        self.games = 0
        self.gameswon = 0
        self.winstreak = 0
        self.streaksList = []
        self.guessDistribution = [0]*(maxTry + 1)

    def updateStats(self, won, tries):
        if won is True:
            self.guessDistribution[tries] += won
            self.gameswon = self.gameswon + 1
            self.games = self.games + 1
            self.winstreak = self.winstreak + 1
        elif won is False:
            self.games = self.games + 1
            self.streaksList.append(self.winstreak)
            self.winstreak = 0 
        
    def winPercentage(self):
        winPercent = ( self.gameswon / self.games ) * 100
        return winPercent

    def gamesPlayed(self):
        return self.games

    def currentStreak(self):
        return self.winstreak

    def maxStreak(self):
        if len(self.streaksList) == 0:
            return self.winstreak
        elif self.winstreak > max(self.streaksList):
            return self.winstreak
        else:
            maxStreak = max(self.streaksList)
            return maxStreak
        
    def maxTry(self):
        return self.max

    def displayStats(self):
        print("Games Played: {}".format(self.gamesPlayed()))
        print("Win %: {}%".format(round(self.winPercentage())))
        print("Current Streak: {}".format(self.currentStreak()))
        print("Max Streak: {}".format(self.maxStreak()))
        print("Guess Distribution")
        for i in range(1, self.max + 1):
            print("  {}: {} {}".format(i, "#" + "#"*(20*self.guessDistribution[i]//max(1, max(self.guessDistribution))), self.guessDistribution[i]))

