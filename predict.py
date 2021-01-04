import numpy
import myLib
import matplotlib.pyplot as plt


fileName = './test.csv'
dataVecList, ansList = myLib.dataReader(fileName, includeAge=True, cutDataWhichHasnoAge=False, includeCabin=False, hasAns=False)

w_withoutAge = numpy.load('./withoutAge.npy') 
w_withAge = numpy.load('./withAge.npy')

print(w_withoutAge)
print(w_withAge)

survivedList = []

for dataVec in dataVecList:
    # dataVec[3] is age
    if (dataVec[3] == -1):
        result = dataVec.dot(w_withoutAge)
    else:
        result = dataVec.dot(w_withAge)

    if result > 0:
        survivedList.append(1)
        print(1)
    else:
        survivedList.append(0)
        print(0)

    print(dataVec)
    print("------------------")

# draw

# SEX
maleSurvivedCount = 0
maleTotal = 0

femaleSurvivedCount = 0
femaleTotal = 0

# AGE
ageSurvivedList = [0] * 8
ageTotalList = [0] * 8
ageSurvivedRateList = [0] * 8


for dataVec, isSurvived in zip(dataVecList, survivedList):
    # SEX
    if dataVec[2] == 1:
        maleTotal += 1
        if isSurvived:
            maleSurvivedCount += 1
    else:
        femaleTotal += 1
        if isSurvived:
            femaleSurvivedCount += 1

    #AGE
    if dataVec[3] != -1:
        # print(dataVec[3], dataVec[3] / 10)
        index = int(numpy.floor(dataVec[3] / 10))
        ageTotalList[index] += 1
        if isSurvived:
            ageSurvivedList[index] += 1
# end analize

maleSurvivedRate = maleSurvivedCount / maleTotal
femaleSurvivedRate = femaleSurvivedCount / femaleTotal

plotX = [1, 2]
plotY = [maleSurvivedRate, femaleSurvivedRate]
xLabel = ['male', 'female']

plt.bar(plotX, plotY, tick_label=xLabel, color=['blue', 'red'])
plt.ylabel('survived rate')
plt.title('relationship between sex and survivedRate')
plt.savefig('sex&survivedRate.png')
plt.show()

# AGE
for i in range(8):
    if ageTotalList[i] != 0 :
        ageSurvivedRateList[i] = ageSurvivedList[i] / ageTotalList[i]
# end cacu

plotX = range(8)
plotY = ageSurvivedRateList
xLabel = []
for i in range(8):
    xLabel.append("{}0~{}0".format(i, i+1))

plt.bar(plotX, plotY, tick_label=xLabel,color=['aqua'])
plt.title('relationship between age and survivedRate')
plt.savefig('age&survivedRate.png')
plt.show()





