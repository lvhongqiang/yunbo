import requests
from proxy import proxies


def post(url, data=None, json=None, limit=10, timeout=5, **kwargs):
    while (limit > 0):
        limit -= 1
        proxy = proxies.choice()
        try:
            return requests.post(url, data=data, json=json, proxies={'http': proxy}, timeout=timeout, **kwargs)
        except Exception as e:
            proxies.remove(proxy)
            print(e)
