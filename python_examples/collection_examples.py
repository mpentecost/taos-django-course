"""Useful patterns when working with collections"""

# our list of cities
cities = ["San Francisco", "New York", "Chicago", "Miami", "Houston", "Anchorage"]

# typical print iteration
for city in cities:
    print(city)

# while loop w/ pop
while cities:
    city = cities.pop()  # mutates the list
    print(city)

# in a list comprehension
cities = ["San Francisco", "New York", "Chicago", "Miami", "Houston", "Anchorage"]
[print(city) for city in cities]

# a list of city dictionairies
cities = [
    {"name": "San Francisco", "population": 870000},
    {"name": "New York", "population": 8500000},
    {"name": "Chicago", "population": 2700000},
    {"name": "Miami", "population": 460000},
    {"name": "Houston", "population": 23000000},
    {"name": "Anchorage", "population": 294000}
]

# let's create some new dicts from this data
# let's make a new dict that only includes cities that have a population of over 500,000

# the for loop way
new_cities = []
for city in cities:
    if city.get("population") > 500000:
        new_cities.append(city)

print(new_cities)

# the list comprehension way
new_cities = [city for city in cities if city.get("population") > 500000]
print(new_cities)

# we can also make a function that returns a boolean
def is_filtered_city(city):
    if city.get("population") > 500000:
        return True
    return False # base case

new_cities = [city for city in cities if is_filtered_city(city)]
print(new_cities)

# Lets now add a new field to each dict that holds a boolean if the city has > 500000
# for this exercise let's construct a new dict for each city
#  in practice we would probably mutate this dict but let's use this as an exercise in 
# constructing dicts from other dicts

# the for loop way
new_cities = []
for city in cities:
    new_city_dict = {
        "name": city.get("name"),
        "population": city.get("population")
    }
    if city.get("population") > 500000:
        new_city_dict["is_over_500k"] = True
    else:
        new_city_dict["is_over_500k"] = False
    
    new_cities.append(new_city_dict)

print(new_cities)

# the list comprehsion way
def is_over_500k(city):
    """Checks if the city is over 500k"""
    if city.get("population") > 500000:
        return True
    return False

new_cities = [
    {
        "name": city.get("name"),
        "population": city.get("population"),
        "is_over_500k": is_over_500k(city)
    } for city in cities
]

print(new_cities)

# What if we want to make a new dict, where we have the structrue like this
# {
#    "city name":{"population": 500000, "is_over_500k": True},
# }

# For loop
new_cities = {}
for city in cities:
    key = city.get("name")
    new_dict = {
        "population": city.get("population")
    }
    if city.get("population") > 500000:
        new_dict["is_over_500k"] = True
    else:
        new_dict["is_over_500k"] = False
    
    new_cities[key] = new_dict

print(new_cities)

# Dict comprehension way w/ function
new_cities = {
    city.get("name"): {
        "population": city.get("population"), 
        "is_over_500k": is_over_500k(city)
        } for city in cities
}
print(new_cities)
