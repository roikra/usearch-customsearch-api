# Using Python to call the custom Search APIs:
  - ##### Web Search API
  - #####  News API
  - ##### Image API
  
## Web Search API
```sh
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
```

## News Search API
```sh
import requests

URL = "https://rapidapi.p.rapidapi.com/api/search/CustomNewsSearchAPIV2"
HEADERS = {
    'x-rapidapi-host': "custom-search.p.rapidapi.com",
    "x-rapidapi-key": "Your-X-RapidAPI-Key"
}

query = "taylor swift"
page_number = 1
search_engine_id = "Your-Search-Engine-Id"
with_thumbnails = True
to_published_date = ""
from_published_date = ""

querystring = {"q": query,
               "pageNumber": page_number,
               "searchEngineId": search_engine_id,
               "withThumbnails": with_thumbnails,
               "fromPublishedDate": to_published_date,
               "toPublishedDate": from_published_date}

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

    image_url = web_page["image"]["url"]
    image_height = web_page["image"]["height"]
    image_width = web_page["image"]["width"]

    thumbnail = web_page["image"]["thumbnail"]
    thumbnail_height = web_page["image"]["thumbnailHeight"]
    thumbnail_width = web_page["image"]["thumbnailWidth"]

    print("Url: {}. Title: {}. Published Date: {}.".format(url, title, date_published))
```

## Image Search API ##
```sh
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

```



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

