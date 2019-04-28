from PIL import Image
#pil_im = Image.open('phot.jpg')
pil_im = Image.open('phot.jpg')
out =pil_im.resize((128,128))
out.show()
out = pil_im.rotate(45)
out.show()

