from bs4 import BeautifulSoup
import cloudscraper  # 1. بنستدعي المكتبة الجديدة هنا


class PriceScrap():
    def __init__(self, url):
        self.url = url

        # 2. بنعمل سيسشن ذكي يقدر يتخطى الحماية
        scraper = cloudscraper.create_scraper()

        # 3. بنخليه هو اللي يجيب الصفحة بدل requests العادية
        self.response = scraper.get(url=self.url)
        self.web_page = self.response.text
        self.soup = BeautifulSoup(self.web_page, "html.parser")

    def scraping_price(self):
        price_whole = self.soup.select_one(selector="span.a-price-whole")

        # الحماية اللي بتمنع الكود ينهار لو أمازون لسه رخم
        if not price_whole:
            print("تنبيه: أمازون حظر السيرفر ومقدرناش نقرأ السعر المرة دي.")
            return 999999.0

        price_whole_value = price_whole.getText().strip(".")
        price_fraction = self.soup.find(name="span", class_="a-price-fraction")
        price_fraction_value = price_fraction.getText() if price_fraction else "00"

        the_whole_price = price_whole_value + "." + price_fraction_value
        clean_price = the_whole_price.replace(",", "")
        return float(clean_price)

    def scraping_title(self):
        product_title = self.soup.select_one("#productTitle")
        return product_title.getText().strip() if product_title else "منتج غير معروف"
