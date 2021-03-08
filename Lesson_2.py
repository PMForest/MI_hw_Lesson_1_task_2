import dotenv import load_dotenv
import os
# from dotenv import load_dotenv
# load_dotenv()
#
# USERNAME = os.gerenv("USERNAME")
# print(USERNAME)
import bs4
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs

# r = requests.get("http://localhost:5000")
# # pprint(r.content)
# soup = bs(r.text, 'html.parser')
# soup = bs(r.text, 'lxml')
# # pprint(soup)
# p = soup.find("p")
# print(p)
# ps = soup.find_all("p", limit=3)
# pprint(len(ps))

soup = bs(r.text, 'html.parser')
a = soup.find("a")
print(a)

parent_a = a.parent
print(parent_a)

print()
