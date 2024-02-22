
import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_Name = []
Prices = []
Description = []
Reviews = []
for i in range (2, 12):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_8_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_8_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=a4cdd6a6-15af-432e-ac49-6c4e6b29ae2b&as-searchtext=mobiles+&page="+str(i)
    
    r = requests.get(url)
    
    
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
    #**************************For Names ********************
    names = box.find_all("div", class_ = "_4rR01T")
    #print(names)
    
    # Now we get list in that all names are there so we etrate each name
    
    for i in names:
        name = i.text 
        Product_Name.append(name)
        
    #print(Product_Name)
    #print(len(Product_Name))
    #**************************For Prices ********************
    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    ##print(prices)
    
    for i in prices:
        name = i.text
        Prices.append(name)
    
    #print(Prices)
    #print(len(Prices))
    #************* FOr description ******
    desc = box.find_all("ul", class_="_1xgFaf")
    #print(desc)
    
    # Now we get list in that all names are there so we etrate each name
    
    for i in desc:
        name = i.text 
        Description.append(name)
        
    #print(Description)
    #print(len(Description))
    
    #********For Review *******
    
    reviews = box.find_all("div", class_="_3LWZlK")
    #print(reviews)
    
    # Now we get list in that all names are there so we etrate each name
    
    for i in reviews:
        name = i.text 
        Reviews.append(name)
        
    #print(Reviews)
    #print(len(Reviews))
#********To create Data Frame *******
#df = pd.DataFrame({"Product Name":Product_Name,"Prices":Prices,"Description":Description,"Reviews":Reviews})
#print(df)
#We use this when lengeth of each column is not same
a =  {"Product Name":Product_Name,"Prices":Prices,"Description":Description,"Reviews":Reviews}
df = pd.DataFrame.from_dict(a, orient='index')
df = df.transpose()
print(df)
#This will give data for one page
# If we want data for multiple page give loop after list

df.to_csv("H:/flipkart_mobiles_under_50000.csv")
