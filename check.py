import urllib3

http = urllib3.PoolManager()
url = input("Website URL: ")
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