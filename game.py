import string
from setting import Setting
from wordbank import WordBank
from wordleword import WordleWord
from wordleplayer import WordlePlayer
import time 
import random

#Snapshot 1 2/14/22 - We worked on the wordleword and wordleplayer classes. Our wordleword class is finished and after testing it we saw that it worked well. We've started to use it in our markguess function too. Our wordleplayer class is almost done and just needs the guessdistribution to be implemented, and then we will debug and test it. 
#Snapshot 2 2/28/22 - Over break we worked on the markguess and finished up the wordleplayer class. Our markguess seems to be working after multiple tests and we were able to implement the guess distribution part of wordleplayer. Now we are working on playround and playwordle.
#Snapshot 3 3/2/22 - We finished and tested play round and it works well, but we have to implement it with playwordle which isn't completely done, so we are still learning how to put everything together in playwordle. Once we finish that function, our game should work with no extra features implemented, which we will do next.
#Snapshot 4 3/7/22 - We are completely done with all baseline functionality and have tested that and we implemented extra features, which we are ok with submitting as is right now, but if time allows we can add more. We think we are pretty much done though because we have added all that we wanted to. We added a timer, input validation, instructions, and a welcoming message.
#FINAL SUBMISSION 3/10/22
# # #======
# markGuess - will "mark" the guess and the alphabet according to the word
#   word - String of word to be guessed
#   guess - WordleWord that have been guessed
#   alphabet - WordleWord of the letters a-z that have been marked
#======
def markGuess(word, guess, alphabet):
    correct = [] 
    misplaced = []
    ac = []
    am = []
    letterslist = []
    #puts all the letters from the word into a list
    for i in range(len(word)):
        letterslist.append(word[i])
        
    #to retain what was correct from the alphabet already
    for i in range(26):
        if alphabet.isCorrect(i):
            ac.append(alphabet.charAt(i))

    #marks them green if correct
    for i in range(len(word)):
        if guess.charAt(i) == word[i]:
            guess.setCorrect(i)
            correct.append(guess.charAt(i))
    #finds the yellow 
    #if the character from word is anywhere in guess and it is not green in guess, mark it yellow / leave everything else gray
    for i in range(len(word)):
        if (guess.charAt(i) in letterslist) and (guess.isCorrect(i) == False) and (guess.charAt(i) not in correct):
            guess.setMisplaced(i)
            letterslist.remove(guess.charAt(i))

    #alphabet
    for i in range(len(guess.getWord())):
        for j in range(26):
            if guess.charAt(i) == alphabet.charAt(j):
                if guess.isMisplaced(i) == True and (guess.charAt(i) not in ac):
                    alphabet.setMisplaced(j)
                    am.append(alphabet.charAt(j))
                elif guess.isCorrect(i) == True:
                    alphabet.setCorrect(j)
                    ac.append(alphabet.charAt(j))
                elif (alphabet.charAt(j) not in ac) and (alphabet.charAt(j) not in am):
                    alphabet.setNotUsed(j)

def print_past_guesses(lst):
    for i in range(len(lst)):
        print(str(i+1) + ": " + str(lst[i]))

#==================================================
# playRound(players, words, all_words, settings)
# Plays one round of Wordle. 
# Returns nothing, but modifies the player statistics at end of round
#   players - List of WordlePlayers
#   words - Wordbank of the common words to select from
#   all_words - Wordbank of the legal words to guess
#   settings - Settings of game
#==================================================
def playRound(players, words, all_words, settings):
    #establishes the player, the tries counter, gets the random word and makes it a wordle word as well as the alphabet
    player = players[0]
    tries = 0
    game_notover = True
    maxg = player.max
    word = words.getRandom()
    wordstorage = []
    alpha = WordleWord("abcdefghijklmnopqrstuvwxyz")

    start = time.time()
    #while loop that plays until the word is guessed or not guessed
    while game_notover: 

        unlegal = True
        while unlegal:
            userguess = input("You have " + str(maxg-tries) + " tries left. Enter your valid 5-letter guess: ")
            if all_words.contains(userguess) == False or len(userguess) !=5:
                print("Invalid guess!")
            else:
                unlegal = False

        guess = WordleWord(userguess)
        markGuess(word, guess, alpha)
        wordstorage.append(guess)
        tries += 1
        print_past_guesses(wordstorage)
        print(alpha)
        print()

        #if blocks to check if game is over
        if (userguess == word):
            print("You got the word!")
            stop = time.time()
            timer = round(stop-start, 2)
            print("It took you " + str(timer) + " seconds to guess the word!")# tells you how long it took you to guess your word!
            player.updateStats(True, tries)
            game_notover = False

        elif tries >= maxg:
            print("You ran out of tries :(. The word was " + word+ ". Game over! ")
            game_notover = False
            player.updateStats(False, tries)

        #function updates the stats and ends the while loop when the player is done

def instructions(): #this function is used to store the instruction manual, which the player can choose to view at the start of the game
    print()
    print("Wordle Instruction Manual:")
    print("In this game, Wordle will randomly select a 5 letter word from our wordbank")
    print("You as a player have 6 tries to guess the correct word")
    print("If you have the right letter in the correct spot, it will show up as green!")
    print("If you guess a word that has a common letter with the answer BUT it's in the wrong spot, it will show up as yellow")
    print("Any letter guessed that is not in the word will be marked as grey on the alphabet that keeps track of which letters you've guessed")
    print("Remember you can only guess valid 5 letter words! ")
    print("Most importantly, have fun!")
    print()

def welcome(): # this function prints out our welcoming logo
    lst = ['red', 'yellow','green', 'blue',"purple","pink"]
    str = "WELCOME TO THE GAME OF WORDLE BY RAINA AND ALISON!!!!! "
    hello = WordleWord(str)
    j=0
    for i in range(len(str)):
        if hello.charAt(i) not in " ":
            hello.setColorAt(i,lst[j])
            if j >=5:
                j = 0
            else:
                j+=1
    print(hello)


def playWordle():
    #welcomes you to the game
    print()
    welcome()

    #input validation for the instruction manual
    i = True
    while i:
        instruction = input("Would you like to open the instruction manual (y/n):")
        if instruction == "y":
            instructions()
            i = False
        elif instruction == "n":
            print("Ok!") 
            print()
            i = False
        else:
            print("error please input correct letter (y/n)")

    #creates the player so we can store their stats and welcomes them
    players = []
    name = input("Enter your name: ")
    player = WordlePlayer(name, 6 )
    players.append(player)
    print("Welcome", player.getName() + "!")
    print("OK, let's play Wordle!!")   

    #settings and wordbanks being initialized
    all_words = WordBank("words_alpha.txt")
    words = WordBank("common5letter.txt")
    settings = Setting()
    settings.setSetting('maxguess', 6)
    settings.setSetting('numplayers', 1)
    settings.setSetting('difficulty', 'normal')

    # while loop to play the game until the user would like to stop there is also input validation again for y and n
    keep_playing = True
    while keep_playing:
        print()
        playRound(players, words, all_words, settings)
 
        invalid = True
        while invalid:
            playAgain = input("Did you want to play again? (y/n):")
            if playAgain != "y" and playAgain != "n":
                print("Error, please input y or n")
            else:
                invalid = False
        
        #if you want to play again,it will keep going and continue to record your stats, otherwise it stop the game and displays your statistics
        if playAgain == "n":
                print("Bye! It was good playing Wordle with you!\n")
                player.displayStats()
                keep_playing = False
        elif playAgain == "y":
            print("Ok! Let's play again! ")


def main():
    playWordle()

if __name__ == "__main__":
    main()