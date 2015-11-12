#coding:utf-8
# Problem Set 3: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab
import copy

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''
class SimpleVirus(object):
    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
    def getMaxBirthProb(self):
        return self.maxBirthProb
    def getClearProb(self):
        return self.clearProb
    def doesClear(self):
        if random.random() < self.getClearProb():
            return True
        else:
            return False  
    def reproduce(self, popDensity):     
        
        if random.random() < self.getMaxBirthProb() * (1 - popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        else:
            raise NoChildException

class Patient(object):
    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop
    def getViruses(self):
        return self.viruses
    def getMaxPop(self):
        return self.maxPop
    def getTotalPop(self):
        return len(self.viruses)
    def update(self):
        for v in self.viruses[:]:
            if v.doesClear():
                self.viruses.remove(v)
        popDensity = self.getTotalPop() / float(self.getMaxPop())
        for v in self.viruses[:]:
            try:
                self.viruses.append(v.reproduce(popDensity))
            except NoChildException:
                pass        
        return len(self.viruses)


class ResistantVirus(SimpleVirus):
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistances(self):
        return self.resistances

    def getMutProb(self):
        return self.mutProb

    def isResistantTo(self, drug):
        if drug in self.getResistances():
            return self.getResistances()[drug]

    def reproduce(self, popDensity, activeDrugs):
        for d in activeDrugs:
            if self.getResistances().has_key(d):
                if self.getResistances()[d] == False:     
                    raise NoChildException                

        if random.random() < self.getMaxBirthProb() * (1 - popDensity):
            for e in self.getResistances():
                if random.random() < self.getMutProb():
                    self.getResistances()[e] = not self.getResistances()[e]
            return ResistantVirus(self.getMaxBirthProb(), self.getClearProb(), self.getResistances(), self.getMutProb())
        else:
            raise NoChildException            

class TreatedPatient(Patient):
    def __init__(self, viruses, maxPop):
        Patient.__init__(self, viruses, maxPop)
        self.drugList = []

    def addPrescription(self, newDrug):
        if newDrug not in self.drugList:
            self.drugList.append(newDrug)

    def getPrescriptions(self):
        return self.drugList

    def getResistPop(self, drugResist): 
        res = []                                      
        for v in self.getViruses():
            if all(map(v.isResistantTo, drugResist)): 
                res.append(v)
        return len(res)

    def update(self):
        for v in self.getViruses()[:]:
            if v.doesClear():
                self.getViruses().remove(v)
        popDensity = self.getTotalPop() / float(self.getMaxPop())
        

        for v in self.getViruses()[:]:
            try:
                self.getViruses().append(copy.deepcopy(v).reproduce(popDensity, self.getPrescriptions()))
            except NoChildException:
                pass
        return len(self.getViruses())

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    patientList = []
    for i in range(numTrials):
        virus = SimpleVirus(maxBirthProb, clearProb)
        virusList = []
        for i in range(numViruses):
            virusList.append(virus)
        patient = Patient(virusList, maxPop)
        patientList.append(patient)
    
    totalRecord = []
    
    for p in patientList:
        pRecord = []
        for i in range(300):
            pRecord.append(p.update())
        totalRecord.append(pRecord)
    res = []
    for i in range(300):    
        ave = []
        for r in totalRecord:
            ave.append(r[i])
        res.append(sum(ave)/float(len(ave)))

    pylab.plot(res)
    pylab.title('Virus Reproduce Simulation')
    pylab.xlabel('Number of timeSteps')
    pylab.ylabel('Qty of Viruses')
    pylab.legend('Growth')
    pylab.show()

def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    patientList = []
    for i in range(numTrials):
        virus = ResistantVirus(maxBirthProb, clearProb, resistances, mutProb)
        virusList = []
        for i in range(numViruses):
            virusList.append(virus)
        patient = TreatedPatient(virusList, maxPop)
        patientList.append(patient)
    totalRecord = []
    resistantRecord = []
    for p in patientList:
        pRecord = []
        rRecord = []
        for i in range(150):
            pRecord.append(p.update())
            rRecord.append(p.getResistPop(['guttagonol']))
        p.addPrescription('guttagonol')
        for i in range(150):
            pRecord.append(p.update())
            rRecord.append(p.getResistPop(p.getPrescriptions()))
        totalRecord.append(pRecord)
        resistantRecord.append(rRecord)

    res1 = []
    for i in range(300):    
        ave1 = []
        for r in totalRecord:
            ave1.append(r[i])
        res1.append(sum(ave1)/float(len(ave1)))
    res2 = []
    for i in range(300):    
        ave2 = []
        for r in resistantRecord:
            ave2.append(r[i])
        res2.append(sum(ave2)/float(len(ave2)))

    pylab.plot(res1, label = 'total virus population')
    pylab.plot(res2, label = 'resistant population')
    pylab.title('ResistantVirus simulation')
    pylab.xlabel('time step')
    pylab.ylabel('# viruses')
    pylab.legend()
    pylab.show()


