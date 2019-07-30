import requests
from bs4 import BeautifulSoup
import smtplib
URL = 'https://www.amazon.in/Philips-BG1024-Battery-Operated-Groomer/dp/B00YJ55SAY/ref=sr_1_5?keywords=body+shaver&qid=1564292504&s=gateway&sr=8-5'

#URL = 'https://www.amazon.in/Philips-Trimmer-Cordless-QT4001-15/dp/B00L8PEEAI/ref=sr_1_5?keywords=men+trimmer&qid=1564406747&s=gateway&sr=8-5'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    print (title.strip())
    print (price)
    converted_price = float ('.'.join(price [2:7].split(',')))
    

    print (title.strip())
    print (converted_price)

    if (converted_price <= 1.000):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('krunal@appliedcloudcomputing.com', 'acc12345')

    subject = 'Price Fell Down!'
    body = 'Check the amazon link -> https://www.amazon.in/Philips-BG1025-15-Showerproof-Groomer/dp/B00TO7K08C'

    msg = f"Subject:  {subject}\n\n{body}"

    server.sendmail(
        'krunal@appliedcloudcomputing.com',
        'spoison585@gmail.com',
        msg
    )
    print("HEY! MAIL HAS BEEN SENT.")
    server.quit()

check_price()