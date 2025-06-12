import requests

def get_wikipedia_summary(topic):
    url = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "query",
        "format": "json",
        "titles": topic,
        "prop": "extracts",
        "exintro": True,
        "explaintext": True,
        "redirects": 1
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        page = next(iter(data['query']['pages'].values()))
        return page.get('extract', 'No summary available.')
    else:
        return "Error fetching data from Wikipedia."

topic = "Artificial Intelligence"
summary = get_wikipedia_summary(topic)
print(summary)
