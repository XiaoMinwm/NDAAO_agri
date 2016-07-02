def attack_seq(totalseq, data, k):
	destString = ''.join(data)
	res =  map(lambda x:x,filter(lambda x:x not in destString and len(x)>=(k+2),totalseq))
	return list(res)

def select_attack_seq(totalseq, inputdata, k):
	for vector in inputdata:
		totalseq = attack_seq(totalseq, vector, k)
		#print(totalseq)
		#print(len(totalseq))

	return totalseq