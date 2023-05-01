import re
import requests
from bs4 import BeautifulSoup

########################################################################################################################


def find_hyperlinks(page_name):
    # Set up the API request parameters
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'titles': page_name,
        'prop': 'links',
        'pllimit': 'max',
        'format': 'json'
    }

    # Send the API request and parse the response
    response = requests.get(url, params=params)
    data = response.json()

    # Extract the links from the API response
    links = []

    try:
        for page in data['query']['pages'].values():
            for link in page['links']:
                links.append(link['title'])
    except KeyError:
        print(f"KeyError: No links found for: {page_name}")
        return []

    # Print the resulting list of links
    return links

def get_page_contents(page_name):
    # Set up the API request parameters
    url = 'https://en.wikipedia.org/w/api.php'
    params = {
        'action': 'query',
        'titles': page_name,
        'prop': 'extracts',
        'exintro': True,
        'format': 'json'
    }

    # Send the API request and parse the response
    response = requests.get(url, params=params)
    data = response.json()['query']['pages']
    key = list(data.keys())[0]
    html = data[key]['extract']
    
    soup = BeautifulSoup(html, 'html.parser')
    text = soup.get_text()
    #['217291']['extract']
    
    return text #['217291']['extract']217291


########################################################################################################################

def clean_list(links):
    clean = []

    # define regex pattern to match non-alphanumeric characters and whitespace
    pattern = re.compile('[^\\w\\s]+')

    for string in links:
        # apply pattern
        cleaned = pattern.sub('', string)

        # add the cleaned string to the new array if non-null
        if cleaned:
            clean.append(cleaned)

    return clean


########################################################################################################################

def get_closest(hyperlinks, destination, model):
    """
    Returns the closest URL to the given URL.
    """
    if not hyperlinks:
        return None

    sorted_hyperlinks = list()

    for link in hyperlinks:
        sorted_hyperlinks.append((link, model.query(link, destination)))

    sorted_hyperlinks.sort(key=lambda x: x[1])

    for i, link in enumerate(sorted_hyperlinks):
        if not valid_link(link[0]):
            continue

        return link[i][0]

########################################################################################################################


def valid_link(link):
    # Set up the URL for the Wikipedia API
    url = "https://en.wikipedia.org/w/api.php"

    # Set the search phrase
    search_phrase = link

    # Set the parameters for the API call
    params = {
        "action": "query",
        "format": "json",
        "titles": link,
        "prop": "info",
        "inprop": "url"
    }

    # Send the API request
    response = requests.get(url=url, params=params)
    data = response.json()

    # Check if the page exists
    page_id = list(data["query"]["pages"].keys())[0]
    return page_id != "-1"


# print(find_hyperlinks("Albert Einstein"))