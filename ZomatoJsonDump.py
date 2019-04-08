from pyzomato import Pyzomato
import json

p = Pyzomato('<insert your API key here>')

"""
As the search function in Zomato API only returns a maximum of 20 results per call, we'll need to
five times. 
"""

# Create an empty list, that will be used to append each dictionary returned.
restaurantList = []

# Create a loop that iterates five times starting from 0th record and increases by increments of 20
for a in range(0,100,20):
    restaurants = p.search(lat=-33.865,lon=151.2094,
                           count=20,
                           sort='rating',
                           order='desc',
                           category=10,
                           start=a)
    print(a)
    restaurantList.append(restaurants)

# Write list of dictionaries to a json file
with open('Top100SydneyDinners.json', 'w') as fp:
    json.dump(restaurantList, fp)



