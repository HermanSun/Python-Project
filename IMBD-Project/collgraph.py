import json
import networkx as nx 

G = nx.Graph()
movie_data_file = r'./IMDb_data/IMDb2006-2015.json'
with open (movie_data_file,'r') as f:
	data = json.load(f)

pair_record = {}	

for r in data.keys():
	name_list = data[r]['Actors'].split(', ')
	if len(name_list) == 0:
		continue
	if len(name_list) == 1:
		if name_list[0] == 'N/A':
			continue
	
	for actorA1 in name_list:
		for actorB1 in name_list:
			actorA = actorA1.strip()
			actorB = actorB1.strip()
			if actorA == actorB:
				continue
			if pair_record.has_key((actorA, actorB)):
				G[actorA][actorB]['double_collaborationtimes'] += 1
			else:
				if actorA > actorB:
					tmp = actorA
					actorA = actorB
					actorB = tmp
				G.add_edge(actorA, actorB, double_collaborationtimes=1)
				pair_record[(actorA, actorB)] = 1
				pair_record[(actorB, actorA)] = 1
		

f = open("collgraph.edgelist", "w+")

for (u, v) in G.edges():
	d = G[u][v]['double_collaborationtimes']
	if d % 2 != 0:
		print u, v, G[u][v]['double_collaborationtimes'], G[v][u]['double_collaborationtimes']
		raw_input()
	
	if u < v:
		f.write(('%s,%s,%d\n'%(u, v, d / 2)).encode('utf-8'))
	else:
		f.write(('%s,%s,%d\n'%(v, u, d / 2)).encode('utf-8'))
	
f.close()
