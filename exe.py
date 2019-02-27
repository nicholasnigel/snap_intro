import snap

# Load Edge Graph
G = snap.LoadEdgeList(snap.PNGraph,"exercise_graph.txt", 0 , 1)

# -------------------------------- Q1 ----------------------------------------
SGraph = snap.GetSubGraph(G,snap.TIntV.GetV(0,1,2,3,4,5,6,7)) # getting subgraph

snap.DrawGViz(SGraph, snap.gvlDot, "subgraph.png", "subgraph", True) # Drawing subgraph into file 'subgraph.png' into the current working directory

# -------------------------------- Q2 ----------------------------------------

for NI in G.Nodes():
	print "node: %d : out-degree=%d, in-degree=%d" %(NI.GetId(), NI.GetOutDeg(), NI.GetInDeg())

# -------------------------------- Q3 ----------------------------------------

# PR is PageRank
PR = snap.TIntFltH()
snap.GetPageRank(G, PR)		# Gives page rank value 

for item in PR:
	print item, PR[item]

# -------------------------------- Q4 ----------------------------------------
Coeff = snap.GetClustCf(G,-1)
print "Clustering Coefficient: %f" % (Coeff)


# -------------------------------- Q5 ----------------------------------------
UndirectG = snap.ConvertGraph(snap.PUNGraph, G)	#		Convert to undirected graph
for NI in UndirectG.Nodes():
	C = snap.GetDegreeCentr(UndirectG, NI.GetId())	#		For each graph, prepare

print "node %d: centrality %f" %(NI.GetId(), C)	#		print node

