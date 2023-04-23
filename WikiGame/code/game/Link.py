import re


class Link:
    def __init__(self, blue_text, title, url):
        self.blue_text = blue_text
        self.title = title
        self.url = url
        clean_string = re.sub('[^0-9a-zA-Z]+', ' ', blue_text + " " + title)
        self.clean_words = clean_string.split()

    def __hash__(self):
        return hash(self.url)
