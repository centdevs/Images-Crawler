from sys import implementation
import requests, bs4

base_url = "https://www.freeimages.com/"
html = requests.get(base_url)
soup = bs4.BeautifulSoup(html.content, 'html.parser')

gridContainer = soup.find("div", class_="grid-container")


for imgClass in gridContainer.find_all("div", class_="grid-item rounded-sm overflow-hidden"):
    imgRef = imgClass.find("a")['href']
    imgTitle = imgRef.replace("/photo/", "")

    
    urlImg = "https://www.freeimages.com" + imgRef
    soupPhotoPage = bs4.BeautifulSoup(requests.get(urlImg).content, 'html.parser')
    
    photoWrapper = soupPhotoPage.find("div", id="photo-wrapper")
    imgSrc = photoWrapper.find("img")['src']
    
    # instead lets use image names
    
    with open(f"{imgTitle}.jpg", "wb+") as imgfile:
        dat = requests.get(imgSrc)
        imgfile.write(dat.content)
    print(f"Image {imgTitle} downloaded and saved to {imgTitle}.jpg")


  
    


