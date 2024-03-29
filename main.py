import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
THRESHOLD_PRICE = 100
product_url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.7",
    "sec-ch-ua-platform": "Windows",
    "Accept-Encoding": "gzip, deflate, br",
    # "Host": "myhttpheader.com",
    "Content-Type": "application/pdf",
    # "Content-Length": "1708",
    # "Cache-Control": "max-age=0",
    # "Accept-Charset": "utf-8"

}
request = requests.get(url=product_url, headers=headers)
# print(request.text)
soup = BeautifulSoup(request.text, "lxml")
price_line = soup.find(name="span", class_="a-offscreen")
price = float(price_line.getText().replace("$", ""))
if price <= THRESHOLD_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login("pythonsurbhi@gmail.com", "SECRET KEY")
        connection.sendmail(
                from_addr="pythonsurbhi@gmail.com",
                to_addrs="sonisurbhi2003@gmail.com",
                msg=f"Subject:Low price for Amazon Product\n\nPrice {price} for link :{product_url}".encode('utf-8')
            )
