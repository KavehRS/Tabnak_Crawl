import requests
from bs4 import BeautifulSoup
import pandas as pd

# Get Portal Data & Create DataFrame
link = requests.get('https://www.tabnak.ir/')
soup_link = BeautifulSoup(link.text, 'html.parser')
tabnak1 = pd.DataFrame()
tabnak2 = pd.DataFrame()

# Main Titr News
title_first = soup_link.find('h3', {'class': "Htag title_elec"})
aa = title_first.find('a')
tabnak1.loc[0, "NewsLink"] = 'http://www.tabnak.ir'+aa.get('href')
tabnak1.loc[0, "NewsTitr"] = aa.get('title')
tfb = soup_link.find('div', {'class': "box_election"})
tabnak1.loc[0, "NewsTitrBrief"] = tfb.find('div', {'class': "lead2"}).text

# News of second importance
title_contents = soup_link.find('div', {'class': "service_content"})
for i in range(0, 48):
    # try:
        content = title_contents.findAll('a', {'class': "title_main"})[i]
        tabnak2.loc[i, "NewsLink"] = 'http://www.tabnak.ir' + content.get('href')
        tabnak2.loc[i, "NewsTitr"] = content.get('title')
        tcb = soup_link.findAll('div', {'class': "lead1"})[i]
        print(tcb.text)
        tabnak1.loc[i, "NewsTitrBrief"] = tcb.text
        print(i)
    # except:
    #          pass
