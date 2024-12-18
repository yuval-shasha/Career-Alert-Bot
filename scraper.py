from aiohttp.web_routedef import delete
from bs4 import BeautifulSoup
import requests

def scrape(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # getting the names of the roles via their links
    links = []
    for link in soup.find_all('a'):
        curr_link = link.get('href')
        if curr_link is None:
            continue
        curr_link = curr_link.lower()
        if link.get('href') in links:
            continue
        if 'https' in link.get('href'):
            continue
        # if the link contains at least one of the required words add to the list
        if 'intern' in curr_link or 'student' in curr_link or 'internship' in curr_link:
            links.append(link.get('href'))
        if 'page' in link.get('href'):
            links = links + scrape(link.get('href'))

    return links
