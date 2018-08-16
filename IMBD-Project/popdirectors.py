import json
movie_data_file = './IMDb_data/IMDb2006-2015.json'
with open (movie_data_file,'r') as f:
	data_string = json.load(f)

edgelist = []
with open("top20pairs.txt", 'r') as actors_file:
	line = actors_file.readline()
	while line:
		edge = line.strip().split(',')
		if len(edge) != 3:
			print 'Error'
			print edge
			raw_input()
		actorA = edge[0]
		actorB = edge[1]
		times = -int(edge[2])

		cell = (actorA, actorB)
		edgelist.append(cell)
		line = actors_file.readline()
#print edgelist

directors = {}
for r in data_string.keys():
	actor_list = data_string[r]['Actors'].strip().split(',')
	actor_list = [x.strip() for x in actor_list]
	if len(actor_list) == 0:
		continue
	if len(actor_list) == 1:
		if actor_list[0] == 'N/A':
			continue
	
	director_list =  data_string[r]['Director'].strip().split(',')
	director_list = [x.strip() for x in director_list]
	if len(director_list) == 0:
		continue
	if len(director_list) == 1:
		if director_list[0] =='N/A':
			continue
	
	for cell in edgelist:
		#print cell[0], cell[1]
		#print actor_list
		if cell[0] in actor_list:
			if cell[1] in actor_list:
				#print cell[0], cell[1]
				#print actor_list
				dkey = cell[0]+','+cell[1]
				for director_name in director_list:
					#print dkey
					if directors.has_key(dkey):
						if directors[dkey].has_key(director_name):
							directors[dkey][director_name] += 1
						else:
							directors[dkey][director_name] = 1
					else:
						directors[dkey] = {}
						directors[dkey][director_name] = 1

for cell in edgelist:
	if not directors.has_key(cell[0]+','+cell[1]):
		directors[cell[0]+','+cell[1]] = {'N/A':1}

f = open("popdirectors.txt", "w")

for cell in edgelist:
	dkey = cell[0]+','+cell[1]
	sort_list = []
	for name, times in directors[dkey].items():
		sort_list.append((-times, name))
	sort_list.sort()
	#print sort_list
	f.write(("%s,%s,%s\n" % (cell[0], cell[1], sort_list[0][1])).encode('utf-8'))

f.close()
