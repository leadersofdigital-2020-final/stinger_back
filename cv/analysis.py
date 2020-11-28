from nltk.stem.wordnet import WordNetLemmatizer
from pymorphy2 import MorphAnalyzer


keywords = [
    {
        'Backend Python-разработчик': {
            'language':  ['Python 2.x, Python 3.x'],
            'frameworks': ['Django', "Flask"], 
            'libs': ['asyncio'], 
            'databases': ['Postgre', 'MS-SQL', 'MySQL'],
            'container': ['Docker']
        }
    }
]

def correct_msg(text):

    morph = MorphAnalyzer()
    lemmatizer = WordNetLemmatizer()
    
    words = text.split()

    changes = [lemmatizer.lemmatize(w.lower()) for w in words]
    changes = morph.parse(changes)[0].inflect({'sing', 'nomn'}).word
    return changes


text = '''
    Работал в GetPure Inc, 3 месяца, занимался переписыванием legacy кода, разработкой новых фич в сервисе, доработкой и поддержкой старых фич.
    Стек и инструменты - Python 2.7 + Django 1.10, Python 3 + asyncio, Docker, Postgres
    '''




print(correct_msg(text))
