edgelist = []
with open("collgraph.edgelist", 'r') as collgraph_file:
	line = collgraph_file.readline()
	while line:
		edge = line.strip().split(',')
		if len(edge) != 3:
			print 'Error'
			print edge
			raw_input()
		actorA = edge[0]
		actorB = edge[1]
		times = -int(edge[2])
		if actorA > actorB:
			print 'WTF'
			print actorA, actorB
			raw_input()
			tmp = actorA
			actorA = actorB
			actorB = tmp
		cell = (times, actorA, actorB)
		edgelist.append(cell)
		line = collgraph_file.readline()
		
edgelist.sort()
count = 0
out_file = open("top20pairs.txt", 'w')
for cell in edgelist:
	times, actorA, actorB = cell
	out_file.write(("%s,%s,%d\n" % (actorA, actorB, -times)).encode('utf-8'))
	count += 1
	if count >= 20:
		break
out_file.close()