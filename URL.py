import requests
from bs4 import BeautifulSoup

def query_searching(line): 
	if len(line)  > 300:
		sentence = sentence[0:298]
	query = 'https://en.wikipedia.org/w/index.php?search=+'+ line
	response = requests.get(query)
	soup = BeautifulSoup(response.text, 'html.parser')
	
	for div in soup.findAll('div',attrs={'class':'mw-search-result-heading'}):
		link = div.find('a')['href']
		address.append(link)

def frequency_checking():
	maximum = 0    
	link = None
	for i in address:
		cnt = address.count(i)
		if cnt>maximum :
			maximum = cnt
	if maximum>1:
		link = max(address, key = address.count)
	else:
		link = address[0]
	return link

address = []

n= int(input("Input:\nEnter the number of sentences to be checked  "))
for i in range(n):
    sentence=input("Enter sentence  :\n")
    query_searching(sentence)
link = frequency_checking()
print("\nOutput :")
print('https://en.wikipedia.org'+link)