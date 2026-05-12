from randomisation_lists_loops import nested_lists

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"]
}

#print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C" , "D"]]
print(nested_list[2])
print(nested_list[2][1])

travel_log_2 = {
    "France": {
        "numbers visited" : 2,
        "cities_visited" : ["Paris", "Lille", "Dijon"]
    },
    "Germany": ["Berlin", "Stuttgart"]
}
#print Lille again
print(travel_log_2["France"]["cities_visited"][1])