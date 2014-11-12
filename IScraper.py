import mainDL as scraper
class ScraperInterface():
    def downloadPage(self, url, numberOfPages=1):
        scraper.pullXPages(numberOfPages, url)
    def downloadFromSubreddits(self, urlList, numberOfPages=1):
        for url in urlList:
            scraper.pullXPages(numberOfPages, url)