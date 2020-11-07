import urllib3
import requests

http = urllib3.PoolManager()
url = input("Website URL: ")
try:
    response = requests.get(url)
    r = http.request("GET", url, headers={
        'User-Agent': 'Mozilla/5.0'
    })
    nf = 404
    rl = 429
    ok = 200
    br = 400
    fr = 403
    rt = 408
    rp = r.status
    if rp == nf:
        print("Not found")
    if rp == rl:
        print("Rate limiting")
    if rp == ok:
        print("Online")
    if rp == rt:
        print("Request Timeout/Offline")
except requests.exceptions.MissingSchema as exception:
    print("URL does not exist on the Internet. Try adding HTTP:// before the url. Eg. https://google.com")
except requests.exceptions.ConnectionError as urlexception:
    print("The connection to the URL has been terminated due to some error.")