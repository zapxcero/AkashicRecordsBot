from bs4 import BeautifulSoup
import cloudscraper


def to_url(string):
    return string.replace(" ", "-").lower().replace("'", "").replace("’", "")


SITE_LINK = "https://novelupdates.com"


class Novel:
    def __init__(self, title):
        self.title = title
        self.link = f"{SITE_LINK}/series/{to_url(title)}/"

        source = cloudscraper.create_scraper().get(self.link).content
        soup = BeautifulSoup(source, "lxml")

        self.genre = soup.find("div", id="seriesgenre").text.strip().replace(" ", ", ")
        self.rating = soup.find("span", class_="uvotes").text.strip()
        self.language = soup.find("div", id="showlang").text.strip()
        self.author = soup.find("a", id="authtag").text.strip()
        self.author_link = soup.find("a", id="authtag")["href"].strip()
        self.status = soup.find("div", id="editstatus").text.strip()

    def formatted_reply(self):
        return (
            f"[**{self.title}**]({self.link}) ({self.language}) by [{self.author}]({self.author_link})\n"
            f"\n"
            f"Genre: {self.genre}\n"
            f"\n"
            f"Status: {self.status}\n"
        )
