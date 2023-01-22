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

counterB = 0


# Main Titr News
title_first = soup_link.find('h3', {'class': "Htag title_elec"})
aa = title_first.find('a')
Tabnak1.loc[0, "NewsLink"] = 'http://www.tabnak.ir'+aa.get('href')
Tabnak1.loc[0, "NewsTitr"] = aa.get('title')
tfb = soup_link.find('div', {'class': "box_election"})
Tabnak1.loc[0, "NewsTitrBrief"] = tfb.find('div', {'class': "lead2"}).text
url = 'http://www.tabnak.ir' + aa.get('href')
ab = requests.get(url)
tfl = BeautifulSoup(ab.text, 'html.parser') # title_first list
# count paragraphs
counter = 0
for k in tfl.findAll('p'):
    if k:
        counter = counter + 1
# get paragraphs and put to DataFrame
fullnews = ''
for j in range(counter):
    ac = tfl.findAll('p')[j]
    fullnews = fullnews + '\n' + ac.text
Tabnak1.loc[0, "NewsText"] = fullnews
link2 = requests.get(url)
# GET NewsGroup
try:
    titr1_link = BeautifulSoup(link2.text, 'html.parser')
    newsAA = titr1_link.find('div', {'id': "box-top-news"})
    news_path = newsAA.find('div', {'class': "news_path"}).text
    atest = news_path.split('»')
    Tabnak1.loc[0, "NewsGroup"] = atest[0]
    Tabnak1.loc[0, "NewsGroupSub"] = atest[1]
except:
    pass
# count tags
tag_count = 0
for k in titr1_link.findAll('a', {'class': "btn btn-primary-news"}):
    if k:
        tag_count = tag_count + 1

# get Tags and put to DataFrame
AllTags = ''
for l in range(tag_count):
    tags = titr1_link.findAll('a', {'class': "btn btn-primary-news"})[l]
    AllTags = AllTags + '#' + tags.text
Tabnak1.loc[0, "KeyWord"] = AllTags
# get Date & Time
news_time = titr1_link.find('div', {'class': "news_nav news_pdate_c"}).text
fa_time = news_time.split('-')
Tabnak1.loc[0, "ReleaseDateNews"] = fa_time[0].split(':')[1]
Tabnak1.loc[0, "ReleaseTimeNews"] = fa_time[1].split()[0]

############################################################################################
# News of second importance
title_contents = soup_link.find('div', {'class': "service_content"})
for i in range(0, 48):
    try:
        Content = title_contents.findAll('a', {'class': "title_main"})[i]
        t2l = 'http://www.tabnak.ir' + Content.get('href')
        Tabnak2.loc[i, "NewsLink"] = t2l
        Tabnak2.loc[i, "NewsTitr"] = Content.get('title')
        Tcb = soup_link.findAll('div', {'class': "lead1"})[i]
        Tabnak2.loc[i, "NewsTitrBrief"] = Tcb.text
        bb = requests.get(t2l)[i]
        tcl = BeautifulSoup(bb.text, 'html.parser')[i]
# count paragraphs
        for k in tcl.findAll('p'):
            if k:
                counterB = counterB + 1
# get paragraphs and put to DataFrame
        fullnewsB = ''
        for n in range(counterB):
            af = tcl.findAll('p')[n]
            fullnewsB = fullnewsB + '\n' + af.text
        Tabnak2.loc[i, "NewsText"] = fullnewsB

        # Tabnak2.loc[i, "NewsGroup"] = 0
        # Tabnak2.loc[i, "NewsGroupSub"] = 0
        # Tabnak2.loc[i, "KeyWord"] = 0
        # Tabnak2.loc[i, "ReleaseTimeNews"] = 0
        # Tabnak2.loc[i, "ReleaseDateNews"] = 0




    except:
             pass












# last News
Lnl = soup_link.find('div', {'id': "tab1_aa"})
for i in range(1, 200):
     try:
        Lastnews = Lnl.findAll('a')[i]
        Tabnak3.loc[i, "NewsLink"] = Lastnews.get('href')
        Tabnak3.loc[i, "NewsTitr"] = Lastnews.get('title')
      except:
               pass
