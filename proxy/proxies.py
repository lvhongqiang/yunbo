import random
from proxy import pull

minSize = 1
proxyList = []

def fill():
    ps = pull.xici()
    for p in ps:
        proxyList.append(p)

def choice():
    if len(proxyList)<minSize:
        fill()
    print("proxies:",len(proxyList))
    return random.choice(proxyList)

def remove(proxy):
    proxyList.remove(proxy)