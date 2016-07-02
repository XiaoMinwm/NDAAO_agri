import re

def replaceseq(seq):
	awaitSeq = []
	nonRepet = []
	delTxtSet = []
	partten = {}

	for x in range(len(seq)):
		awaitSeq.append(seq[x])
	nonRepet = sorted(set(awaitSeq), key=awaitSeq.index)

	for m in nonRepet:
		if not re.match(r'\d+.txt', m):
			delTxtSet.append(m)

	for n in delTxtSet:
		partten[n] = 'Q%d' %delTxtSet.index(n)

	awaitSeq = [partten[x] if x in partten else x for x in awaitSeq]
	return awaitSeq