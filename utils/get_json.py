'''
Features to be extracted from json data:
    Primary Image - images[0]['src']
    Title - title
    Price - variants[0]['price']

{
  "templateName": "rhombus",
  "media": [
    "http://res.cloudinary.com/xplanck/image/fetch/c_pad,h_600,w_600/https://www.fancypantsthestore.com/media/catalog/product/cache/1/thumbnail/600x800/9df78eab33525d08d6e5fb8d27136e95/_/m/_mg_0929_1_1_1.jpg",
    "http://cdn2.momjunction.com/wp-content/uploads/2016/01/Colorful-Layering.jpg",
    "http://www.fashionisers.com/wp-content/uploads/2012/11/how_to_wear_neon_clothing.jpg",
    "https://i.pinimg.com/736x/8e/2b/20/8e2b206e81178b9822ed7c80de02ad2b--into-the-blue-summer-work-outfits.jpg",
    "https://static1.squarespace.com/static/56074f7ce4b03eb8da80cc79/56d70e64859fd0120ac25cab/56d70e64ab48dec1b1329c04/1459372438835/jennifer-lake-most-colorful-bloggers-style-charade+4.jpg"
  ],
  "productName": [
    "Scarf",
    "Yellow Caps",
    "Peach Skirt Scandinavian",
    "Zebra Skirt Black & White",
    "Fashion"
  ],
  "price": [
    "$89.999",
    "$89.9999",
    "$89.99999",
    "$89.9999999",
    "$89.99999999"
  ],
  "videoLength": 12,
  "audio": true
}
'''
import requests,json
from .datesort import ds
productName=[]
price=[]
media=[]
videoLength=12
audio="true"
currency = "$"
dic={}
def get_json(templateName,url,c):
    global currency
    currency = str(c)
    url+="/products.json/"
    src = requests.get(url)

    if(src.status_code == 200):
        data = json.loads(src.text)
        data=data['products']
        return extract(data,sorter(data),templateName),src.reason
    elif(src.status_code == 404):
        return None,"Not a shopify website!"
    else:
        return None,src.reason


def sorter(products):
    list=[]
    for i in products:
        list.append(i['published_at'])
    return ds(list)

def extract(products,list,templateName):
    for i in list:
        productName.append(products[i]['title'])
        price.append(str(currency)+str(products[i]['variants'][0]['price']))
        media.append(products[i]['images'][0]['src'])
    dic["templateName"]=templateName
    dic["productName"]=productName
    dic["price"]=price
    dic["media"]=media
    dic["videoLength"]=videoLength
    dic["audio"]=audio
    print("Fetching product details...")
    final_json=json.dumps(dic)
    return final_json
