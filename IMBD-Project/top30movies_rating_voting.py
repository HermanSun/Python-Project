import json

movie_data_file = './IMDb_data/IMDb2006-2015.json'
with open(movie_data_file,'r') as f:
	data = json.load(f)
	
rating_list = []
voting_list = []

for key, movie in data.items():
	if not movie.has_key('Title'):
		continue
	
	if movie['Title'] == "N/A":
		continue
	
	title = movie['Title']
	id = movie['imdbID']

	if movie['imdbRating'] != "N/A":
		rating = float(movie['imdbRating'])
		rating_list.append((-rating, title, id))
		
	if movie['imdbVotes'] != "N/A":
		voting = int(''.join(movie['imdbVotes'].split(',')))
		voting_list.append((-voting, title, id))
	
rating_list.sort()
voting_list.sort()

res = {'rating':[], 'voting':[], 'comm':0}

count = 0
last = None
for x, y, z in rating_list:
	if x != last and count >= 30:
		break
	count += 1
	res['rating'].append((-x, y, z))
	last = x

count = 0
last = None
for x, y, z in voting_list:
	if x != last and count >= 30:
		break
	count += 1
	res['voting'].append((-x, y, z))
	last = x
		
for ratingA, titleA, idA in res['rating']:
	for votingB, titleB, idB in res['voting']:
		if titleA == titleB and idA == idB:
			res['comm'] += 1

last = None
count = 0
f = open('top30movies_rating_voting.txt', 'w')
f.write("Rating:\n")
for rating, title, id in res['rating']:
	if rating != last:
		count += 1
		f.write(("%-5d%.2f %s\n" % (count, rating, title)).encode('utf-8'))
	else:
		f.write(("     %.2f %s\n" % (rating, title)).encode('utf-8'))
	last = rating

last = None
count = 0
f.write("\nVoting:\n")
for voting, title, id in res['voting']:
	if voting != last:
		count += 1
		f.write(("%-5d%d %s\n" % (count, voting, title)).encode('utf-8'))
	else:
		f.write(("%d %s\n" % (voting, title)).encode('utf-8'))
	last = voting
	
f.write("\nCommon: " + str(res['comm']))
