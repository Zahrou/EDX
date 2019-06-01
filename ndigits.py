
def ndigits(number):
    """
    Takes an integer as input
    Returns the number of digits in number
    """
    if number > 0:
        Snum = str(number)
        return len(Snum)
    else:
        snum = str(number)
        snumNig = snum[1:]
        return len(snumNig)
    

