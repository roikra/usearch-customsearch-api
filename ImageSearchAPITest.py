import requests

URL = "https://rapidapi.p.rapidapi.com/api/search/CustomImageSearchAPIV2"
HEADERS = {
    'x-rapidapi-host': "custom-search.p.rapidapi.com",
    'x-rapidapi-key': "Your-X-RapidAPI-Key"
}

query = "taylor swift"
page_number = 1
search_engine_id = "Your-Search-Engine-Id"

query_string = {"q": query,
                "pageNumber": page_number,
                "searchEngineId": search_engine_id}

response = requests.get(URL, headers=HEADERS, params=query_string).json()

print(response)

totalCount = response["totalCount"]

for image in response["value"]:
    url = image["url"]
    name = image["name"]
    title = image["title"]

    provider = image["provider"]["name"]

    image_url = image["url"]
    image_height = image["height"]
    imageWidth = image["width"]

    thumbnail = image["thumbnail"]
    thumbnail_height = image["thumbnailHeight"]
    thumbnail_width = image["thumbnailWidth"]

    print("Url: %s. Title: %s." % (url, name))
