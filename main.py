import myLib
import numpy


trainFileName = './train.csv'
# trainFileName = './train-mini.csv'
dList, ansList = myLib.dataReader(trainFileName, includeAge=False, includeCabin=False)

# for vec, ans in zip(dList, ansList):
#     print(vec, end='; ')
#     print(ans)

# weightVec = numpy.arange(len(dList[0]))

# weightVec = myLib.trainModel(dList, ansList, counterLimit=100000000)
weightVec = myLib.trainModelWithMatrixMethod(dList, ansList, counterLimit=100000000)
print(weightVec)

# w = numpy.array([-1937.0,   -97.0,  1587.0,     0.0,  -587.0,  -193.0,    43.0,     0.0,  -403.0,])
# [ -59.  -60.  401.    0.   40.    0.    3.    0. -282.]
# [ -59  -60  401    0   40    0    3    0 -282]    // after 10**8
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