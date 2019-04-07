
# Zomato Restaurants
What is the average price of having dinner at one of Sydney's Top 100 restaurants? Have a guess before you find out the answer below!

We will go through an example to answer:
1. How to extract data using the Zomato API
2. How to transform it into a consumable and readable format
3. How to make sense of the data (by applying some descriptive statistics)

### What is Zomato?
It is a platform that holds information on over 1 million restaurants globally, including ratings, reviews and many more. It is a place that I visit before checking out a new place to eat, or even after going to one I've tried (just to see what everyone else thinks of it).

### The Zomato API
To get started with the Zomato API, you first need to [request an API key](https://developers.zomato.com/api?lang=id). Once that's done head on over to the _Documentations_ section and have a look at all the data points you can begin to source!

Let's have a look at what one of the functions returns

#### /cities function
This function retrieves the [city details](https://developers.zomato.com/documentation#!/common/cities). Let's put in your API key into _user-key_, and *Sydney* for parameter _q_. We get the following:

        {
          "location_suggestions": [
            {
              "id": 260,
              "name": "Sydney, NSW",
              "country_id": 14,
              "country_name": "Australia",
              "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_14.png",
              "should_experiment_with": 0,
              "discovery_enabled": 0,
              "has_new_ad_format": 1,
              "is_state": 0,
              "state_id": 128,
              "state_name": "New South Wales",
              "state_code": "NSW"
            },
            {
              "id": 3171,
              "name": "Sydney, Atlantic Provinces, NS",
              "country_id": 37,
              "country_name": "Canada",
              "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_37.png",
              "should_experiment_with": 0,
              "discovery_enabled": 0,
              "has_new_ad_format": 0,
              "is_state": 0,
              "state_id": 144,
              "state_name": "Nova Scotia",
              "state_code": "NS"
            },
            {
              "id": 3169,
              "name": "North Sydney, NS",
              "country_id": 37,
              "country_name": "Canada",
              "country_flag_url": "https://b.zmtcdn.com/images/countries/flags/country_37.png",
              "should_experiment_with": 0,
              "discovery_enabled": 0,
              "has_new_ad_format": 0,
              "is_state": 0,
              "state_id": 144,
              "state_name": "Nova Scotia",
              "state_code": "NS"
            }
          ],
          "status": "success",
          "has_more": 0,
          "has_total": 0
        }
        

## Example: Top 100 places for dinner in Sydney
So with this example we're trying to find what is the average price to eat dinner in one at Sydney's top 100 places. Before we answer this question, we should think about what data points we need.
1. By what means are we ranking the Top 100? We will be ranking it by the restaurant's _rating_
2. Average price? We will need some cost value.

# 1. How to extract data using the Zomato API
## 

## Example: Restaurants in Sydney
This project primarily utlises the _search_ function in the Zomato library to obtain the Top 100 restaurants in Sydney. I will be going through the following:
