from visualization import dotdraw_net, visualizeAttack
from data_input import datainput
from verifier import verifier

if __name__ == '__main__':
	model = dotdraw_net(4,50)
	waitSeq = [['Q0Q43Q44Q45Q46Q4Q10Q48Q63Q61Q71Q52Q53Q50Q54Q55Q56Q57Q58Q46'],['Q0Q81Q82Q84Q85Q86Q96Q130']]
	for seq in waitSeq:
		if verifier(seq,model[3],datainput(50)[0]):
			visualizeAttack(seq, model, datainput(50)[0], 4)
			visualizeAttack(seq, model, datainput(50)[0], 4)