def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            s += letter
        else:
            s += '_'
            s += ' '
    return s
print(getGuessedWord('apple', ['e', 'i', 'k', 'p', 'r', 's']))
