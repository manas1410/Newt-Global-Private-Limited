import requests

api_key = "db6b500738ce49559a58ca799f377147"
url = (("https://newsapi.org/v2/everything?q=tesla&"\
       "from=2023-11-21&sortBy=publishedAt&apiKey=") +
       api_key)

request = requests.get(url)
content = request.text
print(content)