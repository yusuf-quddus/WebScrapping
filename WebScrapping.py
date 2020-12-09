import requests
import pandas
from bs4 import BeautifulSoup

l=[]
base_url = "https://www.century21.com/real-estate/fremont-ca/LCCAFREMONT/?p="

# multiple pages
for page in range(1, 3, 1):
    r=requests.get(base_url+str(page))
    c=r.content
    soup=BeautifulSoup(c, "html.parser")
    all=soup.find_all("div", {"class":"property-card"})
    for item in all:
        d={}
        d["Address"]=item.find("div", {"class": "property-address"}).text.strip()
        d["City"]=item.find("div", {"class": "property-city"}).text.strip()
        d["Price"]=item.find("a", {"class": "listing-price"}).text.replace("\n", "").replace(" ", "")
        try: 
            d["Beds"]=item.find("div", {"class": "property-beds"}).find("strong").text.strip()
        except:
            d["Beds"]=None
        try: 
            d["Baths"]=item.find("div", {"class": "property-baths"}).find("strong").text.strip()
        except:
            d["Baths"]=None
        try:
            d["Square Feet"]=item.find("div", {"class": "property-sqft"}).find("strong").text.strip()
        except:
            d["Square Feet"]=None
        l.append(d)

# output data to csv file
df = pandas.DataFrame(l)
df.to_csv("Listings.csv")

