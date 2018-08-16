#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import json


def IMDb_query_url(id):
    # the returned query url for id='tt0407887' should be 'http://www.omdbapi.com/?i=tt0407887&plot=short&r=json'
    query_url = "http://www.omdbapi.com/?i="+id.strip()+"&plot=short&r=json"
    return query_url


def get_movie_ids(input_file):
    # the returned list should like ['tt0407887', 'tt1212123', ... ]
    id_list = []
    file = open(input_file, 'r')
    line = file.readline()
    while line:
        id_list.append(line)
        line = file.readline()
    file.close()
    return id_list


def get_all_data(in_file, out_file):
    movie_data_dict = {}
    movie_ids = get_movie_ids(in_file)

    id_counter = 0
    counter = 0
    session = requests.Session()

    for id in movie_ids:
        counter += 1

        url = IMDb_query_url(id)

        # start writing your code here
        # get movie data using the session.get(url).json()
        try:
            movie_data = session.get(url).json()
        except:
            continue
        # you may need to handle some exceptions here
        if movie_data['Response'] == 'False':
            continue
        movie_data_dict[id_counter] = movie_data
        id_counter += 1
        
        print 20 * ' ' + '\r',
        print str(len(movie_ids)) + ' / ' + str(counter) + ', real: ' + str(id_counter) + '\r',
        
    # don't change any code below this line
    with open(out_file, 'w+') as f:
        json.dump(movie_data_dict, f)


if __name__ == '__main__':
    # don't change any code below this line
    movie_id_file = r'../IMDbIDCrawler/movie_ids06-15'
    movie_data_file = 'IMDb2006-2015.json'
    get_all_data(movie_id_file, movie_data_file)
