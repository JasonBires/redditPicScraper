import re
import os
import mechanize

"""Pass in a URL from imgur, ergo imgLink.url
   Return a properly formatted string"""
def nameImgurFile(imgUrl):
    name = imgUrl.lstrip('http://')
    name = name.replace('/', '_')
    name = name.replace('?', '')
    return name

def pullPage(pageString):
    br = mechanize.Browser()
    linkChaser = mechanize.Browser()

    br.addheaders = [('User-agent', 'earthpornScraping')]
    linkChaser.addheaders = [('User-agent', 'imgurScrapin')]

    br.open(pageString)
    if re.match("(.)*www.reddit.com/over18(.)*", br.geturl()):
        print "fuck"
        br.set_cookie("name=over18;content=1;domain=.reddit.com;path=/")
        br.open(pageString)
        print br.geturl()
    files = []
    try:
        for link in br.links(url_regex=r"http://(.)*imgur(.)*"):
            if link.text != "[IMG]":
                if not re.match("(.)*i.imgur(.)*", link.url):
                    linkChaser.open(url=link.url)
                    for imgLink in linkChaser.links(url_regex=r"(.)*/i.imgur(.)*"):
                        fileName = nameImgurFile(imgLink.url)
                        linkChaser.retrieve("http:" + imgLink.url, filename="pics/" + fileName)
                else:
                    linkChaser.open(url=link.url)
                    fileName = nameImgurFile(link.url)
                    br.retrieve(link.url, filename="pics/" + fileName)
    except:
        print "dropped"
def pullXPages(numPages, pageString):
    curPage = pageString
    br = mechanize.Browser()
    br.addheaders = [('User-agent', 'earthpornScraping')]
    for x in range(0, numPages):
        pullPage(curPage)
        br.open(curPage)
        curPage = br.links(url_regex=r"http://www.reddit.com/r/(.)*?count(.)*&after=(.)*").next().url
        print curPage

def main():
    pullXPages(15, "http://www.reddit.com/r/tumblrinaction")
    
if __name__ == '__main__':
    main()