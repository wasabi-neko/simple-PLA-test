import myLib
import numpy


trainFileName = './train.csv'
# trainFileName = './train-mini.csv'

# ------------------------------------------------------------------------------
# not include age
# ------------------------------------------------------------------------------
# dList, ansList = myLib.dataReader(trainFileName, includeAge=False, includeCabin=False)
# # weightVec = myLib.trainModel(dList, ansList, counterLimit=100000000)
# weightVec = myLib.trainModelWithMatrixMethod(dList, ansList, counterLimit=100000000)
# print(weightVec)

# [ -59.  -60.  401.    0.   40.    0.    3.    0. -282.]
# [ -59  -60  401    0   40    0    3    0 -282]    // after 10**8


# ------------------------------------------------------------------------------
# include age
# ------------------------------------------------------------------------------
dList, ansList = myLib.dataReader(trainFileName, includeAge=True, cutDataWhichHasnoAge=True, includeCabin=False)
# weightVec = myLib.trainModel(dList, ansList, counterLimit=100000000)
weightVec = myLib.trainModelWithMatrixMethod(dList, ansList, counterLimit=10000000)
print(weightVec)
# [-14621 -11966  72296   -948   7530   3429   -408      0   1513]


# testing
w = weightVec
print(w)
for x, ans in  zip(dList, ansList):
    result = x.dot(w)
    myAns = 0

    if (result > 0):
        myAns = 1
    elif result < 0:
        myAns = 0
    else:
        myAns = -1        

    if myAns == -1:
        print("ignore")
    else:
        print(myAns == ans)
# END for each data