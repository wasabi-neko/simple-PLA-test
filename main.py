import myLib
import numpy


trainFileName = './train.csv'
dList, ansList = myLib.dataReader(trainFileName, includeAge=False, includeCabin=False)

# for vec, ans in zip(dList, ansList):
#     print(vec, end='; ')
#     print(ans)

# weightVec = numpy.arange(len(dList[0]))

weightVec = myLib.trainModel(dList, ansList, counterLimit=100000)
print(weightVec)

# w = numpy.array([-1937.0,   -97.0,  1587.0,     0.0,  -587.0,  -193.0,    43.0,     0.0,  -403.0,])
w = weightVec
for x, ans in  zip(dList, ansList):
    result = x.dot(w)
    myAns = 0

    if (result > 0):
        myAns = 1
    else:
        myAns = 0

    print(myAns == ans)