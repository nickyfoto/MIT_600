import numpy
import random
import pylab

from ps3b import *   


def simulationWithDrug2(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials, stepsBeforeSecondDrug):
    res = []
    patientList = []
    for i in range(numTrials):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        virusList = []
        for i in range(numViruses):
            virusList.append(virus)
        patient = TreatedPatient(virusList, maxPop)
        patientList.append(patient)
    totalRecord = []
    for p in patientList:
        pRecord = []
        for i in range(150):
            pRecord.append(p.update())
        p.addPrescription('guttagonol')
        for i in range(stepsBeforeSecondDrug):
            pRecord.append(p.update())
        p.addPrescription('grimpex')
        for i in range(150):
            pRecord.append(p.update())
        totalRecord.append(pRecord)
    for e in totalRecord:
        res.append(e[-1])
    return res



def labelPlot(stepsBeforeDrug):
    pylab.title(str(stepsBeforeDrug) + ' steps before drug')
    pylab.xlabel('Number of Total Virus After Treatment')
    pylab.ylabel('Number of Trials')


        
def simulationDelayedTreatment(numTrials):
    cured = []
    # pylab.figure(1)
    res1 = simulationWithDrug2(100, 1000, 0.1, 0.05, {"guttagonol": False, 'grimpex': False}, 0.005, numTrials, 150)
    for e in res1:
        if e < 50:
            cured.append(e)
    print len(cured)/float(numTrials)
    # pylab.hist(res1)
    # labelPlot(150)
    # pylab.show()

    cured2 = []
    
    res2 = simulationWithDrug2(100, 1000, 0.1, 0.05, {"guttagonol": False, 'grimpex': False}, 0.05, numTrials, 150)
    for e in res2:
        if e < 50:
            cured2.append(e)
    print len(cured2)/float(numTrials)
    
    # pylab.figure(2)
    # pylab.hist(simulationWithDrug2(100, 1000, 0.1, 0.05, {"guttagonol": False}, 0.005, numTrials, 150))
    # labelPlot(150)
    # pylab.show()

    # pylab.figure(3)
    # pylab.hist(simulationWithDrug2(100, 1000, 0.1, 0.05, {"guttagonol": False}, 0.005, numTrials, 75))
    # labelPlot(75)
    # pylab.show()

    # pylab.figure(4)
    # pylab.hist(simulationWithDrug2(100, 1000, 0.1, 0.05, {"guttagonol": False}, 0.005, numTrials, 0))
    # labelPlot(0)
    # pylab.show()

simulationDelayedTreatment(100)
