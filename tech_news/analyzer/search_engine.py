import datetime
from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    complete_news = search_news(query)
    return [(news["title"], news["url"]) for news in complete_news]


# Requisito 7
def search_by_date(date):
    try:
        search_date = datetime.date.fromisoformat(date)
    except ValueError:
        raise ValueError("Data inválida")
    search_date = search_date.strftime("%d/%m/%Y")
    query = {"timestamp": search_date}
    complete_news = search_news(query)
    return [(news["title"], news["url"]) for news in complete_news]
    



# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
