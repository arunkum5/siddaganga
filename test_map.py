import urllib.request

url = "https://maps.google.com/maps?q=12.9974756,77.5503294+(SRI%20SIDDAGANGA%20CHARITABLE%20TRUST)&ll=12.9990,77.5503294&t=&z=16&ie=UTF8&iwloc=&output=embed"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req)
    html = resp.read().decode('utf-8')
    if "12.999" in html:
        print("ll is present in the response")
    else:
        print("ll might be ignored")
except Exception as e:
    print(e)
