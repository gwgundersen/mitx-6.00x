# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps9_ps8 import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """

    # create variables
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005

    timeSteps, treatStep = 300, 150
    totalVs, resisVs = [], []
    results = []
    
    for step in range(timeSteps): totalVs.append(0), resisVs.append(0)
    
    # run number of trials
    for trial in range(numTrials):
                
        # instantiate viruses and patient
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        patient = TreatedPatient(viruses, maxPop)
        
        # update total virus population
        # then get num resistant viruses
        # add drug
        # repeat above
        for step in range(timeSteps):
            if step == treatStep:
                patient.addPrescription('guttagonol')
            patient.update()
            totalVs[step] += patient.getTotalPop()
            resisVs[step] += patient.getResistPop(['guttagonol'])

        results.append(patient.getTotalPop())

    pylab.hist(results, 9)
    pylab.show()

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # create variables
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances =  {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    firstDrugStep = 150
    secondDrugStep = 150 + 150
    timeSteps = secondDrugStep + 150
    totalVs, resisVs = [], []
    results = []
    
    for step in range(timeSteps): totalVs.append(0), resisVs.append(0)
    
    # run number of trials
    for trial in range(numTrials):
                
        # instantiate viruses and patient
        viruses = []
        for i in range(numViruses):
            viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
        patient = TreatedPatient(viruses, maxPop)
        
        # update total virus population
        # then get num resistant viruses
        # add drug
        # repeat above
        for step in range(timeSteps):
            if step == firstDrugStep:
                patient.addPrescription('guttagonol')
            if step == secondDrugStep:
                patient.addPrescription('grimpex')
            patient.update()
            totalVs[step] += patient.getTotalPop()
            resisVs[step] += patient.getResistPop(['guttagonol'])
            resisVs[step] += patient.getResistPop(['grimpex'])
            
        results.append(patient.getTotalPop())

    pylab.hist(results, 9)
    pylab.show()

#
# MAIN PROGRAM
#

simulationTwoDrugsDelayedTreatment(300)
