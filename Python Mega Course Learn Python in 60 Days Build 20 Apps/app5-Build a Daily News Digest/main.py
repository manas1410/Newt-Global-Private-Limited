import requests
from send_email import send_email


topic = "tesla"
api_key = "890603a55bfa47048e4490069ebee18c"
url = f"https://newsapi.org/v2/everything?q={topic}&" \
      "sortBy=publishedAt&apiKey=" \
      f"{api_key}&language=en"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + body + article["title"] + "\n" + \
        str(article["description"]) + \
        "\n" + article["url"]  +2*"\n"

body = body.encode("utf-8")
send_email(message=body)