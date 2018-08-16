
d = dict()

movie_data_file = r'collgraph.edgelist'
with open(movie_data_file,'r') as fp:
    for line in fp:
        #print line
    	temlst = line.split(',')
    	temlst[0] = temlst[0].strip()
    	temlst[1] = temlst[1].strip()
    	temlst[2] = temlst[2].strip()
    	if temlst[0] not in  d:
    		d[temlst[0]] = int(temlst[2])
    	else:
    		d[temlst[0]] += int(temlst[2])
    	if temlst[1] not in d:
    		d[temlst[1]] = int(temlst[2])
    	else:
    		d[temlst[1]] += int(temlst[2])
#l = list()
#for key, val in d.items():
#	l.append((val,key))
l = d.items()
#print l
s = sorted(l, key=lambda tup: tup[1], reverse = True)
#print s



f = open("top10actors.txt", "w+")

for i in range(10):
	x,y = s[i]
	f.write(('%s,%d\n'%(x, y)).encode('utf-8'))
	
f.close()







    