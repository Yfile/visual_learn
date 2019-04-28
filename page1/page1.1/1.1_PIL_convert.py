from PIL import Image
#pil_im = Image.open('phot.jpg')
pil_im = Image.open('phot.jpg').convert('L')
pil_im.show()

