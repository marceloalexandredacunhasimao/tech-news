from tech_news.database import get_collection, find_news


# Requisito 10
def top_5_news():
    query = [("comments_count", -1), ("title", 1)]
    complete_news = get_collection().find({}).sort(query).limit(5)
    return [(news["title"], news["url"]) for news in complete_news]


# Requisito 11
def top_5_categories():
    count = {}
    news_list = find_news()
    categories = [news["category"] for news in news_list]
    for category in categories:
        if category not in count:
            count[category] = 0
        count[category] += 1
    count = list(count.items())
    if len(count) == 0:
        return []
    count = sorted(count, key=lambda c: (-c[1], c[0]))
    return [category for category, _ in count[0:5]]
