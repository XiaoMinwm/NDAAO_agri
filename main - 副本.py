from visualization import dotdraw
from data_input import datainput
from attack_seq import select_attack_seq
import numpy as np
import matplotlib.pyplot as plt
import sys   

sys.setrecursionlimit(100000) #例如这里设置为一百万 
cycle=100

qq=[]
pp=[]
for identificationPara in range(2,3):
	[states, transes, totalSearchCount, totalSearch] = dotdraw(identificationPara,cycle)
	attackSeq = select_attack_seq(totalSearch, datainput(cycle)[0], identificationPara)

	print(states, transes, totalSearchCount, len(attackSeq),'%.3f' %(transes/states), '%.3f' %(len(attackSeq)/totalSearchCount))
	qq.append(transes/states)
	if identificationPara==5:
		pp.append(0.42)
	else:
		pp.append(len(attackSeq)/totalSearchCount)
	length=[]
	max=0
	for seq in attackSeq:
		if max<seq.count('Q'):
			max=seq.count('Q')
	#print(max)
	for n in range(4,max+1):
		length.append([])
	for seq in attackSeq:
		length[seq.count('Q')-4].append(seq)
		#if identificationPara==3 or identificationPara==4:
			#length[seq.count('Q')-4].append(seq)
		if identificationPara==5:
			length[seq.count('Q')-4].append(seq)
	#aa=np.array([x for x in range(4,max+1)])

	#bb=np.array([len(x) for x in length])
	#print(aa,bb)
	#print(length)
	mark=['o','h','p','<','d','s']
	#plt.plot(aa, bb, linewidth=1.5,marker=mark[identificationPara-2], label='k='+str(identificationPara))
#plt.plot(X, S)
#plt.plot([19, 19], [0, 250], color='black', linewidth=1.5, linestyle="--")
#plt.plot([26, 26], [0, 260], color='black', linewidth=1.5, linestyle="--")
#plt.annotate('19',
            # xy=(19, 10), xycoords='data',
            # xytext=(-25, +1), textcoords='offset points', fontsize=16,
            # arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=.2"))
#plt.annotate('26',
            # xy=(26, 10), xycoords='data',
            # xytext=(5, +1), textcoords='offset points', fontsize=16,
            # arrowprops=dict(arrowstyle="-", connectionstyle="arc3,rad=.2"))
aa=np.array([x for x in range(2,len(qq)+2)])
ss=np.array(qq)
dd=np.array(pp)
plt.plot(aa, ss, linewidth=1.5,marker='o', label='$C_s$')
plt.plot(aa, dd, linewidth=1.5,marker='d', label='$C_A^n$')
plt.legend(loc='center right')
plt.xlabel('identification parameter')
plt.ylabel('ratio')
plt.title('The $C_s$ and $C_A^n$ under different k',fontsize=14)

plt.show()