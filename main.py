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
for i in range(1, 48):
    try:
        content = title_contents.findAll('a', {'class': "title_main"})[i]
        tabnak2.loc[i, "NewsLink"] = 'http://www.tabnak.ir' + content.get('href')
        tabnak2.loc[i, "NewsTitr"] = content.get('title')
        #tcb = soup_link.find('div', {'class': "box_election"})
        tabnak1.loc[i, "NewsTitrBrief"] = title_contents.find('div', {'class': "lead1"}).text

    except:
             pass

#         # NewsTitrBrief = title_contents.findAll()
#         # tabnak2.loc[i, "NewsTitrBrief"] = NewsTitrBrief.text
#         # NewsGroup = title_contents.findAll()[i]
#         # tabnak2.loc[i, "NewsGroup"] = NewsGroup.text
#         # NewsGroupSub = title_contents.findAll()[i]
#         # tabnak2.loc[i, "NewsGroupSub"] = NewsGroupSub.text
#         # NewsTitr = title_contents.findAll()[i]
#         # tabnak2.loc[i, "NewsTitr"] = NewsTitr.text
#         # KeyWord = title_contents.findAll()[i]
#         # tabnak2.loc[i, "KeyWord"] = KeyWord.text
#         # ReleaseTimeNews = title_contents.findAll()[i]
#         # tabnak2.loc[i, "ReleaseTimeNews"] = ReleaseTimeNews.text
#         # ReleaseDateNews = title_contents.findAll()[i]
#         # tabnak2.loc[i, "ReleaseDateNews"] = ReleaseDateNews.text

# #


# for i in range(0, 15):
#     try:

        # NewsGroup = title_first.findAll()[i]
        # tabnak.loc[i, "NewsGroup"] = NewsGroup.text
        # NewsGroupSub = title_first.findAll()[i]
        # tabnak.loc[i, "NewsGroupSub"] = NewsGroupSub.text
        # NewsTitr = title_first.findAll()[i]
        # tabnak.loc[i, "NewsTitr"] = NewsTitr.text
        # KeyWord = title_first.findAll()[i]
        # tabnak.loc[i, "KeyWord"] = KeyWord.text
        # ReleaseTimeNews = title_first.findAll()[i]
        # tabnak.loc[i, "ReleaseTimeNews"] = ReleaseTimeNews.text
        # ReleaseDateNews = title_first.findAll()[i]
        # tabnak.loc[i, "ReleaseDateNews"] = ReleaseDateNews.text
#     except:
#         pass
#
# print(NewsLink.text)





# for ii in driver.find_elements_by_tag_name("a"):
#     link = ii.get_attribute('href')

# tabnak.loc[i, "NewsLink"] = NewsLink.text

# print('NewsLink')
# for i in range(0, 15):
#     try:

        # NewsGroup = title_first.findAll()[i]
        # tabnak.loc[i, "NewsGroup"] = NewsGroup.text
        # NewsGroupSub = title_first.findAll()[i]
        # tabnak.loc[i, "NewsGroupSub"] = NewsGroupSub.text
        # NewsTitr = title_first.findAll()[i]
        # tabnak.loc[i, "NewsTitr"] = NewsTitr.text
        # KeyWord = title_first.findAll()[i]
        # tabnak.loc[i, "KeyWord"] = KeyWord.text
        # ReleaseTimeNews = title_first.findAll()[i]
        # tabnak.loc[i, "ReleaseTimeNews"] = ReleaseTimeNews.text
        # ReleaseDateNews = title_first.findAll()[i]
        # tabnak.loc[i, "ReleaseDateNews"] = ReleaseDateNews.text
#     except:
#         pass
#
# print(NewsLink.text)


# for i in range(0, 15):
#     try:
#         address = title_original.findAll('a', {'class': "d-block"})[i]
#         #print(address.text)
#         #print('*******************')
#         news.loc[i, "address"] = address.text
#         rutitr = title_original.findAll('div', {'class': "section-3-news-rutitr"})[i]
#         news.loc[i, "rutitr"] = rutitr.text
#         titr = title_original.findAll('h2', {'class': "section-3-news-titr"})[i]
#         print(titr.text)
#         news.loc[i, "titr"] = titr.text
#         print(i)
#         subtitle = title_original.findAll('div', {'class': "section-3-news-subtitle"})[i]
#         news.loc[i, "subtitle"]  = subtitle.text
#     except:
#         pass
