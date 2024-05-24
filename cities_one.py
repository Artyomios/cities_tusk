import json
import yaml
from lib_cities import (remove_duplicate_cities,
                        megapolises,
                        sorted_fouded,
                        sorted_population,
                        new_city)

with open("cities.json", "r") as read_file:
    data = json.load(read_file)


while True:
    x = input('do you want to append city?(yes/no): ')
    if x == "yes":
        c_id, c_name, c_founded, c_population = (input('input id: '),
                                                 input('name: '),
                                                 input('year of founding: '),
                                                 input('population: '))
        data['cities'] = new_city(data['cities'], c_id, c_name, c_founded, c_population)
    else:
        break

x = input('Display a list of cities without duplicates?(yes/no):')
if x == "yes":
    data['cities'] = remove_duplicate_cities(data['cities'])

x = input('Remove cities with a population more than 1 million?(yes/no):')
if x == "yes":
    data['cities'] = megapolises(data['cities'])

x = input('Sort cities by year of founding?(yes/no):')
if x == "yes":
    data['cities'] = sorted_fouded(data['cities'])

x = input('Sort cities by population?(yes/no):')
if x == "yes":
    data['cities'] = sorted_population(data['cities'])

print(json.dumps(sorted_fouded(data['cities']), indent=4, ensure_ascii=False))

with open('test.yaml', 'w') as fw:
    data1 = yaml.safe_dump(data, fw, sort_keys=False,
                     default_flow_style=False, explicit_start=True)
