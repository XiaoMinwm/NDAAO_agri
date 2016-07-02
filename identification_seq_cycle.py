from data_input import datainput

def identification(k, seqSet):
	wordObsState = []
	wordObsTrans = []

	for x in seqSet:
		for n in range(k-1):
			x.insert(0, x[0])
			x.append(x[0])
		seqSet[seqSet.index(x)] = x

		for i in range(len(x)-(k-1)):
			joinSeqState = ''
			for m in range(k):
				joinSeqState += x[i+m]
			wordObsState.append(joinSeqState)
		for j in range(len(x)-k):
			joinSeqTrans = ''
			for n in range(k+1):
				joinSeqTrans += x[j+n]
			wordObsTrans.append(joinSeqTrans)

	wordObsState = sorted(set(wordObsState), key=wordObsState.index)
	wordObsTrans = sorted(set(wordObsTrans), key=wordObsTrans.index)

	return (wordObsState, wordObsTrans)
