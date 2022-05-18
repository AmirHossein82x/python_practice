cities_in_f = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago': 50}
cities_in_c = {key: (value - 32) for (key, value) in cities_in_f.items()}
print('cities_in_c: %s' %cities_in_c)
print('------------------------------------------------\n')

weather = {'New York':'snowing', 'Boston':'sunny', 'Los Angeles':'sunny', 'Chicago': 'cloudy'}
sunny_weather = { key: value for key, value in weather.items() if value == 'sunny'}
print('sunny_weather: %s' %sunny_weather)
print('------------------------------------------------\n')

cities = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago': 50}
cities_situation = {key:('cold' if value <= 50 else'warm') for key, value in cities.items()}
print('cities_situation: %s' %cities_situation)
print('------------------------------------------------\n')

def check_weather(value):

    if value <= 50:
        return 'cold'
    return 'warm'

cities = {'New York':32, 'Boston':75, 'Los Angeles':100, 'Chicago': 50}
cities_situation_new = {key: check_weather(value) for key, value in cities.items()}
print('cities_situation_new: %s' %cities_situation_new)
print('------------------------------------------------\n')