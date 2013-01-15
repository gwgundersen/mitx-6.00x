import random

def test(numTrials):
    """
    Uses simulation to compute and return an estimate of
    the probability of at least 30 of the top 100 grades
    coming from a single geographical area purely by chance
    """
    # region codes: africa=0, south america=1, asia=2, europe=3

    c = 0.0
    
    for i in range(numTrials):

        # generate top 100 grades
        grades = []
        for region in range(4):
            for g in range(250):
                grades.append([random.random(), region])
        grades = sorted(grades)[900:]

        af, am, az, eu = 0, 0, 0, 0
        for g in grades:
            if g[1] == 0: af += 1
            if g[1] == 1: am += 1
            if g[1] == 2: az += 1
            if g[1] == 3: eu += 1

        # count exceptional regions
        if (af >= 30 or am >= 30 or az >= 30 or eu >= 30):
            c += 1

    return c / numTrials
                
print test(1000)
