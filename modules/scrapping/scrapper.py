from datetime import datetime, timezone
from typing import Dict, Union

import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


class Scrapper:
    def __init__(self):
        pass

    def get_parsed_website(self, website_url: str) -> BeautifulSoup:
        page = requests.get(website_url)
        return BeautifulSoup(page.text, 'html.parser')

    def get_article_elements(self, article_obj: Tag) -> Dict[str, Union[str, datetime]]:
        title_obj = article_obj.find("h2", {"class": "entry-title"})
        time_obj = article_obj.find("time", {"class": "entry-date published"})
        published = datetime.strptime(time_obj.get("datetime"), '%Y-%m-%dT%H:%M:%S%z')

        return {
            "title": title_obj.text.title(),
            "link": title_obj.a.get('href'),
            "intro": article_obj.p.text.title(),
            "published": published.astimezone(timezone.utc).date()
        }
