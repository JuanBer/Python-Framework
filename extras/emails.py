import re
from re import match

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

pattern = re.compile(r'[A-Za-z0-1.-]+@[A-Za-z-]+\.(com|edu|net)')

matches = pattern.finditer(emails)

for match in matches:
    print(match)