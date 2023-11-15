input_filename = "country_info.txt"

country_list = []

with open(input_filename, encoding='utf-8') as country_file:
    country_file.readline() 
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, code3, dialing, timezone, currency = data
        country_dict = {
            'name': country,
            'capital': capital,
            'code': code,
            'code3': code3,
            'dialing': dialing,
            'timezone': timezone,
            'currency': currency
        }
        country_list.append(country_dict)

user_input = input("Enter a country name: ")
for country_dict in country_list:
    if country_dict['name'].lower() == user_input.lower():
        print(f"The capital city is {country_dict['capital']}")
        break
else:
    print("Country not found.")
    