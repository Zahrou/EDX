from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
hand = dealHand(n)
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    bestWord = None
    MaxScore = 0 
    for word in wordList:                         # For each word in the wordList
                                         # Create a new variable to store the maximum score seen so far (initially 0)
         
             # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):     # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
                 
            score = getWordScore(word, n)         # Find out how much making that word is worth

            if score > MaxScore:                  # If the score for that word is higher than your best score

                MaxScore = score                  # Update your best score, and best word accordingly
                bestWord = word


    return bestWord                               # return the best word you found.

#print(compChooseWord(hand, loadWords(), n))
#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    Total_score = 0
    while displayHand(hand) != '':
        
        print('current hand: %s' % displayHand(hand))
        word = compChooseWord(hand, wordList, n)
        if word == None:
            break
        else:
            score = getWordScore(word, n)
            Total_score += score
            print("%s earned %d points. Total: %d" % (word, score, Total_score))
            hand = updateHand(hand, word)

    if displayHand(hand) == '':
        print("Run out of letters. Total score: %d points." % Total_score)
    else:
        print("Total score: %d points." % Total_score)  # Game is over (user entered a '.' or ran out of letters), so tell user the total score
 


     
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    numN = 0
    while True:
        UserInput = input("Enter n to deal a new hand, r to play the last hand, or e to end: ")
        if UserInput not in "nre":
            print('Invalid command')

        #print("\n")
        if UserInput == 'n':
            numN += 1
            
        if UserInput == 'r' and numN == 0:
            
            print('You have not played a hand yet. Please play a new hand first!')

        else:
            if UserInput == 'n':
                while True:
                    Input = input('Enter u to have yourself play, c to have the computer play: ')
                    if Input not in "cu":
                        print('invalid input')
                    elif Input == 'u':
                        hand1 = dealHand(n)
                        playHand(hand1, wordList, n)
                        break
                    elif Input == 'c':
                        hand1 = dealHand(n)
                        compPlayHand(hand1, wordList, n)
                        break
                
                    
                    
            elif UserInput == 'r':
                while True:
                
                    Input = input('Enter u to have yourself play, c to have the computer play: ')
                    if Input not in "cu":
                        print('invalid input')
                                         
                    elif Input == 'u':
                        playHand(hand1, wordList, n)
                        break
                    elif Input == 'c':
                        compPlayHand(hand1, wordList, n)
                        break
                    else:
                        print('invalid input') 
            elif UserInput == 'e':
                break
            
                
        print("\n")
        
            
            
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    


