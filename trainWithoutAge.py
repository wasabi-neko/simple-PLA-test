import myLib
import numpy


trainFileName = './train.csv'
dList, ansList = myLib.dataReader(trainFileName, includeAge=False, cutDataWhichHasnoAge=True,includeCabin=False)
weightVec = myLib.trainModelWithMatrixMethod(dList, ansList, counterLimit=100000000)
print(weightVec)

numpy.save('./withoutAge.npy', weightVec)