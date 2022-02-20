import board
import digitalio
from PIL import Image, ImageDraw, ImageFont, ImageOps
import adafruit_ssd1306
import time
from datetime import datetime

WIDTH = 128
HEIGHT = 64
BORDER = 5
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C)

oled.fill(0)
oled.show()

top = BORDER
bottom = HEIGHT-BORDER
x = BORDER
font = ImageFont.truetype("Gidole-Regular.ttf", size=15)

def display_emotion(emotion):
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    image = Image.new('1', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    
    draw.text((WIDTH-55, 0), current_time, font=font, fill=255)
    draw.text((0, 0), 'E',  font=font, fill=255)
    draw.text((x, top+25), f'{emotion}', font=font, fill=255)
    
    image = ImageOps.flip(image)
    image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    oled.image(image)
    oled.show()

def display_weather(weather):
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    image = Image.new('1', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    
    draw.text((WIDTH-55, 0), current_time, font=font, fill=255)
    draw.text((0, 0), 'W',  font=font, fill=255)
    if weather == "Offline":
        draw.text((x, top+14), 'Offline:',  font=font, fill=255)
        draw.text((x, top+28), 'Weather not available', font=font, fill=255)
    else:
        draw.text((x, top+25), weather, font=font, fill=255)
    
    image = ImageOps.flip(image)
    image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    oled.image(image)
    oled.show()

def display_schedule(schedule):
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    for event in schedule:
        image = Image.new('1', (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(image)
        draw.text((WIDTH-55, 0), current_time, font=font, fill=255)
        draw.text((0, 0), 'S',  font=font, fill=255)
        draw.text((x, top+25), event,  font=font, fill=255)
        image = ImageOps.flip(image)
        image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
        oled.image(image)
        oled.show()
        time.sleep(3)

def display_logo(path):
    image = Image.open(path)
    image = ImageOps.flip(image)
    image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    image = image.resize((128, 64))
    image = image.convert('1')
    image.show()
    oled.image(image)
    oled.show()