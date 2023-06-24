from bs4 import BeautifulSoup
import requests

class Scraper():
    def get_info(self, name):
        name = str(name).lower().replace("g'",'g‘')
        html = requests.get('http://ismlar.com/name/' + name).text
        soup = BeautifulSoup(html, 'lxml')  
        full = soup.find('h1').parent
        try:
            title = full.h1.text.strip()
        except:
            title = False
        try:
            meaning = full.p.text.strip()
        except:
            meaning = False
        try:
            type = full.find_all('span')[1].text.strip().replace('\n', '').replace(' ', '').replace(',',', ')
        except:
            type = False
        try:
            category = full.find_all('a')[1].text.strip()
        except:
            category = False
        try:
            views = full.find_all('span')[-1].text.strip()
        except:
            views = False

        return {'title':title, 'meaning':meaning, 'types':type, 'category':category, 'views':views}
    
scraper = Scraper()