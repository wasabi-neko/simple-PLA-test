#%%
import numpy as np
from numpy.core.fromnumeric import _swapaxes_dispatcher

X = []


# read file
isFirstLine = 1
file = open("./train.csv")
lines = file.readlines()
for line in lines:
    if (isFirstLine == 0):
        #           0,      1       2   3 |   4    5      6       7       8       9   10        11
        # PassengerId,Survived,Pclass,Name, Sex, Age, SibSp, Parch,  Ticket,   Fare, Cabin,   Embarked
        #           no,      y,   int, not,bool, int,   int, int,    str+int, float, str+int, S/C/Q
        elementList = line.split(',')
        # exclude the data which missing age col
        if (elementList[6] != ''):
            ans = elementList[1]

            temp = np.arange(7)
            temp[0] = 1                     # x0 is 1
            temp[1] = int(elementList[2])    # Pclass
            if elementList[4] == 'male':    # sex
                temp[2] = 0
            else:
                temp[2] = 1
            temp[3] = float(elementList[6])    # age
            temp[4] = int(elementList[7])    # Sibp
            temp[5] = int(elementList[8])    # Parch
            temp[6] = float(elementList[10])    # flare
            
            # Embarked
            if elementList[12] == 'C':
                temp[7] = 1
            elif elementList[12] == 'S':
                temp[7] = 2
            elif elementList[12] == 'Q':
                temp[7] = 3

            print(elementList[0], temp)
        
    isFirstLine = 0

file.close()
# # END read file

# %%
