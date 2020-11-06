import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')

# substitute out group 2 and 3
subbed_urls = pattern.sub(r'\2\3',urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match)

print(subbed_urls)