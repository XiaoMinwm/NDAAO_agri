import re

re_output = re.compile(r'\w*(Q\d+)$')
def search(G, initNodeIter, out, collect):
	for node in initNodeIter:
		#print(node)
		initNodeIter = G.itersucc(node)
		out.append(re_output.match(node).group(1))
		search(G, initNodeIter, out, collect)
		print(out)
		str = ('').join(out)
		collect.append(str)
		#print(collect)
		out.pop()
		
	return collect


