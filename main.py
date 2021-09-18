import itertools

from modules.scrapping.scrapper import Scrapper
from modules.data_handling.handler import DataHandler

scrapper = Scrapper()
data_handler = DataHandler(columns=["title", "intro", "published", "link"])

if __name__ == '__main__':
    articles_summary = []
    for (year, month) in itertools.product([2019, 2020, 2021], (str(n) for n in range(1, 13))):
        parsed_page = scrapper.get_parsed_website(f"https://wiadrodanych.pl/{year}/{month.zfill(2)}")
        articles = parsed_page.find_all(name="article")

        for article in articles:
            try:
                articles_summary.append(scrapper.get_article_elements(article))
                data_handler.update_storage(articles_summary)
            except Exception as err:
                print(f"Error with an article from {year}/{month.zfill(2)}")
                print(str(err))
        print(f"Finished: {year}/{month.zfill(2)}")

    data_handler.export_to_excel("./output/articles_summary.xlsx")
