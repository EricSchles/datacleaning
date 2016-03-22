import requests
import lxml.html
import grequests

def get_all_data():
    urls = [
        "https://nycopendata.socrata.com/data?cat=city%20government"#,
    #    "https://nycopendata.socrata.com/data?cat=business",
    #    "https://nycopendata.socrata.com/data?cat=education",
    #    "https://nycopendata.socrata.com/data?cat=environment",
    #    "https://nycopendata.socrata.com/data?cat=health",
    #    "https://nycopendata.socrata.com/data?cat=housing%20%26%20development",
    #    "https://nycopendata.socrata.com/data?cat=public%20safety",
    #    "https://nycopendata.socrata.com/data?cat=recreation",
    #    "https://nycopendata.socrata.com/data?cat=social%20services","https://nycopendata.socrata.com/data?cat=transportation",
    #    "https://nycopendata.socrata.com/data?cat=NYC%20BigApps"
    ]
    data = []
    rs = (grequests.get(u) for u in urls)
    for r in grequests.map(rs):
    
        html = lxml.html.fromstring(r.text)
        links = html.xpath("//a/@href")
        
        for link in links:
            if "data" in link:
                data.append(link)
    return data



def save_all_pdfs(links):
    final = []
    pdfs = []
    for link in links:
        r = requests.get(link)
        html = lxml.html.fromstring(r.text)
        possible_links = html.xpath("//a/@href")
        for i in possible_links:
            if "download" in i:
                final.append(i)

    for link in final:
        r = requests.get(link)
        html = lxml.html.fromstring(r.text)
        possible_pdfs = html.xpath("//a/@href")
        
        for i in possible_pdfs:
            if "pdf" in i:
                pdfs.append(i)
    
    for pdf in pdfs:
        name = pdf.split("/")[-1]
        with open(name,"wb") as f:
            r = requests.get(pdf)
            f.write(r.content)
    
if __name__ == '__main__':
    print get_all_data()
