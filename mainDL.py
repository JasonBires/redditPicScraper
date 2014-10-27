import re
import mechanize

br = mechanize.Browser()
br.open("http://www.reddit.com/r/earthporn/")
urlList = []
for link in br.links(url_regex=r"http://(.)*imgur(.)*"):
    if link.text != "[IMG]":
        if not re.match("(.)*i.imgur(.)*):
            link.follow()
        print link.text
        print link.url
