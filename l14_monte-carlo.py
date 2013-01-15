import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    bucket = []
    count = 0.0
    for n in range(numTrials):
        bucket = ['r','r','r','g','g','g']
        for i in range(3):
            index = random.choice(range(len(bucket)))
            bucket.pop(index)
        if 'r' not in bucket or 'g' not in bucket:
            count += 1
    return count / float(numTrials)
