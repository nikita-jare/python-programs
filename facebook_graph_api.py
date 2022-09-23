import os
import requests

url = "https://graph.facebook.com/{}/picture?type=large"

if not "fb_pictures" in os.listdir("./output/"):
    os.mkdir("./output/fb_pictures")

for i in range(10,20):
    result = requests.get(url.format(i))
    with open("./output/fb_pictures/{}_img.jpg".format(i), "wb") as file:
        file.write(result.content)
