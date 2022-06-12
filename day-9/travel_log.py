# Instructions
# You can see a travel_log which is a List that contains 2 Dictionaries.
#
# Write a function that will work with the following line of code on line 21 to add the entry for Russia to the travel_log.
#
# add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
# You've visited Russia 2 times.
#
# You've been to Moscow and Saint Petersburg.
#
# DO NOT modify the travel_log directly. You need to create a function that modifies it.
#
# Hint
# Look at the function call above to see what the name of the function should be.
#
# The inputs for the function are positional arguments. The order is very important.
#
# Feel free to choose your own parameter names.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
# 🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(new_country_name, times_visited, cities_visited):
    travel_log.append({
        "country": new_country_name,
        "visits": times_visited,
        "cities": cities_visited,
    })

    # Cleaner solution by creating a new named dictionary
    # new_country = {}
    # new_country["country"] = new_country_name
    # new_country["visits"] = times_visited
    # new_country["cities"] = cities_visited
    # travel_log.append(new_country)



# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
