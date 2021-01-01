import myLib
import numpy


trainFileName = './train.csv'
dList, ansList = myLib.dataReader(trainFileName, includeAge=False, includeCabin=False)

# for vec, ans in zip(dList, ansList):
#     print(vec, end='; ')
#     print(ans)

weightVec = numpy.arange(len(dList[0]))
print(weightVec)