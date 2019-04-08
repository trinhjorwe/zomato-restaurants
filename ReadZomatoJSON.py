import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

desired_width=320
pd.set_option('display.max_columns', 10)
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)


# Read JSON file of restaurants
with open('Top100SydneyDinners.json') as json_file:
    allRestaurants = json.load(json_file)

# Create columns for DataFrame
columns = ["name", "locality", "city", "cuisines", "average_cost_for_two", 'aggregate_rating', 'rating_text', 'votes']

# Create empty DataFrame with above columns
restaurantTable = pd.DataFrame(columns=columns)


# This function loops through each restaurant dictionary in allRestaurants, grabs values for
# each restaurant which is then grouped into a Series that is appended to the DataFrame
for restaurantSet in allRestaurants:
    restaurants = restaurantSet['restaurants']
    for restaurant in restaurants:
        singleRow = [restaurant['restaurant']['name'],
               restaurant['restaurant']['location']['locality'],
               restaurant['restaurant']['location']['city'],
               restaurant['restaurant']['cuisines'],
               restaurant['restaurant']['average_cost_for_two'],
               restaurant['restaurant']['user_rating']['aggregate_rating'],
               restaurant['restaurant']['user_rating']['rating_text'],
               restaurant['restaurant']['user_rating']['votes']]
        newRow = pd.Series(singleRow, index=columns)
        restaurantTable = restaurantTable.append(newRow, ignore_index=True)

restaurantTable.index.name = 'id'

print(restaurantTable)

"""
Analysis section: We can now find out what the average cost for
for two people to have dinner at Sydney's Top 100 places.
"""

# Grab the 'average_cost_for_two' column
costs = restaurantTable['average_cost_for_two']
avgCosts = costs.mean()
print("Average Cost for Two = $",avgCosts)

# Is the average the best way to measure central tendency of
# the Top 100 Places to have Dinner in Sydney?

# First, lets have a quick look at how many restaurants are below the mean.
belowCostMean = costs < costs.mean()
numBelowCostMean = belowCostMean.sum()
print("Number of restaurants below the average cost for two mean is = ",numBelowCostMean)

# Let's look at the distribution with a histogram plot
sns.set(style="ticks")
x = sns.distplot(list(costs.values), kde=False, bins=25)
x.xaxis.set_minor_locator(plt.MultipleLocator(5))
x.xaxis.set_major_locator(plt.MultipleLocator(20))
x.yaxis.set_major_locator(plt.MultipleLocator(2))
x.yaxis.set_major_locator(plt.MultipleLocator(1))
plt.xlabel("Average cost for two ($)")
plt.ylabel("Number of Places")
plt.title("Average Costs of Sydney's Top 100 Places for Dinner")
plt.show()












