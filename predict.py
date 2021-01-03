import numpy
import myLib


fileName = './test.csv'
dataVecList, ansList = myLib.dataReader(fileName, includeAge=True, cutDataWhichHasnoAge=False, includeCabin=False, hasAns=False)

w_withoutAge = numpy.load('./withoutAge.npy') 
w_withAge = numpy.load('./withAge.npy')

print(w_withoutAge)
print(w_withAge)

for dataVec, ans in zip(dataVecList, ansList):

    print(dataVec)

    # dataVec[3] is age
    if (dataVec[3] == -1):
        result = dataVec.dot(w_withoutAge)
    else:
        result = dataVec.dot(w_withAge)

    if result > 0:
        ans = 1
    else:
        ans = 0

    print(dataVec)
    print(ans, end='---------\n')

# draw 