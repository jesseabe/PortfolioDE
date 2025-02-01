import requests

URL = "https://api.nasa.gov/planetary/apod?api_key=tAqbMeZBZIJZKBgCejpGDrC9fNJgyhla2kiEWvft"

response = requests.get(URL)

imagem_path = response.json()['url']

print(requests.get(imagem_path).content)

image_data = requests.get(imagem_path).content

with open("imagem.jpg", "wb") as file:
    file.write(image_data)