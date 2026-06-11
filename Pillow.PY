#Pillow

from PIL import Image

img = Image.open("photo.jpg")

print(img.size)

img.show()