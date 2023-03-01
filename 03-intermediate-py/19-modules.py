# A module in py maybe can be a file.py

import sys

print(sys.path) # Where is running the py file



import re # regular expressions 

text = 'My false name is 3052285678, the country code 18 and my lucky number is 13'

result = re.findall('[0-9]+', text)
print(result)


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













