import requests
import turtle
import time
from PIL import Image

apiKey = 'DEMO_KEY'
req = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + apiKey)
dados = req.json()
req = requests.get(dados['url'])
with open("PictureOfTheDay.jpg", "wb") as f:
    f.write(req.content)
time.sleep(5)
img = Image.open("PictureOfTheDay.jpg", "r")
img.save("PictureOfTheDay.gif", "GIF")

screen = turtle.Screen()
screen.setup(720, 360)
screen.title("NASA Astronomical Picture of the Day")
screen.bgpic('PictureOfTheDay.gif')
while True:
    screen.update()
