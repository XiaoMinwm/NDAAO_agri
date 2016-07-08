import re
from graphviz import Digraph
from data_input import datainput
from identification_seq import identification
import pygraphviz as pgv
from search import search
from trans_label import label
import networkx as nx
import pydotplus as pydot
import matplotlib.pyplot as plt
import Levenshtein as lev
from PIL import Image

re_output = re.compile(r'\w*(Q\d+)$')
re_first = re.compile(r'^(Q\w+)Q\d+$')
re_last = re.compile(r'^Q\d+(Q\w+)$')


def filterLastOut(str, k):
    filterStr = ''
    filterArray = []
    for i in range(k):
        filterArray.append(re_output.match(str).group(1))
        str = str[0:len(str) - len(re_output.match(str).group(1))]
    for x in range(len(filterArray)):
        filterStr += filterArray[len(filterArray) - x - 1]
    return filterStr


def visualizeAttack(att, model, real, k):
    A = pgv.AGraph('simple.dot')
    strReal = []
    realOutput = []
    for r in real:
        strReal.append(''.join(r))
    for state in model[4]:
        realOutput.append(re_output.match(state).group(1))
    realPath = list(filter(lambda x: len(x) > k, strReal))
    maxPathDict = {}
    Max = lev.ratio(realPath[0], att[0])
    for seq in realPath:
        jaro = lev.ratio(seq, att[0])
        if (Max <= jaro):
            Max = jaro
            maxPathDict[jaro] = seq
    bestPath = maxPathDict[Max]
    bestNode = list(filter(lambda x: x in bestPath, model[4]))
    attNode = list(filter(lambda x: x in att[0], model[4]))
    for node in attNode:
        A.add_node(node, color='red')
        A.get_node(node).attr['shape'] = 'doubleoctagon'
    for node in attNode:
        for node1 in attNode:
            if A.has_edge(node, node1):
                A.get_edge(node, node1).attr['color'] = 'red'
    # To show the fault
    if re_output.match(att[0]).group(1) not in realOutput:
        A.add_node(re_output.match(att[0]).group(1), color='red', shape='doubleoctagon')
        A.add_edge(attNode[len(attNode) - 1], re_output.match(att[0]).group(1), color='red')
    elif filterLastOut(att[0], k) not in realOutput:
        A.add_node(filterLastOut(att[0], k), color='red', shape='doubleoctagon')
        A.add_edge(attNode[len(attNode) - 1], filterLastOut(att[0], k), color='red')

    for node in bestNode:
        A.add_node(node, color='yellow')
    for node in bestNode:
        for node1 in bestNode:
            if A.has_edge(node, node1):
                A.get_edge(node, node1).attr['color'] = 'green'
    A.layout(prog='dot')  # layout with default (neato)
    A.draw('showAttack[' + att[0] + '].png')  # draw png


def dotdraw(k, cycle):
    A = pgv.AGraph()
    # dot = Digraph(comment='The Round Table', engine='dot')
    [seqState, seqTrans] = identification(k, datainput(cycle)[0])
    [seqState1, seqTrans1] = identification(1, datainput(cycle)[0])
    [binState, binTrans] = identification(1, datainput(cycle)[1])
    # print(seqState,binState)
    # print(seqTrans)

    # for state in seqState:
    # dot.node(state, 'x%d' %seqState.index(state) + '\n%s' %re_output.match(state).group(1))
    # A.add_node(state, label='x%d' %seqState.index(state) + '\n%s' %state)
    # A.add_node(state, label='x%d' %seqState.index(state) + '\n%s' %re_output.match(state).group(1))
    # A.add_node(state, label='x%d' %seqState.index(state) + '\n%s' %re_output.match(state).group(1))

    for trans in seqTrans:
        # dot.edge(re_first.match(trans).group(1), re_last.match(trans).group(1))
        # print(binState[seqState.index(re_first.match(trans).group(1))],binState[seqState.index(re_last.match(trans).group(1))])
        lab = label(binState[seqState1.index(re_output.match(re_first.match(trans).group(1)).group(1))],
                    binState[seqState1.index(re_output.match(re_last.match(trans).group(1)).group(1))])
        # print(lab)
        # A.add_edge(re_first.match(trans).group(1), re_last.match(trans).group(1), label=','.join(lab))
        A.add_edge(binState[seqState1.index(re_output.match(re_first.match(trans).group(1)).group(1))],
                   binState[seqState1.index(re_output.match(re_last.match(trans).group(1)).group(1))],
                   label=','.join(lab))

    out = []
    collect = []
    totalSearch = []
    # nodeiter=['Q0Q0']

    for nodeiter in A.nodes():
        # print(nodeiter)
        # totalSearch += search(A, [nodeiter], out, collect)
        out = []
        collect = []
    A.write('simple.dot')  # write to simple.dot
    B = pgv.AGraph('simple.dot')  # create a new graph from file
    B.layout(prog='dot')  # layout with default (neato)
    B.draw('simple.png')  # draw png
    B.draw('simple.pdf')  # draw png
    print(len(seqState))
    return (len(seqState), len(seqTrans), len(totalSearch), totalSearch)


def dotdraw_net(k, cycle):
    G = nx.DiGraph()
    [seqState, seqTrans] = identification(k, datainput(cycle)[0])
    [seqState1, seqTrans1] = identification(1, datainput(cycle)[0])
    [binState, binTrans] = identification(1, datainput(cycle)[1])
    re_output = re.compile(r'\w*(Q\d+)$')
    for state in seqState:
        # G.add_node(state, label='x%d' %seqState.index(state) + '\n%s' %re_output.match(state).group(1))
        G.add_node(state, label=state + '\n%s' % re_output.match(state).group(1))
    re_first = re.compile(r'^(Q\w+)Q\d+$')
    re_last = re.compile(r'^Q\d+(Q\w+)$')
    for trans in seqTrans:
        lab = label(binState[seqState1.index(re_output.match(re_first.match(trans).group(1)).group(1))],
                    binState[seqState1.index(re_output.match(re_last.match(trans).group(1)).group(1))])
        G.add_edge(re_first.match(trans).group(1), re_last.match(trans).group(1), label=','.join(lab))
    allPath = []
    for node in seqState:
        for path in nx.all_simple_paths(G, seqState[0], node):
            path = [re_output.match(node).group(1) for node in path]
            # print(path)
            allPath.append(''.join(path))
    # print(allPath)
    # nx.draw(G, pos=nx.spring_layout(G), arrows=True, with_labels=True)
    # plt.savefig('test_9.png')
    # 测试而已
    # plt.show()
    return (len(seqState), len(seqTrans), len(allPath), allPath, seqState, seqTrans)


if __name__ == '__main__':
    dotdraw_net(2, 28)
