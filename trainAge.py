import myLib
import numpy

trainFileName = './train.csv'

dList, ansList = myLib.dataReader(trainFileName, includeAge=True, cutDataWhichHasnoAge=True, includeCabin=False)
weightVec = myLib.trainModelWithMatrixMethod(dList, ansList, counterLimit=1000000000)
print(weightVec)

numpy.save('./withAge.npy', weightVec)