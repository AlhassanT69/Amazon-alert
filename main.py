from email_manager import SendMail
from scraping import PriceScrap

URL="https://appbrewery.github.io/instant_pot/"
URL_2="https://www.amazon.com/Ray-Ban-Wayfarer-Matte-Black-Smart-Glasses/dp/B0FLYDWQDZ/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.69a935ef-cee6-41d5-aefa-c36bfc7821bc&dib=eyJ2IjoiMSJ9.a6i2Sg5JloqUkFYCh0j7QMR8A2mH4vDqPC14D787igDClsWvWKwU1koVRRcqZIRJtyjRoFLXsnYqYseOeXXORpFMeKvX_exMMVz3qiw0M-z2aHya7qFDsACK4LouJTxvYYoJPSkYKa1FK7mCUUp3OT90JXfbGGSdFxygbKl4NTIoiyXz73_k5wMhE18tDTNWGusMCt8H2us29fVjAkwrpLx6V6gj8scnaFMIUeWeMig.Pg4pfhKdphlrqQFjOqjXqoWwv6F_9SK39-Rd-eadhMY&dib_tag=se&keywords=electronics&pd_rd_r=df3afdc7-00ab-45c4-86fd-ddd0bbdec530&pd_rd_w=CEwLi&pd_rd_wg=4ug7f&qid=1783688851&sr=8-1&th=1"
target_price=100000

scraper=PriceScrap(URL_2)
current_price=scraper.scraping_price()
title=scraper.scraping_title()
if current_price<target_price:
    mail=SendMail(current=current_price,target=target_price,product_details=title)
else:
    print(f"The price {current_price} is too high")


