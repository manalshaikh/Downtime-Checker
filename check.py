import urllib3

http = urllib3.PoolManager()

r = http.request("GET", "https://shadowhosting.net")
rp = r.status
print(rp)