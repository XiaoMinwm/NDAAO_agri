import re
import os
from sym_rep import replaceseq


def datainput(cycles):
    if os.path.isfile('./output/45.gv'):
        os.remove('./output/45.gv')
    with open('./result.txt', 'r') as data:
        cycleData = []
        for line in data.readlines():
            cycleData.append(line.strip())

    symData = replaceseq(cycleData)
    singleCycleData = []
    for i in range(cycles):
        singleCycleData.append([])

    cycle = -1
    for x in range(len(symData)):
        if not re.match(r'\d+.txt', symData[x]):
            singleCycleData[cycle].append(symData[x])
        else:
            cycle += 1

    binCycleData = []
    for i in range(cycles):
        binCycleData.append([])

    cycle = -1
    for x in range(len(cycleData)):
        if not re.match(r'\d+.txt', cycleData[x]):
            binCycleData[cycle].append(cycleData[x])
        else:
            cycle += 1
    # print(singleCycleData,binCycleData)
    return singleCycleData, binCycleData
