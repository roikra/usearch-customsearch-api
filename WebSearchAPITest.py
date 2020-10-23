import requests

URL = "https://rapidapi.p.rapidapi.com/api/search/CustomWebSearchAPIV2"
HEADERS = {
    'x-rapidapi-host': "custom-search.p.rapidapi.com",
    'x-rapidapi-key': "Your-X-RapidAPI-Key"
}

query = "taylor swift"
page_number = 1
search_engine_id = "Your-Search-Engine-Id"

querystring = {"q": query,
               "pageNumber": page_number,
               "searchEngineId": search_engine_id}

response = requests.get(URL, headers=HEADERS, params=querystring).json()

print(response)

total_count = response["totalCount"]

for web_page in response["value"]:

    url = web_page["url"]
    title = web_page["title"]
    description = web_page["description"]
    body = web_page["body"]
    date_published = web_page["datePublished"]
    language = web_page["language"]
    is_safe = web_page["isSafe"]
    provider = web_page["provider"]["name"]

    print("Url: {}. Title: {}.".format(url, title))