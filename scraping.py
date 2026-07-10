from bs4 import BeautifulSoup
import requests

class PriceScrap():
    def __init__(self,url):
        self.url=url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Connection": "keep-alive"
        }
        self.response=requests.get(url=self.url,headers=self.headers)
        self.web_page=self.response.text
        self.soup=BeautifulSoup(self.web_page,"html.parser")

    def scraping_price(self):
        price_whole=self.soup.select_one(selector="span.a-price-whole")
        price_whole_value=price_whole.getText()
        price_fraction=self.soup.find(name="span",class_="a-price-fraction")
        price_fraction_value=price_fraction.getText()
        the_whole_price=price_whole_value+price_fraction_value
        clean_price=the_whole_price.replace(",","")
        the_whole_price_num=float(clean_price)
        return the_whole_price_num

    def scraping_title(self):
        product_title=self.soup.select_one("#productTitle")
        product_title_text=product_title.getText()
        return product_title_text




