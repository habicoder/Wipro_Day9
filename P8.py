# group() returns the substring that was matched by the RE. 
# start() and end() return the starting and ending index of the match.
 
# span() returns both start and end indexes in a single tuple.
# Since the match() method only checks if the RE matches at the
# start of a string, start() will always be zero.


import re
 
# getting the match of the string

search_pattern = re.search('\d+',

						'1234')
 
""" 

d: stands for integer

+: means a consecutive set of 

characters satisfying a condition. 

Hence d+ will match consecutive 

integer string 

"""
 
print(search_pattern.string)
 
print(search_pattern.start())
 
print(search_pattern.end())
