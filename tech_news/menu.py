import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import search_by_title, search_by_date
from tech_news.analyzer.search_engine import search_by_tag, search_by_category
from tech_news.analyzer.ratings import top_5_news, top_5_categories


def search(option):
    if option == 1:
        result = search_by_title(input("Digite o título:"))
    elif option == 2:
        result = search_by_date(input("Digite a data no formato aaaa-mm-dd:"))
    elif option == 3:
        result = search_by_tag(input("Digite a tag:"))
    elif option == 4:
        result = search_by_category(input("Digite a categoria:"))
    return result


def rating(option):
    if option == 5:
        result = top_5_news()
    elif option == 6:
        result = top_5_categories()
    return result


def menu(option):
    if option < 0 or option > 7:
        print("Opção inválida", file=sys.stderr)
    elif option == 0:
        result = int(input("Digite quantas notícias serão buscadas:"))
        return get_tech_news(result)
    elif option < 5:
        return search(option)
    elif option < 7:
        return rating(option)
    else:
        print("Encerrando script")
        return None


def main_menu(option):
    option = int(option)
    result = menu(option)
    if result:
        print(result)


# Requisito 12
def analyzer_menu():
    option = input("""Selecione uma das opções a seguir:
 0 - Popular o banco com notícias;
 1 - Buscar notícias por título;
 2 - Buscar notícias por data;
 3 - Buscar notícias por tag;
 4 - Buscar notícias por categoria;
 5 - Listar top 5 notícias;
 6 - Listar top 5 categorias;
 7 - Sair.""")
    try:
        main_menu(option)
    except Exception as error:
        print(error, file=sys.stderr)
