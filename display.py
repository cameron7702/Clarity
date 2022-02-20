import board
import digitalio
from PIL import Image, ImageDraw, ImageFont, ImageOps
import adafruit_ssd1306
import time

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
font = ImageFont.load_default()

def display_emotion(emotion):
    image = Image.new('1', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    
    draw.text((0, 0), 'e',  font=font, fill=255,)
    draw.text((x, top), 'Emotion:',  font=font, fill=255,)
    draw.text((x, top+10), f'{emotion}', font=font, fill=255)
    
    image = ImageOps.flip(image)
    image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    oled.image(image)
    oled.show()

def display_weather(weather):
    image = Image.new('1', (WIDTH, HEIGHT))
    draw = ImageDraw.Draw(image)
    
    draw.text((0, 0), 'w',  font=font, fill=255,)
    if weather == "Offline":
        draw.text((x, top), 'Offline:',  font=font, fill=255,)
        draw.text((x, top+10), 'Weather not available', font=font, fill=255)
    else:
        draw.text((x, top), 'Today\'s weather:',  font=font, fill=255,)
        draw.text((x, top+10), weather, font=font, fill=255)
    
    image = ImageOps.flip(image)
    image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
    oled.image(image)
    oled.show()

def display_schedule(schedule):
    for event in schedule:
        image = Image.new('1', (WIDTH, HEIGHT))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), 's',  font=font, fill=255,)
        draw.text((x, top), event,  font=font, fill=255,)
        image = ImageOps.flip(image)
        image = image.transpose(method=Image.FLIP_LEFT_RIGHT)
        oled.image(image)
        oled.show()
        time.sleep(3)