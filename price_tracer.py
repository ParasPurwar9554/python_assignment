import requests
from bs4 import BeautifulSoup

class priceTracer:
    def __init__(self,url):
        self.url = url
        self.user_agent  = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"}
        self.response = requests.get(url=self.url,headers=self.user_agent).text
        self.soup = BeautifulSoup(self.response,"html.parser")

    def product_title(self):
        title = self.soup.find("span",{"id":"productTitle"})
        if title is not None:
            return title.text.strip()
        else:
            return "Tag Not Found!"

    def product_price(self):
        price = self.soup.find("span",{"class":"a-price-whole"})
        if price is not None:
            return price.text.strip()
        else:
            return "Tag Not Found!"  

device = priceTracer(url="https://www.amazon.in/Samsung-Awesome-Storage-Nightography-Corning/dp/B0CWPBBQ3M/ref=sr_1_3?crid=1JVZ72UG3X1ZY&dib=eyJ2IjoiMSJ9.FbLNFBUCbOTGjKf_SeZN2Dw9wmLxDGzFfBEJj4bU3Bg1hJmJJt4X4Z71q8BBqnwoXn5iH6sm7_kPpkbzAQ2FcUv0IpSFWTp1D49Ot0aCLDOtmZZa0KVfANDJndyjd2JPbWF921RhHW2AjVjfQ8vm8B-HuWPlhlkXJzJRNnfsrDXcILV-3MmF96TUf84ICjVchLbqYDIspl5zQlpVL_wNMk9y1j1XvV2qBNm0gVBECd4.DFIjwThb3qlFrUk5VRULu35pK5E27wM5Q2m9BWUVUqs&dib_tag=se&keywords=samsung%2Bgalaxy%2BS10%2Bmobile&qid=1765618504&sprefix=samsung%2Bgalaxy%2Bs10%2Bmobile%2Caps%2C259&sr=8-3&th=1")

print(device.product_title())
print(device.product_price())

samsung_device = priceTracer(url="https://www.amazon.in/amazon-basics-Samsung-Galaxy-M06/dp/B0FHB1NW3Q/ref=pd_dp_d_dp_dealz_etdr_d_sccl_1_3/257-9526445-8074335?pd_rd_w=jbZl4&content-id=amzn1.sym.aef73018-e935-4f38-8aa6-34add793f754&pf_rd_p=aef73018-e935-4f38-8aa6-34add793f754&pf_rd_r=YPG1QE38QRQQT4ZFZDZA&pd_rd_wg=0WzY8&pd_rd_r=2dc375d8-4da0-4a45-8935-1753b41711fb&pd_rd_i=B0FHB1NW3Q&psc=1")

print(samsung_device.product_title())
print(samsung_device.product_price())