from nltk.stem.wordnet import WordNetLemmatizer
from pymorphy2 import MorphAnalyzer


keywords = [
    {
        'Backend Python-разработчик': {
            'language':  ['Python 2', 'Python 3'],
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

    # changes = [lemmatizer.lemmatize(w.lower()) for w in words]
    
    match = []

    for word in words:
        for keyword in keywords[0]['Backend Python-разработчик']['language']:
            if word.lower().contains(keyword):
                match.append(word)
    return match


text = '''
    Работал в GetPure Inc, 3 месяца, занимался переписыванием legacy кода, разработкой новых фич в сервисе, доработкой и поддержкой старых фич.
    Стек и инструменты - Python 2.7 + Django 1.10, Python 3 + asyncio, Docker, Postgres
    '''




print(correct_msg(text))
