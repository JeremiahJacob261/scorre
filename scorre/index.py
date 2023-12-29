from django.http import HttpResponse
import requests
import json
from bs4 import BeautifulSoup
def get_scores(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text,'html5lib')
    mdsoup = soup.find('div',{"id": "score-data"})
    h4_tags = mdsoup.find_all('h4')

    # Clear the content of each h4 tag
    for tag in h4_tags:
        tag.decompose()

    fullres = []
    for des in mdsoup.find_all('span'):

        try:
            time = des.text
            match = des.next_sibling
            result = des.next_sibling.next_sibling.text
            parts = match.split(' - ')

            fullres.append({'time': time, 'home': parts[0],'away':parts[1], 'result': result})
        except Exception:
            print(Exception)
    return fullres;
# Use the function



def index(request):
    return HttpResponse(get_scores('https://www.flashscore.mobi/'))