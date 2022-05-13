import requests

url = "https://football98.p.rapidapi.com/liga/news"

headers = {
	"X-RapidAPI-Host": "football98.p.rapidapi.com",
	"X-RapidAPI-Key": "90b2f674d3msh78662c0e6f7a39bp19876fjsn88de7b119c81"
}

response = requests.request("GET", url, headers=headers)

print(response.text)