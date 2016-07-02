from visualization import *
from data_input import datainput
from attack_seq import select_attack_seq
import numpy as np
import matplotlib.pyplot as plt
import sys   

sys.setrecursionlimit(100000) #例如这里设置为一百万 
cycle=50
identificationPara=4
dotdraw(identificationPara,cycle)
[states, transes, totalSearchCount, totalSearch, seqState, seqTrans] = dotdraw_net(identificationPara,cycle)
attackSeq = select_attack_seq(totalSearch, datainput(cycle)[0], identificationPara)
print(states, transes, totalSearchCount, attackSeq, len(attackSeq),'%.3f' %(transes/states), '%.3f' %(len(attackSeq)/totalSearchCount))
