import requests
from lxml import etree

def xici():
    url = 'http://www.xicidaili.com/wt/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0',
    }
    r = requests.get(url,headers=headers)
    print(r.text)
    document = etree.HTML(r.text)
    proxyList = document.xpath('//table[@id="ip_list"]/tr')[1:]
    plist = []
    for p in proxyList:
        host = p.xpath('./td[2]/text()')[0]
        port = p.xpath('./td[3]/text()')[0]
        plist.append('http://%s:%s' % (host,port))
    return plist