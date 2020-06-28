import pycountry
import pprint
import numpy

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
    ('CH', [': ', ': ', ': ', '91 ', ': ', ': ', '93  ', ': ', '96 ']),
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
    ('LU', ['91 ', '93 ', '94 ', '96 ', '97 ', '97 ', '97 ', '93  ', '95 ']),
    ('LV', ['64 ', '69 ', '72 ', '73 ', '76 ', '77  ', '79 ', '82 ', '85 ']),
    ('ME', [': ', '55 ', ': ', ': ', ': ', ': ', '71 ', '72 ', '74 ']),
    ('MK', [': ', '58 ', '65 ', '68 ', '69 ', '75 ', '74 ', '79 ', '82 ']),
    ('MT', ['75 ', '77 ', '78 ', '80 ', '81 ', '81 ', '85 ', '84 ', '86 ']),
    ('NL', ['94 ', '94 ', '95 ', '96 ', '96 ', '97 ', '98 ', '98 ', '98 ']),
    ('NO', ['92 ', '93 ', '94 ', '93 ', '97 ', '97 ', '97 ', '96 ', '98 ']),
    ('PL', ['67 ', '70 ', '72 ', '75 ', '76 ', '80 ', '82 ', '84 ', '87 ']),
    ('PT', ['58 ', '61 ', '62 ', '65 ', '70 ', '74 ', '77 ', '79 ', '81 ']),
    ('RO', ['47 ', '54 ', '58 ', '61  ', '68 ', '72 ', '76 ', '81 ', '84 ']),
    ('RS', [': ', ': ', ': ', ': ', '64 ', ': ', '68 ', '73 ', '80 ']),
    ('SE', ['91 ', '92 ', '93 ', '90 ', '91 ', '94  ', '95 ', '93 ', '96 ']),
    ('SI', ['73 ', '74 ', '76 ', '77 ', '78 ', '78 ', '82 ', '87 ', '89 ']),
    ('SK', ['71 ', '75 ', '78 ', '78 ', '79 ', '81 ', '81 ', '81 ', '82 ']),
    ('TR', [': ', '47 ', '49 ', '60 ', '70 ', '76 ', '81 ', '84 ', '88 ']),
    ('UK', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
    ('XK', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]

NO_DATA = ': '
COVERAGE = 'coverage'
YEAR = 'year'

# Convert iso_code into its country name and returns the string
# If the iso code can not be find in the ISO database, return it as it is
def prepare_key(iso_code):
    if pycountry.countries.get(alpha_2=iso_code) is None:
        return iso_code
    return pycountry.countries.get(alpha_2=iso_code).name

# Create a dictionary for each element from 'coverages' list and return the list of dictionaries
# Each dictionary will contain two key-value pairs: year and coverage
def prepare_value(coverages, years):
    return [
        dict(year = years[ind], coverage = get_integer_value(coverage_)) 
        for ind, coverage_ in enumerate(coverages) 
        if coverage_ != NO_DATA
        ]

def get_integer_value(string_number):
    return int(string_number)

# Create and return a dictionary with country name as key and coverages list of dictionaries as value
def prepare_dataset(raw_data, description):
    # Extract all the years from 'description' tuple and save them in a list
    years = [year.rstrip() for year in description[1]]
    final_data = {prepare_key(line[0]) : prepare_value(line[1], years) for line in raw_data}    
    return final_data

# Create a list of tuples with two values, country name and coverage for the year given as argument
# Return a dictionary with the year as key and the list of tuples as value
def get_year_data(dataset, year):
    final_list = []
    for country, dicts in dataset.items():
        for dictionary in dicts:
            if year in dictionary.values():
                final_list.append((country, dictionary.get(COVERAGE)))
        # final_list = [tuple((country, dictionary['coverage'])) for dictionary in dicts if year in dictionary.values()]
    return {year : final_list}

# Create a list of tuples with two values, year and coverage for the country given as argument
# Return a dictionary with the country name as key and the list of tuples as value
def get_country_data(dataset, country):
    final_list = []
    if country in dataset.keys():
        for dictionary in dataset[country]:
            final_list.append((dictionary.get(YEAR), dictionary.get(COVERAGE)))
    return {country : final_list}

# Create a dictionary from the list of tuples given as argument
# Calculate the average for the values of the dictionary (coverages)
# Return the float result
def perform_average(data):
    return round(numpy.mean(list(dict(data).values())), 2)

pp = pprint.PrettyPrinter(indent=4)

#Prepare dataset
dataset = prepare_dataset(raw_data, description)
pp.pprint(dataset)

# Retrieve data for the year given as parameter
year = '2013'
year_data = get_year_data(dataset, year)
pp.pprint(year_data)

# Retrieve data for the country given as parameter
country = 'Romania'
country_data = get_country_data(dataset, country)
pp.pprint(country_data)

# Calculate coverage average for country_data
print('The average coverage for {} is: {}'.format(country, perform_average(country_data[country])))

# Calculate coverage average for year_data
print('The average coverage for {} is: {}'.format(year, perform_average(year_data[year])))
