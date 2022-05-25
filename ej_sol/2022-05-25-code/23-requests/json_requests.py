import pprint
import requests
from   requests.models import Response

# Make a GET Request
url:      str      = 'https://animechan.vercel.app/api/random'
response: Response = requests.get(url)

# Print response
print(response)

# Print json content
pprint.pprint(response.json())






