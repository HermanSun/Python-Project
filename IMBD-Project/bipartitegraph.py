import json

data_string = open("./IMDb_data/IMDb2006-2015.json", "r").read()
movie_list = json.loads(data_string)

actor_to_movies = {}
movie_to_actors = {}

for (index, movie) in movie_list.items():
	id = movie['imdbID'].strip()
	actors= movie['Actors'].strip()
	actor_list = actors.split(',')
	
	if not movie_to_actors.has_key(id):
		movie_to_actors[id] = []
		
	for actor in actor_list:
		actor = actor.strip()
		if not (actor in movie_to_actors[id]):
			movie_to_actors[id].append(actor)
	
	for actor in actor_list:
		actor = actor.strip()
		if not actor_to_movies.has_key(actor):
			actor_to_movies[actor] = []
		
		if not (id in actor_to_movies[actor]):
			actor_to_movies[actor].append(id)

res = {'movie_to_actors':movie_to_actors, 'actor_to_movies':actor_to_movies}

res_string = json.dumps(res, ensure_ascii=False, indent=2)
open("bipartitegraph.json", 'w').write(res_string.encode('utf-8'))
			
