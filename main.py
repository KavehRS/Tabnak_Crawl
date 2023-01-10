#Libs
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get Portal Data & Create DataFrame
link = requests.get('https://www.tabnak.ir/')
soup_link = BeautifulSoup(link.text, 'html.parser')
Tabnak1 = pd.DataFrame()
Tabnak2 = pd.DataFrame()
Tabnak3 = pd.DataFrame()


# Main Titr News
title_first = soup_link.find('h3', {'class': "Htag title_elec"})
aa = title_first.find('a')
Tabnak1.loc[0, "NewsLink"] = 'http://www.tabnak.ir'+aa.get('href')
Tabnak1.loc[0, "NewsTitr"] = aa.get('title')
tfb = soup_link.find('div', {'class': "box_election"})
Tabnak1.loc[0, "NewsTitrBrief"] = tfb.find('div', {'class': "lead2"}).text

# News of second importance
title_contents = soup_link.find('div', {'class': "service_content"})
for i in range(0, 48):
    try:
        Content = title_contents.findAll('a', {'class': "title_main"})[i]
        Tabnak2.loc[i, "NewsLink"] = 'http://www.tabnak.ir' + Content.get('href')
        Tabnak2.loc[i, "NewsTitr"] = Content.get('title')
        Tcb = soup_link.findAll('div', {'class': "lead1"})[i]
        Tabnak2.loc[i, "NewsTitrBrief"] = Tcb.text
    except:
             pass


# last News
Lnl = soup_link.find('div', {'id': "tab1_aa"})
for i in range(1, 200):
     try:
        # Lastnews = Lnl.find('h3', {'class': "Htag"})[i]
        Lastnews = Lnl.findAll('a')[i]
        Tabnak3.loc[i, "NewsLink"] = Lastnews.get('href')
        Tabnak3.loc[i, "NewsTitr"] = Lastnews.get('title')
      except:
               pass
