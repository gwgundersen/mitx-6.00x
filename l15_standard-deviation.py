def stdDevOfLengths(L):

    # if L is empty
    if len(L) == 0:
        return float('NaN')
    
    # generate new list of string lengths
    newL = []
    for e in L:
        newL.append(len(e))
    mean = sum(newL)/float(len(newL))
	
    # calculate the standard deviation
    V = 0.0
    for e in newL:
        V += (e - mean)**2
    variance = V / len(newL)

    # return standard deviation
    return variance**0.5