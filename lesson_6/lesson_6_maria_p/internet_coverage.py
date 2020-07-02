import pycountry
import pprint

pp = pprint.PrettyPrinter(indent = 4)

description = ('Country', [
    '2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ',
    '2019 '
])

raw_data = [
    ('AL', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '84 ', ': ']),
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('BE', ['77 ', '78 ', '80 ', '83 ', '82 ', '85 ', '86 ', '87 ', '90 ']),
    ('BG', ['45 ', '51 ', '54 ', '57 ', '59 ', '64 ', '67 ', '72 ', '75 ']),
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93 b', ': ', '96 ']),
    ('CY', ['57 ', '62 ', '65 ', '69 ', '71 ', '74 ', '79 ', '86 ', '90 ']),
    ('CZ', ['67 ', '73 ', '73 ', '78 ', '79 ', '82 ', '83 ', '86 ', '87 ']),
    ('DE', ['83 ', '85 ', '88 ', '89 ', '90 ', '92 ', '93 ', '94 ', '95 ']),
    ('DK', ['90 ', '92 ', '93 ', '93 ', '92 ', '94 ', '97 ', '93 ', '95 ']),
    ('EA', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
    ('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
    ('EL', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
    ('ES', ['63 ', '67 ', '70 ', '74 ', '79 ', '82 ', '83 ', '86 ', '91 ']),
    ('FI', ['84 ', '87 ', '89 ', '90 ', '90 ', '92 ', '94 ', '94 ', '94 ']),
    ('FR', ['76 ', '80 ', '82 ', '83 ', '83 ', '86 ', '86 ', '89 ', '90 ']),
    ('HR', ['61 ', '66 ', '65 ', '68 ', '77 ', '77 ', '76 ', '82 ', '81 ']),
    ('HU', ['63 ', '67 ', '70 ', '73 ', '76 ', '79 ', '82 ', '83 ', '86 ']),
    ('IE', ['78 ', '81 ', '82 ', '82 ', '85 ', '87 ', '88 ', '89 ', '91 ']),
    ('IS', ['93 ', '95 ', '96 ', '96 ', ': ', ': ', '98 ', '99 ', '98 ']),
    ('IT', ['62 ', '63 ', '69 ', '73 ', '75 ', '79 ', '81 ', '84 ', '85 ']),
    ('LT', ['60 ', '60 ', '65 ', '66 ', '68 ', '72 ', '75 ', '78 ', '82 ']),
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93 b', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77 b', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61 b', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94 b', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]

# Prepare dataset
def prepare_dataset(raw_data, description):
    description = format_description(description)
    raw_data = format_raw_data(raw_data)
    
    dataset = {}

    for entry in raw_data:
        country = get_country_name(entry[0])
        dataset[country] = []
        i=0
        for coverage in entry[1]:
            dataset[country].append(dict(year = description[i], coverage = coverage))
            i +=1

    return dataset

# Retrieve data for each year
def get_year_data(dataset, year):
    year_data = [(country_name, entry.get('coverage')) for (country_name, country_data) in dataset.items() for entry in country_data if entry.get('year') == year]

    return {year: year_data}


# Retrieve data for each country
def get_country_data(dataset, country_name):
    country_data = [(entry.get('year'), entry.get('coverage')) for entry in dataset.get(country_name)]
    country_data.reverse()

    return {country_name: country_data}

# Perform average
def perform_average(data):
    coverage_values = [item[1] for key in data for item in data[key]]
    average = sum(filter(None, coverage_values))/len(coverage_values)
 
    return average


# Format description
def format_description(description):
    description = [year.strip() for year in description[1]]
    return description

#Format raw_data
def format_raw_data(raw_data):
    raw_data = get_list_of_lists(raw_data)
    
    i=0
    for i in range(len(raw_data)):
        raw_data[i][0] = get_country_name(raw_data[i][0])
        i +=1

    for entry in raw_data:
        j = 0
        for coverage in entry[1]:
            entry[1][j] = remove_chars_from_text(entry[1][j])
            entry[1][j] = convert_string_to_int_or_None(entry[1][j])
            j += 1

    raw_data = get_list_of_tuples(raw_data)

    return raw_data

# Replace country iso code with country name
def get_country_name(country_iso):
    country_mapping = {'EA': 'Ceuta, Melilla', 'EL': 'Greece', 'UK': 'United Kingdom', 'XK': 'Kosovo'}
    country_iso_exceptions = [key for key in country_mapping]
   
    if country_iso in country_iso_exceptions:
        country_name = country_mapping[country_iso]
    else:
        country_details = pycountry.countries.get(alpha_2=country_iso)
        if country_details != None:
            country_name = country_details.name
        else:
            country_name = country_iso
                    
    return country_name

# Transform list of tuples to list of lists
def get_list_of_lists(list_of_tuples):
    list_of_lists = []
    for tuple in list_of_tuples:
        list_of_lists.append(list(tuple))

    return list_of_lists

# Transform list of lists in list of tuples
def get_list_of_tuples(list_of_lists):
    list_of_tuples = []
    for list in list_of_lists:
        list_of_tuples.append(tuple(list))

    return list_of_tuples


# Remove "b", " " and ":" from strings
def remove_chars_from_text(text):
    text = text.strip(' b:')
    return text

# Convert empty string to none
def convert_string_to_int_or_None(a):
    if a != '':
        return int(a)
    else:
        return None


# Prepare and print dataset
dataset = prepare_dataset(raw_data, description)
pp.pprint(dataset)

# Retrive and print data for an year
year_data = get_year_data(dataset, '2015')

pp.pprint(year_data)

# Retrive and print data for a country
country_data = get_country_data(dataset, 'Austria')

pp.pprint(country_data)

# Calculate and print average for an year
year_data = get_year_data(dataset, '2014')
year_average = perform_average(year_data)

print('Year average is', year_average)

# Calculate and print average for an year
country_data = get_country_data(dataset, 'Austria')
country_average = perform_average(country_data)

print('Country average is', country_average)

