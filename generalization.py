import requests
import lxml.html
import unidecode
import grequests

class Scraper:
    def __init__(self,url):
        self.url = url
        self.text = self.grab(self.url)
    def grab(self):
        r = requests.get(url)
        text = unidecode.unidecode(r.text)
        return text
    def links(self):
        html = lxml.html.fromstring(self.text)
        return html.xpath("//a/@href")
            
    def pdfs(self):
        links = self.links()
        return [link for link in links if "pdf" in link]
    
    def save_pdfs(self):
        pdfs = self.pdfs()
        for pdf in pdfs:
            name = pdf.split("/")[-1]
            with open(name,"wb") as f:
                r = requests.get(pdf)
                f.write(r.content)

    def crawl_many_links(self,many_links=None):
        """Crawls all the links given to the function and returns all the links on subsequent pages"""
        if many_links==None:
            many_links = self.links()
        if not isinstance(many_links,[]):
            raise AssertionError("crawl_many_links requires a list of links!!! (of type string)")
        for i in many_links:
            if not "http" in i:
                many_links.remove(i)
        rs = (grequests.get(u) for u in many_links)
        responses = grequests.map(rs)
        total_links = []
        for r in responses:
            html = lxml.html.fromstring(r.text)
            total_links += html.xpath("//a/@href")
            #looking for complete links only
        for i in total_links:
            if not "http" in i:
                total_links.remove(i)
        return total_links
    def depth_crawl(self,depth):
        if depth < 1:
            raise AssertionError("depth must be 1 or greater")
        while depth > 0:
            total_links += self.crawl_many_links(total_links)
            depth -= 1
        return total_links

