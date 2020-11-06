import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)

req = requests.get('https://www.google.com')



print(req)
