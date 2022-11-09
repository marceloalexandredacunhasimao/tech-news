import requests
from parsel import Selector
import time
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    time.sleep(1)
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, timeout=3, headers=headers)
        if response.status_code != 200:
            return None
        return response.text
    except requests.ReadTimeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    return selector.css(".entry-title a::attr(href)").getall()


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    return selector.css(".next.page-numbers::attr(href)").get()


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel=canonical]::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author a::text").get()
    comments_count = selector.css("#comments .title-block::text").get()
    if not comments_count:
        comments_count = 0
    else:
        comments_count = int(comments_count.strip().split(" ")[0])
    # summary = selector.css(".entry-content p::text").get().strip()
    summary = selector.css(".entry-content > p:first-of-type *::text").getall()
    summary = "".join(summary).strip()
    # print("<<<<<"+summary+">>>>>")
    tags = selector.css(".post-tags ul li a::text").getall()
    category = selector.css("span.label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    count = 0
    news = []
    next = "https://blog.betrybe.com/"
    # next = scrape_next_page_link(next)
    while count < amount:
        response = fetch(next)
        pages_links = scrape_novidades(response)
        for page_link in pages_links:
            news.append(scrape_noticia(fetch(page_link)))
            count += 1
            if count == amount:
                break
        next = scrape_next_page_link(response)
        if not next:
            break
    create_news(news)
    return news
