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
def add_new_country(country_visited,visited,cities_visited):
    new_country = {}
    new_country['country'] = country_visited
    new_country['visits'] = visited
    new_country['cities'] = cities_visited
    travel_log.append(new_country)
    print(travel_log)

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

