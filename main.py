import requests
import nltk
from bs4 import BeautifulSoup

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

URL = 'https://www.w3.org/DesignIssues/TimBook-old/History.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
body = soup.find('body')
text = body.text
tokens = nltk.word_tokenize(text)
tagged_words = nltk.pos_tag(tokens)

array = [{'count': 0, 'name': 'Существительные'}, {'count': 0, 'name': 'Глаголы'}, {'count': 0, 'name': 'Наречия'},
         {'count': 0, 'name': 'Междометия'}, {'count': 0, 'name': 'Прилагательные'}, {'count': 0, 'name': 'Предлоги'}]

for (word, pos) in nltk.pos_tag(tokens):
    if word.isalpha():
        if pos.startswith('N'):
            array[0]['count'] += 1
        elif pos.startswith('V'):
            array[1]['count'] += 1
        elif pos.startswith('RB'):
            array[2]['count'] += 1
        elif pos.startswith('IN'):
            array[3]['count'] += 1
        elif pos.startswith('JJ'):
            array[4]['count'] += 1
        elif pos.startswith('PR'):
            array[5]['count'] += 1

array = sorted(array, key=lambda x: x['count'], reverse=True)
for item in array[:5]:
    print(f"{item['name']}: {item['count']}")
