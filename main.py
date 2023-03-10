#Libs
import requests
from bs4 import BeautifulSoup
import pandas as pd


# Get Portal Data & Create DataFrame
link = requests.get('https://www.tabnak.ir/')
soup_link = BeautifulSoup(link.text, 'html.parser')
ColumnsName =['NewsLink', 'NewsTitr', 'NewsTitrBrief', 'NewsText', 'NewsGroup','NewsGroupSub','KeyWord','ReleaseDateNews', 'ReleaseTimeNews']
Tabnak1 = pd.DataFrame(columns = ColumnsName, dtype=object)
Tabnak2 = pd.DataFrame(columns = ColumnsName, dtype=object)
Tabnak3 = pd.DataFrame(columns = ColumnsName, dtype=object)
Tabnak_Total = pd.DataFrame(columns = ColumnsName, dtype=object)

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
        bb = requests.get(t2l)
        contentB = BeautifulSoup(bb.text, 'html.parser')
# count paragraphs
        countB = 0
        for k in contentB.findAll('p'):
            if k:
                countB = countB + 1
# get paragraphs and put to DataFrame
        fullcontentB = ''
        for d in range(countB):
            paragraphB = contentB.findAll('p')[d]
            fullcontentB = fullcontentB + '\n' + paragraphB.text
        Tabnak2.loc[i, "NewsText"] = fullcontentB
        pageB_link = BeautifulSoup(bb.text, 'html.parser')
    # GET NewsGroup
        NewsGroupB = pageB_link.find('div', {'class': "news_path"}).text
        sepA = NewsGroupB.split('»')
        Tabnak2.loc[i, "NewsGroup"] =sepA[0]
        Tabnak2.loc[i, "NewsGroupSub"] = sepA[1]
# count tags
        tagB_count = 0
        for m in pageB_link.findAll('a', {'class': "btn btn-primary-news"}):
            if m:
                tagB_count = tagB_count + 1

# get Tags and put to DataFrame
        AllTagBs = ''
        for n in range(tagB_count):
            tagB = pageB_link.findAll('a', {'class': "btn btn-primary-news"})[n]
            AllTagBs = AllTagBs + '#' + tagB.text
        Tabnak2.loc[i, "KeyWord"] = AllTagBs
# get Date & Time
        content_time = pageB_link.find('div', {'class': "news_nav news_pdate_c"}).text
        faB_time = content_time.split('-')
        Tabnak2.loc[i, "ReleaseDateNews"] = faB_time[0].split(':')[1]
        Tabnak2.loc[i, "ReleaseTimeNews"] = faB_time[1].split()[0]

    except:
        pass

##############################################################################################
# last News
Lnl = soup_link.find('div', {'id': "tab1_aa"})
for i in range(1, 150):
    Lastnews = Lnl.findAll('a')[i]
    lastnews_link = 'http://www.tabnak.ir' + Lastnews.get('href')
    lastnews_link2 = requests.get(lastnews_link)
    Tabnak3.loc[i, "NewsLink"] = lastnews_link
    Tabnak3.loc[i, "NewsTitr"] = Lastnews.get('title')
# get NewsTitrBrief
    lastnews_content = BeautifulSoup(lastnews_link2.text, 'html.parser')
    lastnewBrief = lastnews_content.find('div', {'class': "subtitle"})
    try:
        Tabnak3.loc[i, "NewsTitrBrief"] = lastnewBrief.text
    except:
        pass
# count paragraphs
    countC = 0
    for p in lastnews_content.findAll('p'):
        if p:
            countC = countC + 1

# get paragraphs and put to DataFrame
    fullLastnews = ''
    lastnews_text = lastnews_content.find('div', {'class': "body"})

    for z in range(countC):
        try:
            paragraphL  = lastnews_text.findAll('p')[z]
            fullLastnews = fullLastnews + '\n' + paragraphL.text
        except:
            pass
    Tabnak3.loc[i, "NewsText"] = fullLastnews
# GET NewsGroup
    try:
        NewsGroupC = lastnews_text.find('div', {'class': "news_path"})
        NGtext = NewsGroupC.text
        sepC = NGtext.split('»')
        Tabnak3.loc[i, "NewsGroup"] =sepC[0]
        Tabnak3.loc[i, "NewsGroupSub"] = sepC[1]
    except:
        pass

#count tags
    tagL_count = 0
    for u in lastnews_content.findAll('a', {'class': "btn btn-primary-news"}):
        if u:
            tagL_count = tagL_count + 1
# get Tags and put to DataFrame
    try:
        AllTagL = ''
        for w in range(tagL_count):
            tagL = lastnews_content.findAll('a', {'class': "btn btn-primary-news"})[w]
            AllTagBs = AllTagL + '#' + tagL.text
        Tabnak3.loc[i, "KeyWord"] = AllTagBs
    except:
        pass
# get Date & Time
    try:
        contentL_time = lastnews_content.find('div', {'class': "news_nav news_pdate_c"}).text
        faL_time = contentL_time.split('-')
        Tabnak3.loc[i, "ReleaseDateNews"] = faL_time[0].split(':')[1]
        Tabnak3.loc[i, "ReleaseTimeNews"] = faL_time[1].split()[0]
    except:
            pass


############################################################################################
# Total News

Tabnak_Total = Tabnak1.append([Tabnak2, Tabnak3])

