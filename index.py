from bs4 import BeautifulSoup
import requests

#get html content of the website
name=input("Search: ")
URL=f'https://pokemondb.net/pokedex/{name}'
r=requests.get(URL)
while r.status_code!=200:
    print(f"Status code: {r.status_code}")
    name=input("Search: ")
    URL=f'https://pokemondb.net/pokedex/{name}'
    r=requests.get(URL)

#scraping website
soup = BeautifulSoup(r.content, 'html.parser')
div=soup.find("div", {"class": "grid-col span-md-6 span-lg-4"})
tbody=div.table.tbody
tr_list=tbody.find_all("tr")
for tr in tr_list:
    type=tr.th.text
    td=tr.td
    if type=='National №':
        value=td.strong.text
    elif type=='Abilities':
        value=[]
        element_types=td.find_all("span")
        for t in element_types:
            value.append(t.text)
        value=', '.join(value)
        value+='\n'+'Hidden Ability: '+td.small.a.text
    elif type=='Local №':
        value=td.text.split(')')
        value='), '.join(value)
    else:
        value=td.text.strip()
    print(f"{type}: {value}")
