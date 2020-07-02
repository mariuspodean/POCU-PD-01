import pycountry
import statistics 

description=('Country', ['2011 ','2012 ','2013 ','2014 ','2015 ','2016 ','2017 ','2018 ','2019 '])

raw_data=[('AL', [': ',': ',': ',': ',': ',': ',': ','84 ',': ']),
('AT', ['75 ','79 ','81 ','81 ','82 ','85 ','89 ','89 ','90 ']),
('BA', [': ',': ',': ',': ',': ',': ',': ','69 ','72 ']),
('BE', ['77 ','78 ','80 ','83 ','82 ','85 ','86 ','87 ','90 ']),
('BG', ['45 ','51 ','54 ','57 ','59 ','64 ','67 ','72 ','75 ']),
('CH', [': ',': ',': ','91 ',': ',': ','93 b',': ','96 ']),
('CY', ['57 ','62 ','65 ','69 ','71 ','74 ','79 ','86 ','90 ']),
('CZ', ['67 ','73 ','73 ','78 ','79 ','82 ','83 ','86 ','87 ']),
('DE', ['83 ','85 ','88 ','89 ','90 ','92 ','93 ','94 ','95 ']),
('DK', ['90 ','92 ','93 ','93 ','92 ','94 ','97 ','93 ','95 ']),
('EA', ['74 ','76 ','79 ','81 ','83 ','85 ','87 ','89 ','90 ']),
('EE', ['69 ','74 ','79 ','83 ','88 ','86 ','88 ','90 ','90 ']),
('EL', ['50 ','54 ','56 ','66 ','68 ','69 ','71 ','76 ','79 ']),
('ES', ['63 ','67 ','70 ','74 ','79 ','82 ','83 ','86 ','91 ']),
('FI', ['84 ','87 ','89 ','90 ','90 ','92 ','94 ','94 ','94 ']),
('FR', ['76 ','80 ','82 ','83 ','83 ','86 ','86 ','89 ','90 ']),
('HR', ['61 ','66 ','65 ','68 ','77 ','77 ','76 ','82 ','81 ']),
('HU', ['63 ','67 ','70 ','73 ','76 ','79 ','82 ','83 ','86 ']),
('IE', ['78 ','81 ','82 ','82 ','85 ','87 ','88 ','89 ','91 ']),
('IS', ['93 ','95 ','96 ','96 ',': ',': ','98 ','99 ','98 ']),
('IT', ['62 ','63 ','69 ','73 ','75 ','79 ','81 ','84 ','85 ']),
('LT', ['60 ','60 ','65 ','66 ','68 ','72 ','75 ','78 ','82 ']),
('LU', ['91 ','93 ','94 ','96 ','97 ','97 ','97 ','93 b','95 ']),
('LV', ['64 ','69 ','72 ','73 ','76 ','77 b','79 ','82 ','85 ']),
('ME', [': ','55 ',': ',': ',': ',': ','71 ','72 ','74 ']),
('MK', [': ','58 ','65 ','68 ','69 ','75 ','74 ','79 ','82 ']),
('MT', ['75 ','77 ','78 ','80 ','81 ','81 ','85 ','84 ','86 ']),
('NL', ['94 ','94 ','95 ','96 ','96 ','97 ','98 ','98 ','98 ']),
('NO', ['92 ','93 ','94 ','93 ','97 ','97 ','97 ','96 ','98 ']),
('PL', ['67 ','70 ','72 ','75 ','76 ','80 ','82 ','84 ','87 ']),
('PT', ['58 ','61 ','62 ','65 ','70 ','74 ','77 ','79 ','81 ']),
('RO', ['47 ','54 ','58 ','61 b','68 ','72 ','76 ','81 ','84 ']),
('RS', [': ',': ',': ',': ','64 ',': ','68 ','73 ','80 ']),
('SE', ['91 ','92 ','93 ','90 ','91 ','94 b','95 ','93 ','96 ']),
('SI', ['73 ','74 ','76 ','77 ','78 ','78 ','82 ','87 ','89 ']),
('SK', ['71 ','75 ','78 ','78 ','79 ','81 ','81 ','81 ','82 ']),
('TR', [': ','47 ','49 ','60 ','70 ','76 ','81 ','84 ','88 ']),
('UK', ['83 ','87 ','88 ','90 ','91 ','93 ','94 ','95 ','96 ']),
('XK', [': ',': ',': ',': ',': ',': ','89 ','93 ','93 '])]



def year_sort(e):
  return e['year']

def format_data(arr):
    if isinstance(arr, list) == False or len(arr) == 0:
        return False

    output = {}
    for data in arr:
        country = pycountry.countries.get(alpha_2 = data[0])
        if country is not None:
            output[str(country.name)] = []
            for index,value in enumerate(data[1]):
                try:
                    int_value = int(value)
            
                    output[str(country.name)].append( dict(year = description[1][index].strip(), coverage = int_value))
                    output[str(country.name)].sort(reverse=True, key=year_sort)
                except ValueError:
                    continue
    
    return output

def get_year_data(dataset, year):
    if isinstance(dataset, dict) == False or len(dataset) == 0:
        return False
    if isinstance(year, str) == False:
        return False
    output = {}
    output[year] = []
    for country,value in dataset.items():
        coverage = [d['coverage'] for d in value if d['year']== year]
        if len(coverage) > 0:
            output[year].append((country, coverage[0]))

    return output


def get_country_data(dataset, country):
    if isinstance(dataset, dict) == False or len(dataset) == 0:
        return False
    if isinstance(country, str) == False:
        return False
    output = {}
    output[country] = []
    for data in dataset[country]:
        output[country].append((data['year'],data['coverage']))

    return output


def perform_average(dataset):
    if isinstance(dataset, list) == False or len(dataset) == 0:
        return False
    values = [tpl[1] for tpl in dataset]
    return statistics.mean(values)
