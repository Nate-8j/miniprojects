import json
from PIL import Image, ImageFont, ImageDraw


font = ImageFont.truetype('a')

image = Image.open("/home/jk-n/Pictures/VersesBible/image0.jpg")
draw = ImageDraw.Draw(image)

with open("verses.json", "r", encoding="utf-8") as f:
    data = json.load(f)
    text = data[0]["verse"]
text_length = draw.textlength(text, font)
size = (image.size[0]-text_length-12, image.size[1]-32)
draw.text((40,40), text, font=font)
# draw.text(size, text=text, font=font, fill="black")

image.show()
