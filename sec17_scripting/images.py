import json
from PIL import Image, ImageFilter

img = Image.open('./Pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.BLUR)
crooked = filtered_img.rotate(45)
crooked.save('blur.png', 'png')

grey_img = img.convert('L')
grey_img.save("grey.png", 'png')

rez = grey_img.resize((300,30))
rez.save("tiny.png", 'png')

box = (100, 100, 400, 400)
crop = filtered_img.crop(box)
crop.save("crop.png", 'png')

grey_img.show()

print(img.format)
print(img.size)
print(dir(img))


