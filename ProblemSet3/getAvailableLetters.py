def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = string.ascii_lowercase
    for i in lettersGuessed:
        availableLetters = availableLetters.replace(i, '')
    return availableLetters

    
   
