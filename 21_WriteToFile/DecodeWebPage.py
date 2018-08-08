#Using Requests and BeautifulSoup libraries extract the articles titles from NewYorkTimes homepage.

import requests
from bs4 import BeautifulSoup

class DECODE:
    def DecodeWebPage(self):

        # request the html from the webpage
        url = "https://www.nytimes.com"

        r = requests.get(url)
        r_html = r.text

        #print(r_html)

        # ----

        # BeautifulSoup
        # Beautiful Soup then parses the document using the best available parser. It will use an HTML parser unless you specifically tell it to use an XML parser.
        soup = BeautifulSoup(r_html, features="html.parser")

            # find the class = 'story-heading'
            #{'class': 'posted-on'}
            # list of this tag
        classTitle = soup.find_all("h2", class_ = "story-heading", limit = 3)
        print(*classTitle, sep='\n\n')
        print("=========================")

        res = []

        for elem in classTitle:
            #hrefTag = elem.contents[0]
            #title = hrefTag.contents
            hrefTag = elem.find("a")
            title = hrefTag.contents
            print(str(title) + "\n\n")
            res.append(title)

        return res

#main
#if __name__== "__main__":
#    de = DECODE.DecodeWebPage()
