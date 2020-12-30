import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

matchObject = phoneNumRegex.search('My phone number is 773-312-1849.')

print(matchObject.group())