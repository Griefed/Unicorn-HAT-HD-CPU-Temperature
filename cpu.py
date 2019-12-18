#!/usr/bin/env python

import colorsys
import time
from gpiozero import CPUTemperature
from PIL import Image, ImageDraw, ImageFont
import unicornhathd
import sys

print("""Unicorn HAT HD: CPU Temperature

Displays the CPU Temperature on your Unicorn HAT HD!
""")

FONT = ('/usr/share/fonts/truetype/piboto/PibotoCondensed-Regular.ttf', 12)

unicornhathd.rotation(270)
unicornhathd.brightness(0.3)

width, height = unicornhathd.get_shape()
text_x = 0
text_y = 0
font_file, font_size = FONT
font = ImageFont.truetype(font_file, font_size)
degree_sign= u'\N{DEGREE SIGN}'

try:
	while True:
		cpu = CPUTemperature()
		TEXT = (str(int(cpu.temperature))+degree_sign)
		text_width, text_height = font.getsize(TEXT)
		text_width += width + text_x
		image = Image.new('RGB', (text_width, max(height, text_height)), (0, 0, 0))
		draw = ImageDraw.Draw(image)
		draw.text((text_x, text_y), TEXT, fill=(255, 255, 255), font=font)
		if int(cpu.temperature) < 30.0:
			hue = 0.5
		elif int(cpu.temperature) >= 30.0 and int(cpu.temperature) < 35.0:
			hue = 0.4
		elif int(cpu.temperature) >= 35.0 and int(cpu.temperature) < 40.0:
			hue = 0.3
		elif int(cpu.temperature) >= 40.0 and int(cpu.temperature) < 45.0:
			hue = 0.2
		elif int(cpu.temperature) >= 45.0 and int(cpu.temperature) < 50.0:
			hue = 0.1
		elif int(cpu.temperature) >= 55.0:
			hue = 0.0
		for prolong in range(60): #Update every couple of seconds instead of several times per second
			for x in range(width):
				br, bg, bb = [int(n * 255) for n in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
				for y in range(height):
					pixel = image.getpixel((x, y))
					r, g, b = [float(n / 255.0) for n in pixel]
					r = int(br * r)
					g = int(bg * g)
					b = int(bb * b)
					unicornhathd.set_pixel(width - 1 -x, y, r, g, b)
			unicornhathd.show()
			time.sleep(0.02)

except KeyboardInterrupt:
	unicornhathd.off()
