
import pandas as pd
import requests
from bs4 import BeautifulSoup

for i in range (2, 10):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_1_8_na_na_na&otracker1=AS_Query_HistoryAutoSuggest_1_8_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+50000&requestId=a4cdd6a6-15af-432e-ac49-6c4e6b29ae2b&as-searchtext=mobiles+&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    np = soup.find("a", class_ = "_1LKTO3").get("href")
    cnp = "https://www.flipkart.com" + np 
    print(cnp)
