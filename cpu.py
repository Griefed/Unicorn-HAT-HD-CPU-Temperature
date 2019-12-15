#!/usr/bin/env python

import colorsys
import time
from gpiozero import CPUTemperature
from PIL import Image, ImageDraw, ImageFont
import unicornhathd

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
		for scroll in range(text_width - width+ 90):
			for x in range(width):
				if cpu.temperature <= 35:
					hue = (x + scroll) / float(text_width)
				else:
					hue = 0.0 #red
				br, bg, bb = [int(n * 255) for n in colorsys.hsv_to_rgb(hue, 1.0, 1.0)]
				for y in range(height):
					pixel = image.getpixel((x, y))
					r, g, b = [float(n / 255.0) for n in pixel]
					r = int(br * r)
					g = int(bg * g)
					b = int(bb * b)
					unicornhathd.set_pixel(width -1 -x, y, r, g, b)
			unicornhathd.show()
			time.sleep(0.02)

except KeyboardInterrupt:
	unicornhathd.off()
