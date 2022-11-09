from tech_news.database import get_collection


# Requisito 10
def top_5_news():
    query = [("comments_count", -1), ("title", 1)]
    complete_news = get_collection().find({}).sort(query).limit(5)
    return [(news["title"], news["url"]) for news in complete_news]


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
