from ps8b import *

def test1():
    print 'Test 1: initializing virus'
    try:
        virus = SimpleVirus(0.0, 0.0)
        print 'Test 1: passed'
    except Exception,e:
        print str(e) 

def test2(numViruses):
    print 'Test 2: initializing patient'

    viruses = []
    for i in range(numViruses):
        viruses.append(SimpleVirus(1.0, 0.0))

    try:
        patient = Patient(viruses, 0.0)
        print 'Test 2: passed'
    except Exception,e:
        print str(e)

def test3(numTrials):
    print 'Test 3: creating ' + str(numTrials) + \
          ' viruses that do clear and do reproduce'
    for i in range(numTrials):
        virus = SimpleVirus(1.0, 1.0)
        virus.doesClear()
        virus.reproduce(0)
    print 'Test 3: passed'

def test4(numTrials, numViruses):
    print 'Test 4: Create a Patient with virus that ' + \
          'is always cleared and always reproduces'
    virus = SimpleVirus(1.0, 0.0)
    
    viruses = []
    for i in range(numViruses):
        viruses.append(SimpleVirus(1.0, 0.0))

    patient = Patient(viruses, 100)
    patient.getTotalPop()
    print 'Test 4: passed'

def test5():
    return simulationWithoutDrug(100, 1000, .1, 0.99, 50)

"""
MAIN PROGRAM
"""
#test1()
#test2(10)
#test3(10)
#test4(100, 100)
test5()
