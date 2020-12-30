from PIL import Image, ImageDraw, ImageFont

font_size = 10
text = "新年快乐"
img_path = "1.jpg"

img_raw = Image.open(img_path)
img_array = img_raw.load()

img_new = Image.new("RGB", img_raw.size, (10, 10, 10))
draw = ImageDraw.Draw(img_new)
font = ImageFont.truetype('C:/Windows/fonts/Dengl.ttf', font_size)


def character_generator(text):
    while True:
        for i in range(len(text)):
            yield text[i]


ch_gen = character_generator(text)

for y in range(0, img_raw.size[1], font_size):
    for x in range(0, img_raw.size[0], font_size):
        draw.text((x, y), next(ch_gen), font=font,
                  fill=img_array[x, y], direction=None)

img_new.convert('RGB').save("new1.jpg")
