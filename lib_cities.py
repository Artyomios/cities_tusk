
def remove_duplicate_cities(cities):
    seen_names = set()
    unique_cities = []
    for city in cities:
        if city["name"] not in seen_names:
            unique_cities.append(city)
            seen_names.add(city["name"])
    return unique_cities
def megapolises(cities):
    mega_cities = []
    for city in cities:
        if city['population'] >= 1000000:
            mega_cities.append(city)
    return mega_cities
def sorted_fouded(cities):
    sorted_data = sorted(cities, key=lambda city: city['founded'])
    return sorted_data

def sorted_population(cities):
    sorted_data = sorted(cities, key=lambda city: city['population'])
    return sorted_data

def new_city(cities, city_id, city_name, city_founded, city_population):
    cities.append({ "id": int(city_id),
                    "name": city_name,
                    "founded": int(city_founded),
                    "population": int(city_population)  })
    return cities
