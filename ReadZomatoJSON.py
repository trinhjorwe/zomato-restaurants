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
with open('Top100DinnersInSydney.json') as json_file:
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

# ANALYSIS SECTION #

# Compute the mean for 'average_cost_for_two'
costs = restaurantTable['average_cost_for_two']
avgCosts = costs.mean()
print("Average Cost for Two = $", avgCosts)


# Compute percentage of values below the mean.
belowCostMean = costs < costs.mean()
numBelowCostMean = belowCostMean.sum()
print("Number of restaurants below the average cost for two mean is = ",numBelowCostMean*100/costs.count(), "%")

# Plot the distribution
sns.set(style="ticks")
x = sns.distplot(list(costs.values), kde=False, bins=25)
x.xaxis.set_minor_locator(plt.MultipleLocator(5))
x.xaxis.set_major_locator(plt.MultipleLocator(20))
x.yaxis.set_major_locator(plt.MultipleLocator(2))
x.yaxis.set_major_locator(plt.MultipleLocator(1))
plt.xlabel("Average cost for two ($)")
plt.ylabel("Number of Places")
plt.title("Average Costs of Sydney's Top 100 Places for Dinner - V1")
plt.show()

# Calculate the median and percentage of values that lie below the value.
medianCost = costs.median()
belowMedian = costs < medianCost
numBelowMedian = belowMedian.sum()
print("The median cost is = $", medianCost)
print("The percentage of values below the median is ", numBelowMedian*100/costs.count(), "%")

# Set the type of the average_cost_for_two column to int so we can run nsmallest() on it.
print("Current types: ", restaurantTable.dtypes)
newRestaurantTable = restaurantTable.astype({'average_cost_for_two': int})
print("Updated type: ", newRestaurantTable.dtypes)

cheapestRestaurants = newRestaurantTable.nsmallest(10,'average_cost_for_two')
print(cheapestRestaurants)

# It looks to be that our result has returned a few restaurants that are in fact cafes which would explain
# why their cost is so low. Looking at their cuisines they have "Ice Cream, Coffee and Tea, Cafe Food". Lets
# take these one's out.

# Create a list of cuisines we do not want, that will be used to filter out the cafes from the dataset
discardCuisines = ['Ice Cream', 'Coffee and Tea', 'Cafe Food']
cuisines = newRestaurantTable['cuisines']

discardRestaurants = cuisines.str.contains('|'.join(discardCuisines))
filteredRestaurants = discardRestaurants == False
print(newRestaurantTable[discardRestaurants])
newRestaurantTable = newRestaurantTable[filteredRestaurants]
print("The size of our updated dataset is ", newRestaurantTable.shape)

# We compute some descriptive statistics again.
costs = newRestaurantTable.average_cost_for_two
averageCost = costs.mean()
medianCost = costs.median()
belowMedian = costs < medianCost
numBelowMedian = belowMedian.sum()
print("The average cost is = $", averageCost)
print("The median cost is = $", medianCost)
print("The percentage of values below the median is ", numBelowMedian*100/costs.count(), "%")

# Plot the distribution again.
sns.set(style="ticks")
x = sns.distplot(list(costs.values), kde=False, bins=25)
x.xaxis.set_minor_locator(plt.MultipleLocator(5))
x.xaxis.set_major_locator(plt.MultipleLocator(20))
x.yaxis.set_major_locator(plt.MultipleLocator(2))
x.yaxis.set_major_locator(plt.MultipleLocator(1))
plt.xlabel("Average cost for two ($)")
plt.ylabel("Number of Places")
plt.title("Average Costs of Sydney's Top 100 Places for Dinner - V2")
plt.show()











