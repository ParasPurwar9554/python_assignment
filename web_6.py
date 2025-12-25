import requests
import re
import os

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36"
}

user = input("Enter an image name: ")

url = f"https://www.google.com/search?q={user}&tbm=isch"

response = requests.get(url, headers=user_agent).text

pattern = r'\["https://.*?"\]'
images = re.findall(pattern, response)
print(f"Total Images: {len(images)}")
num_of_images = int(input("How many images to download : "))

if images:
    if not os.path.exists(user):  
       os.mkdir(user)
       os.chdir(user)
    else:
       os.chdir(user)
    for image in images[:num_of_images]:
        image_url = eval(image)[0]
        response = requests.get(url = image_url).content
        image_name = image_url.split('/')[-1]
        print(image_url)

        with open(image_name , "wb") as file:
            file.write(response)
