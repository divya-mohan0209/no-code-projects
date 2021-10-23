import requests
import gtts

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "list": "allpages",
    "apfrom": "Nelson Mandela",
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["allpages"]
s1=[]

for page in PAGES:
    s1+=list(page["title"])
    res="".join(s1)
    
t1=gtts.gTTS(res)
t1.save("demo.mp3")
