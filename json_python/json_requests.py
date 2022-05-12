import requests
from requests.models import Response


# cuando un servidor ofrece ditecciones http que devuelven json estas direcciones se llaman una api
# API : aplication programming interfaces


# make a get request

url: str = 'https://animechan.vercel.app/api/random'

response: Response = requests.get(url)

# print response

print(response)