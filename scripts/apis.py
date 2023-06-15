import requests

def get_artist_info(artist_name):
    url = f"https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts%7Cpageimages&exintro&explaintext&piprop=original&titles={artist_name}"
    try:
        response = requests.get(url)
        data = response.json()
        pages = data["query"]["pages"]
        page_id = list(pages.keys())[0]
        summary = pages[page_id]["extract"]
        image_url = pages[page_id]["original"]["source"]
    except Exception as e:
        summary = "quote can not be retrieved at the moment"
        image_url = None
    return summary, image_url

def get_random_quote_by_person(person_name):
    url = "https://api.forismatic.com/api/1.0/"
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "en",
        "key": person_name
    }
    try:
        response = requests.get(url, params=params)
        data = response.json()
        quote = data["quoteText"]
    except Exception as e:
        quote = "quote can not be retrieved at the moment"
    return quote

# print(get_artist_info("Vincent van Gogh")[0])
# print(get_random_quote_by_person("Vincent van Gogh"))