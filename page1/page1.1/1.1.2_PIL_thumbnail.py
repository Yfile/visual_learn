from PIL import Image
#pil_im = Image.open('phot.jpg')
pil_im = Image.open('phot.jpg')
pil_im.thumbnail((128,128))
pil_im.show()

