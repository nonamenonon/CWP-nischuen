#!/usr/bin/env python

def famous_births(people):
    sorted_keys = sorted(people, key=lambda key: people[key]["date_of_birth"])
    for key in sorted_keys:
        name = people[key]["name"]
        year = people[key]["date_of_birth"]
        print(name + " is a great scientist born in " + year + ".")

women_scientists = {
    "ada": {"name": "Ada Lovelace", "date_of_birth": "1815"},
    "cecilia": {"name": "Cecila Payne", "date_of_birth": "1900"},
    "lise": {"name": "Lise Meitner", "date_of_birth": "1878"},
    "grace": {"name": "Grace Hopper", "date_of_birth": "1906"}
}
famous_births(women_scientists)