# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 12:03:45 2017

@author: wook
"""

import bs4 #good for html txt
from urllib.request import urlopen as uReq#grab data from internet:urllib and i  only need request module
from bs4 import BeautifulSoup as soup

my_url = 'https://www.newegg.com/Laptops-Notebooks/Category/ID-223?Tpk=laptop'

#opening up connection , grabbing the page

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
#html parsing
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

filename= "scraping.csv"
f = open(filename, "w")
headers = "brand, title_name\n"

f.write(headers)
for container in containers:
    brand = container.div.div.a.img["title"]
    title = container.findAll("a",{"class":"item-title"})
    title_name = title[0].text #assume that 내용이 0번째 행렬에 들어가있고, 거기서 text만 잡아줌
#    price = container.findAll("a",{"class":"membership-info membership-popup"})
#    product_price = price[0].number
    print("brand : " + brand)
    print("title name : " + title_name)
#    print("product price : " + product_price)
    f.write(brand + "," + title_name.replace(",", " " ) + "\n")

f.close