import requests

url = "https://api.nasa.gov/planetary/apod?api_key=Rf5mJWaeBdwJnWyi6zQQYais1qcf3V3U79EjSvSt"

headers = {
	"X-RapidAPI-Host": "https://api.nasa.gov/",
	"X-RapidAPI-Key": "Rf5mJWaeBdwJnWyi6zQQYais1qcf3V3U79EjSvSt"
}

response = requests.request("GET", url, headers=headers)

print(response.text)