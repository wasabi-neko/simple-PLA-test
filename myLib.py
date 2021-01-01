#%%
import numpy
import csv
from enum import Enum

class TrainMsg:
    """
    the enum of trainning masseage
    """
    isIgnored = False
    isAddjusted = False

    def __init__(self, isIgnored, isAddjusted):
        self.isIgnored = isIgnored
        self.isAddjusted = isAddjusted
# End Class TrainMsg


def dataReader(fileName, includeAge=False, includeCabin=False):
    """Read data from csv file and transform into numpy dArray

    Args:
        fileName (str): 
        includeAge (bool, optional): . Defaults to False.
        includeCabin (bool, optional): . Defaults to False.

    Returns:
        (list): {dataVectorList} a list contain many numpy dArray
        (list): {ansList} a corrsponsed ans list contains awnsers
    """
    vectorList = []
    ansList = []
    with open(fileName, 'r') as file:
        reader = csv.DictReader(file)

        # PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
        for row in reader:
            if includeAge and row['Age'] == '':
                continue
            if includeAge and row['Cabin'] == '':
                continue

            # start prepare the data vector
            vector = numpy.arange(9)
            ans = row['Survived']

            vector[0] = 1
            vector[1] = row['Pclass']
            if row['Sex'] == 'male':
                vector[2] = 1
            else:
                vector[2] = 2
            
            if includeAge and row['Age'] != '':
                vector[3] = row['Age']
            else:
                vector[3] = 0

            vector[4] = row['SibSp']
            vector[5] = row['Parch']
            vector[6] = float(row['Fare'])

            if includeCabin and row['Cabin'] != '':
                vector[7] = 1
            else:
                vector[7] = 0

            if row['Embarked'] == 'C':
                vector[8] = 1
            elif row['Embarked'] == 'S':
                vector[8] = 2
            elif row['Embarked'] == 'Q':
                vector[8] = 3
            
            vectorList.append(vector)
            ansList.append(ans)
        # End for each row in csv
    # End with csv file open
    return vectorList, ansList
# End dataReader


def addjustOneNode(dataVec, weightVec, ans):
    """addjust one Node in the data set

    Args:
        dataVec (numpy.DummyArray): one data node
        weightVec (numpy.DummyArray): your weight vector
        ans (bool): the ans of the data

    Returns:
        (numpy.DummyArray): the weight vector after addjust
        (TrainMsg): some message about this single trainning
    """    
         
    result = dataVec.dot(weightVec)
    myAns = 0

    if result > 0:
        myAns = 1
    elif result < 0:
        myAns = 0
    else:
        # if result == 0: then ignore
        return weightVec, TrainMsg(True, False)

    if (myAns == ans):
        return weightVec, TrainMsg(False, False)
    else:
        weightVec += -dataVec
        return weightVec, TrainMsg(False, True)
    
            

# %%
