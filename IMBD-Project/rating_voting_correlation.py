import numpy as np
import matplotlib.pyplot as plt
import json

movie_data_file = './IMDb_data/IMDb2006-2015.json'
with open(movie_data_file, 'r') as f:
	data = json.load(f)

x_rating = []
y_voting = []

for (key, movie) in data.items():
	rating = movie['imdbRating'].strip()
	voting = movie['imdbVotes'].strip()
	
	if rating == "N/A" or voting == "N/A":
		continue
	
	rating = float(rating)
	voting = ''.join(voting.split(','))
	voting = int(voting)
	
	x_rating.append(rating)
	y_voting.append(voting)


plt.figure(figsize=(10, 6), dpi=100)
X = np.array(x_rating, float)
Y = np.array(y_voting, int)

plt.scatter(X, Y, s=15, marker='x', color='blue')

plt.xlim((X.max() - X.min()) * -0.125, X.max() * 1.025)
plt.ylim((Y.max() - Y.min()) * -0.075, Y.max() * 1.225)

plt.xticks(np.linspace(0, 10, 11, endpoint=True), 
		[r"$%d$" % (i) for i in np.linspace(0, 10, 11, endpoint=True)])
plt.yticks(np.linspace(0, 2000000, 6, endpoint=True),\
		[r"$%.1f\times10^{6}$" % (i/1000000.0) for i in np.linspace(0, 2000000, 6, endpoint=True)])
		
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

plt.show()
	
