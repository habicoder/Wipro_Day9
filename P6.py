import re

s = 'Readability counts.'
pattern = r'[aeiou]'
matches = re.finditer(pattern, s)

for match in matches:
    print(match)
