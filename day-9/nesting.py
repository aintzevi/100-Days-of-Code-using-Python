capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}


# Nesting list in dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Munich"],
}


# Nesting dictionary in dictionary

travel_log_dict_in_dict = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12},
    "Germany": {
        "cities_visited": ["Berlin", "Munich"],
        "total_visits": 20},
}

# Nesting dictionary in list
travel_log_dict_in_list = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
{
        "country": "Germany",
        "cities_visited": ["Berlin", "Munich"],
        "total_visits": 20
    },
]


travel_log_visit_per_city = [
    {
        "country": "France",
        "cities_visited": {
            "Paris": 2,
            "Lille": 1,
            "Dijon": 3,
        }
    },
    {
        "country": "Germany",
        "cities_visited": {
            "Berlin": 2,
            "Munich": 5,
        }
    },
]

