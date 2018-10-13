import requests
from bs4 import BeautifulSoup

# Year of choice is to be given by the user
print("Please input the year: ")
year = int(input())
serial_no = 1

# This url can be used with the variable year to scrape the contents
url = "https://www.imdb.com/search/title?year="+str(year)+"&title_type=feature&sort=num_votes,desc&page=1&ref_=adv_prv"

# Fetching the data
data = requests.get(url)

# Loading the data in bs4
soup = BeautifulSoup(data.text,'html.parser')
infoblocks = soup.findAll('div',{'class':'lister-item-content'})
print('Sl No.', '       ','Movie(Rating)')
for block in infoblocks:
    header = block.find('a').text
    rating = block.find('div',{'class':'ratings-bar'}).find('strong').text
    print(serial_no,"      ", header,'('+rating+')')
    serial_no += 1