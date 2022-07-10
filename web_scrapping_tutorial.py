from requests_html import HTMLSession 

session = HTMLSession() 
url = 'https://news.google.com/topstories?hl=en-US&gl=US&ceid=US:en'

r = session.get(url)
#r.html.render()

#articles = r.html.find('article')

#print(articles)