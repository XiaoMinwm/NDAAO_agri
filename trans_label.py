def label(a, b):
	#print(a,b)
	#vector=['k1','k2','a0','a1','a2','b0','b1','c0','c1','d0','d1','A+','A-','B','C','D']
	vector=['Ta1','Tb1','Ta2','Tb2','Ta3','Tb3','Ta4','Tb4','Ta5','Tb5','s1','s2','s3','s4','s5']
	coll=[]
	t=0
	while(t!=-1):
		if t==0 and coll==[]:
			t=-1
		t = int2bin(int(a,2)^int(b,2), len(a)).find('1',t+1)
		if t != -1:
			coll += [vector[t]+'_'+int2bin((int(a,2)^int(b,2))&int(b,2), len(a))[t]]
	return coll

def int2bin(n, count=15):
	return ''.join([str((n>>y)&1) for y in range(count-1,-1,-1)])

if __name__ == '__main__':
	print(int2bin(7))
