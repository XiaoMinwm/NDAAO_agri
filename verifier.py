def verifier_seq(veriVector,seq):
#########
#观测输出验证器
#输入
#veriVector：待检测输出向量
#model：便是模型
#collSeq：采集的向量
#输出
#veriResult：验证结果
#########
	destString = ''.join(seq)
	res =  map(lambda x:x,filter(lambda x:x in destString,veriVector))
	return list(res)

def verifier(veriVector, model, collSeq):
	attackFlag = False
	faultAttVec = []
	falseSeqAttVec = []
	for seq in model:
		faultAttVec+=verifier_seq(veriVector,seq)
	if not faultAttVec:
		attackFlag = True
		print( '[%s] not in the state model, maybe exist FAULT-LIKE attack'%(','.join(veriVector)))
		return True;
	if not attackFlag:
		for seq in collSeq:
			falseSeqAttVec+=verifier_seq(veriVector,seq)
		if not falseSeqAttVec:
			attackFlag = True
			print( '[%s] not in right logic of model, maybe exist FALSE SEQUENCE attack'%(','.join(veriVector)))
			return True;
	if not attackFlag:
		print('not found any attack')
		return False;


