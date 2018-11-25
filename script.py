import requests
from bs4 import BeautifulSoup as bs

# storing "#accordion" in html file in codepen and using it to extract info
page = requests.get("https://s.codepen.io/gr8ayu/debug/rQvERK/NjkYzqxqOnbM")



print("url status :", page)
soup = bs(page.content, 'html.parser')

body =soup.find("body")
print("body tag :", len(body))

A = list(body.children)[1]
print("--",len(A))
cardsBody = soup.find_all("div", attrs={'class':'card-body'})
print(cardsBody)
for cardBody in cardsBody:
    for i in cardBody.children:
        if(i.name == 'h3'):
            print(i.get_text().upper(), end='\n')
            
        if(i.name == 'a'):
            print(i.attrs['href'], end="\n\n\n")

f = open("links.txt", "w")
for cardBody in cardsBody:
    for i in cardBody.children:
        if(i.name == 'h3'):
            f.write(i.get_text().upper()+'\n')
            
        if(i.name == 'a'):
            f.write(i.attrs['href']+ "\n\n\n")
            
f.close()

