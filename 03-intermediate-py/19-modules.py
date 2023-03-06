# A module in py maybe can be a file.py

import sys

print(sys.path) # Where is running the py file


import re # regular expressions 

text = 'My false name is 3052285678, the country code 18 and my lucky number is 13'

countries = [{'Rank': '36', 'CCA3': 'AFG', 'Country/Territory': 'Afghanistan', 'Capital': 'Kabul', 'Continent': 'Asia', '2022 Population': '41128771', '2020 Population': '38972230', '2015 Population': '33753499', '2010 Population': '28189672', '2000 Population': '19542982', '1990 Population': '10694796', '1980 Population': '12486631', '1970 Population': '10752971', 'Area (km²)': '652230', 'Density (per km²)': '63.0587', 'Growth Rate': '1.0257', 'World Population Percentage': '0.52'}]

r = re.compile(".*tion")

result_population = list(map(lambda item : item[r.match], countries))
print("RESULT =>", result_population)


# result = re.findall('[0-9a-z]+', text)
# print(result)


import time #hours and dates

timestamp = time.time()
local = time.localtime()

# Standard for dates
result_time  = time.asctime()
print(timestamp,result_time) # 1677706232.6431873 Wed Mar  1 16:30:32 2023

import collections # Manipulate lists

numbers = [1,1,2,3,1,2,3,2,1,2,3,1,1,3,1,2,3,1]
counter = collections.Counter(numbers)
print(counter)













