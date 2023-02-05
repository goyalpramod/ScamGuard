from bs4 import BeautifulSoup as bs
import requests, re
url="https://www.apkmirror.com/uploads/"
HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Cache-Control": "max-age=0",
    }
req=requests.get(url, headers=HEADERS)

soup = bs(req.text, "html.parser")
# print(soup.title)
links=soup.find_all(class_='downloadLink')
links=["https://www.apkmirror.com"+link['href'] for link in links]
# print(links)
# print(len(links))
def get_desc(link, head=HEADERS):         #gets description
    req=requests.get(link, headers=head)

    soup = bs(req.text, "html.parser")
    texts=soup.find_all("p")
    textDes=''
    for i in texts:
        textDes+=i.text
    return textDes

def save_img(link, head=HEADERS):           #takes_photo
    req=requests.get(link, headers=head)
    soup = bs(req.text, "html.parser")
    imageLink=soup.find(class_="ellipsisText")
#     return imageLink
    with open("logo.png", "wb") as data:
        data.write(requests.get("https://www.apkmirror.com"+imageLink['src']).content)
    return 0

# def getDLink(link, head=HEADERS):
#     req=requests.get(link, headers=head)
#     soup = bs(req.text, "html.parser")
#     dLink=soup.find(class_="downloadButton")
#     apkLink = "https://www.apkmirror.com"+dLink['href']
#     req=requests.get(apkLink, headers=head, allow_redirects=True)
# 
# #     return imageLink
#     with open("x.apk", 'wb') as file:
#         for chunk in req.iter_content(chunk_size=1024): 
#             if chunk:
#                 file.write(chunk)
#         soup = bs(req.text, "html.parser")
#     
#     return dLink 
#     
#

# def downFile(link):
#     from selenium import webdriver
#     from selenium.webdriver.common.by import By
#     from selenium.webdriver.chrome.options import Options
#     #object of ChromeOptions
#     op = Options()
#     op.add_argument("--start-maximized")
#     prefs = {'safebrowsing.enabled': 'false', "profile.default_content_settings.popups": 0, "download.default_directory": "/home/sam/sel/", "directory_upgrade": True}
#     #set download directory path
#     op.add_experimental_option("prefs", prefs)
#     #p = ("download.default_directory": "/")
#     #adding preferences to ChromeOptions
# 
#     driver = webdriver.Chrome(executable_path="chromedriver", options=op)
#     driver.implicitly_wait(0.4)
#     driver.get(link)
    
#identify element

    


# print(get_desc(links[0]))
print(save_img(links[0]))
# print(getDLink(links[0]))

