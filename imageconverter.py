from PIL import Image
import pillow_avif

opnimg = Image.open('img1.avif')
opnimg.convert('RGB').save("img_converted.jpg",'JPEG')