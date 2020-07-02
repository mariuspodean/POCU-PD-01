import pytz
import pprint

pp = pprint.PrettyPrinter(indent=4)
processed_dict = dict()

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
('ER', ['74 ', '76 ', '79 ', '81 ', '83 ', '85 ', '87 ', '89 ', '90 ']),
('EE', ['69 ', '74 ', '79 ', '83 ', '88 ', '86 ', '88 ', '90 ', '90 ']),
('GR', ['50 ', '54 ', '56 ', '66 ', '68 ', '69 ', '71 ', '76 ', '79 ']),
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
('GB', ['83 ', '87 ', '88 ', '90 ', '91 ', '93 ', '94 ', '95 ', '96 ']),
('ZW', [': ', ': ', ': ', ': ', ': ', ': ', '89 ', '93 ', '93 ']),
]

# Function to get the country name from the country code
def get_country_name(country_code):
    name = pytz.country_names[country_code]
    return name

# Function to remove the non-numeric characters
def process_number(number):
    string_type= type(number)
    return string_type().join(filter(string_type.isdigit, number))

# Function to process the raw data input
def process_data(description, data):
    years = description[1] 
    output_dict = dict()

    for item in data:
        output_dict[get_country_name(item[0])] = []
        for idx, number in enumerate(item[1]):
            fixed_data = process_number(number)
            if not fixed_data:
                continue
            else:
                output_dict[get_country_name(item[0])].append({'year': process_number(years[idx]), 'coverage': int(fixed_data)})   
    
    pp.pprint(output_dict)
    return output_dict

# Function to get data for all countries for a specific year
def get_year_data(dataset, year):
    coverage_tuple = ()
    coverage_list = []
    year_data = dict()

    for key in dataset:
        for item in dataset[key]:
            if(item["year"] == year):
                coverage_tuple = (key, item["coverage"])
                coverage_list.append(coverage_tuple)

    if(len(coverage_list) > 0):
        year_data[year] = coverage_list
    else:
        print("No information available for the selected year.")
        return "No information available for the selected year."
        
    print(year_data)
    return year_data

# Function to get data for a country for a specific year
def get_country_data(dataset, country):
    coverage_tuple = ()
    coverage_list = []
    country_data = dict()

    try:
        if(dataset[country]):
            for item in dataset[country]:
                coverage_tuple = (item["year"], item["coverage"])
                coverage_list.append(coverage_tuple)

        if(len(coverage_list) > 0):
            country_data[country] = coverage_list

        print(country_data)
        return country_data

    except KeyError:
        print("No Information available for that country")
        return "No Information available for that country"

# Function to get the average from year or country data provided by above functions
def get_average(iterable):

    average = 0
    try:
        for key in iterable:
            for item in iterable[key]:
                average += item[1]
            average = average / len(iterable[key])
        print(average)
        return average

    except TypeError:
        print("Invalid input.")
        return "Invalid input."
        

processed_dict = process_data(description, raw_data)
get_year_data(processed_dict, "2018")
get_country_data(processed_dict, "Romania")
get_average(get_year_data(processed_dict, "2011"))
get_average(get_country_data(processed_dict, "Slovenia"))
