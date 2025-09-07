from PIL import Image
import pillow_avif
print("Hello World")
opnimg = Image.open('img1.avif') #converting avif to jpeg
opnimg.convert('RGB').save("img_converted.jpg",'JPEG')