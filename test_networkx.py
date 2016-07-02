import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()   # or DiGraph, MultiGraph, MultiDiGraph, etc
G = nx.DiGraph(name='my graph')
G.add_nodes_from([(1,dict(size=30)), (2,{'color':'blue'})])
G.add_node(3,weight=0.4,UTM=('13S',382871,3972649))
e = [(1,2),(2,3),(3,4)]
G.add_edges_from(e) 
print(G.nodes(data=True))
nx.draw(G, pos=None, arrows=True, with_labels=True)
plt.show()