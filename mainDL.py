import re
import os
import mechanize

br = mechanize.Browser()
linkChaser = mechanize.Browser()

br.addheaders = [('User-agent', 'earthpornScraping')]
linkChaser.addheaders = [('User-agent', 'imgurScrapin')]

br.open("http://www.reddit.com/r/earthporn/")
files = []

for link in br.links(url_regex=r"http://(.)*imgur(.)*"):
    if link.text != "[IMG]":
        if not re.match("(.)*i.imgur(.)*", link.url):
            print "FOLLOWING:", link.url
            linkChaser.open(url=link.url)
            print "followed the link"
            for imgLink in linkChaser.links(url_regex=r"(.)*/i.imgur(.)*"):
                fileName = imgLink.url.lstrip('http://')
                fileName = fileName.replace('/', '_')
                #print dir
                print imgLink.base_url
                print imgLink.url
                print fileName
                #fileName = os.path.join(dir, fileName.replace('/', '_'))
                linkChaser.retrieve("http:" + imgLink.url, filename=fileName)
            print "pumped it off my chest"
        else:
            print link
            linkChaser.open(url=link.url)
            fileName = link.url.lstrip('http://')
            fileName = fileName.replace('/', '_')
            br.retrieve(link.url, filename=fileName)