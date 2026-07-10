from smtplib import SMTP
import os
from scraping import PriceScrap

EMAIL=os.environ.get("EMAIL_ADDRESS")
PASSWORD=os.environ.get("MAIL_PASS")
product_link="https://www.amazon.com/Ray-Ban-Wayfarer-Matte-Black-Smart-Glasses/dp/B0FLYDWQDZ/ref=sr_1_1?_encoding=UTF8&content-id=amzn1.sym.69a935ef-cee6-41d5-aefa-c36bfc7821bc&dib=eyJ2IjoiMSJ9.a6i2Sg5JloqUkFYCh0j7QMR8A2mH4vDqPC14D787igDClsWvWKwU1koVRRcqZIRJtyjRoFLXsnYqYseOeXXORpFMeKvX_exMMVz3qiw0M-z2aHya7qFDsACK4LouJTxvYYoJPSkYKa1FK7mCUUp3OT90JXfbGGSdFxygbKl4NTIoiyXz73_k5wMhE18tDTNWGusMCt8H2us29fVjAkwrpLx6V6gj8scnaFMIUeWeMig.Pg4pfhKdphlrqQFjOqjXqoWwv6F_9SK39-Rd-eadhMY&dib_tag=se&keywords=electronics&pd_rd_r=df3afdc7-00ab-45c4-86fd-ddd0bbdec530&pd_rd_w=CEwLi&pd_rd_wg=4ug7f&qid=1783688851&sr=8-1&th=1"
class SendMail():
    def __init__(self,current,target,product_details):
        self.current_price=current
        self.target_price=target
        self.details=product_details
        self.send_mail()

    def send_mail(self):
        msg_text = (f"Subject:Amazon Alert!!\n\nThe META Glasses current price which is {self.current_price}$ "
        f"is now lower than the target price which is {self.target_price}$\n"
        f"Here are the product details:\n"
        f"{self.details}\n\n\n"
        f"Here you can buy the product:\n"
        f"{product_link}")
        with SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=EMAIL,to_addrs=EMAIL
                            ,msg=msg_text.encode('utf-8'))
        print("Email sent successfully!")



