"""
Stack Overflow checker, by Al Sweigart.

This program does a search on the Stack Overflow site (using Requests), then
return search results it hasn't seen before (and also opens them in a browser
window using webbrowser). Uses BeautifulSoup to parse the HTML.

Personally, I use this to check for anyone mentioning PyAutoGUI so I can
respond to them.
"""


# Set `query` to what you want to search for.
query = 'pyautogui'






from bs4 import BeautifulSoup
import requests
import urllib.parse
import shelve
import webbrowser

questionShelf = shelve.open('stackoverflow_checker_db')

queryUrl = 'https://stackoverflow.com/search?tab=newest&q=' + urllib.parse.quote_plus(query)
response = requests.get(queryUrl)
response.raise_for_status()
resultsSoup = BeautifulSoup(response.text, 'html.parser')

qLink = resultsSoup.select('.question-summary > div.summary > div.result-link > h3 > a')
qExcerpt = resultsSoup.select('.question-summary > div.summary > div.excerpt')

pagesToOpen = []

for i in range(len(qLink)):
	title = qLink[i].getText().strip()

	if title.startswith('A:'):
		continue # we only want the questions, not the answers

	link = 'https://stackoverflow.com' + qLink[i].attrs['href']
	excerpt = qExcerpt[i].getText().strip()

	if title not in questionShelf:
		print('Adding "%s"...' % title[:60])
		pagesToOpen.append(link)
		questionShelf[title] = {'link': link, 'excerpt': excerpt}
	else:
		print('Already in database: %s' % title[:60])




questionShelf.close()

if pagesToOpen:
	print('Opening %s pages...' % (len(pagesToOpen)))
	for url in pagesToOpen:
		webbrowser.open(url)

print('Done.')