import urllib
from bs4 import BeautifulSoup

#Shingeki no Kyojin - error on website
#First name =  " "
#"""error in index """
#url = "http://myanimelist.net/anime/16498/Shingeki_no_Kyojin/episode" 

#url = "http://myanimelist.net/anime/28623/Koutetsujou_no_Kabaneri/episode" #Successful
#url = "http://myanimelist.net/anime/26243/Owari_no_Seraph/episode" #Successful
#url = "http://myanimelist.net/anime/22319/Tokyo_Ghoul/episode" #Successful
#url = "http://myanimelist.net/anime/31964/Boku_no_Hero_Academia/episode" #Successful

print "\n\n1. Shokugeki no Souma - Ni No Sara\n\n2. 91 Days\n\n3. Orange\n\n4. Naruto"
num  = raw_input("\n\nEnter the anime number : ")
if num == '1':
	url = "http://myanimelist.net/anime/32282/Shokugeki_no_Souma__Ni_no_Sara/episode"
elif num == '2':
	url = "http://myanimelist.net/anime/32998/91_Days/episode"
elif num == '3':
	url = "http://myanimelist.net/anime/32729/Orange/episode"
elif num == '4':
	url = "http://myanimelist.net/anime/1735/Naruto__Shippuuden/episode?offset=400"

html_ = urllib.urlopen(url).read()
soup = BeautifulSoup(html_)
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
		if href_title == url + "/" + str(num):
			title = tag_title.get_text()
			if not(title in titlelist):
				titlelist.append(title)			

				
print soup.title.get_text() + "\n"
print "Episode Count : " + str(len(datelist)) + "\n"

for count in range(0, len(datelist)):
	print "\n" + str(count + 1) + ".  " + titlelist[count + 1] + " : " + datelist[count]