from bs4 import BeautifulSoup
import urllib.request

#url="https://myanimelist.net/anime/32282/Shokugeki_no_Souma__Ni_no_Sara/episode"
url = "https://myanimelist.net/anime/5114/Fullmetal_Alchemist__Brotherhood/episode"
page = urllib.request.urlopen(url).read()
soup = BeautifulSoup(page, "lxml")
datelist = list()
titlelist = list()

tags_title = soup('a')
tags_date = soup('td')

for tag_date in tags_date:
        href_date = tag_date.get('class', None)
        if href_date == [u'episode-aired']:
                date = tag_date.get_text()
                if not(date == "Aired"):
                        if not(date in datelist):
                                datelist.append(date)                           
                                
for num in range(1, len(datelist) + 1):
        for tag_title in tags_title:
                href_title = tag_title.get('href', None)
                if href_title == str(url) +"/"+ str(num):
                        title = tag_title.get_text()
                        if not(title in titlelist):
                                titlelist.append(title)                        

                                
print (soup.title.get_text() + "\n")
print ("Episode Count : " + str(len(datelist)) + "\n")
        
for count in range(0, len(datelist)):
    print ("\n" + str(count + 1) + ".  " + titlelist[count + 1] + " : " + datelist[count])
