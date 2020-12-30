import re

# phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# matchObject = phoneNumRegex.search('My phone number is 773-312-1849.')

# print(matchObject.group())

# Regex with groups
# phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

# matchObject = phoneNumRegex.search('My phone number is 773-312-1849.')
# print(matchObject.groups())

# Multiple matches with pipe
heroRegex = re.compile(r'Batman|Carl')
matchObject1 = heroRegex.search('I am watching a shows that star Batman and Carl')
print(matchObject1.group())

# p.155