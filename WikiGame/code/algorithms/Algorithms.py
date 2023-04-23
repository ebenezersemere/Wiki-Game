import re
import requests


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
    return clean_list(links)


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
