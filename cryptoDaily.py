from bs4 import BeautifulSoup
import requests

def crytoDailyInfo():

    d = {}

    r = requests.get("https://cryptodaily.co.uk/")
    soup = BeautifulSoup(r.content, 'html.parser')

    s = soup.find('div', class_ = "wide-breakin")

    main_story = s.find("a")
    main_story_name = main_story.find("img").get("alt")
    main_story_link = main_story.get("href")
    d[main_story_name] = main_story_link


    row_breaking = soup.find('div', class_ = "home-breaking").find('div', class_ = "row breaking-list").find_all('div', class_ = "col-sm-3 breakin-item")

    for row in row_breaking:
        link = row.find("h3").find("a").get("href")
        link_name = row.find("h3").text
        d[link_name] = link
    
    return d

crytoDailyInfo()