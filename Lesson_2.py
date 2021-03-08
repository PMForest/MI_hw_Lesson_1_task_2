import requests
from fake_useragent import UserAgent
u = UserAgent()

url = "https://api.themoviedb.org/3/genre/movie/list?api_key=0eee4c21bc1fa75543e9207ac944ada2&&language=en-US"


r = requests.get(url)

from pprint import pprint
pprint(r.text)
pprint(r.json())
