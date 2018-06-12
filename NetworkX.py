
# coding: utf-8

# In[137]:


import pprint
import json 
import math
import networkx as nx
import matplotlib as plt

pp = pprint.PrettyPrinter()

def readfile(filename):
	with open(filename) as f:
		lines = f.readlines()
	return lines


# In[138]:


def make_edges(lines):
	edg = []
	for l in lines:
		e = []
		mid = l[l.find(';') + 1:l.find(';', l.find(';') + 1)]
		rby = l[l.find('by') + 3:l.find(' ', l.find('by') + 3)]
		rfrom = l[l.find('from') + 5:l.find(' ', l.find('from') + 5)]
# 		print mid, rby, rfrom
		e = [rby, rfrom]
# 		if (rby == '137.113' or rfrom == '137.113'):
# 			print e
		edg.append(e)
	return edg
        


# In[171]:


def main():
	lines = readfile('nlog')
	print len(lines)
	lines = [l for l in lines if l.find('broadcast message received by') != -1]
	print len(lines)
	edges = make_edges(lines)
	g = nx.Graph(edges)
# 	pos = nx.spring_layout(g, scale=40, pos=graphviz_layout(G))
	nx.draw_networkx(g,
                     # pos = nx.spring_layout(g, k=.5, iterations=200),
                     node_size=300, font_size=8, node_color='yellow')
# 	plt.figure(figsize=(160,180))
# 	plt.show()
	# pp.pprint(lines)
# 	pos = nx.spring_layout(g,scale=2)
# 	nx.draw(g,pos,font_size=8)


# In[172]:


if __name__ == '__main__':
	main()


# In[183]:


import networkx as nx
import pylab
lines = readfile('nlog')
print len(lines)
lines = [l for l in lines if l.find('broadcast message received by') != -1]
print len(lines)
edges = make_edges(lines)
g = nx.Graph(edges)
pos=nx.spring_layout(g)
#pylab.figure(1,figsize=(3,3))
pylab.figure(2,figsize=(12,12))
# pylab.xlim(0,1)
# pylab.ylim(0,1)
nx.draw(g,pos,font_size=8, with_labels=True, node_size=500, font_color='black', node_color='#ffeeff')
#nx.draw(G,pos,font_size=10)
pylab.show()

