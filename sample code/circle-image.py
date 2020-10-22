
from PIL import Image, ImageOps, ImageDraw

im = Image.open('D:\collegeproject\gui\image\ok.png')
im = im.resize((120, 120));
bigsize = (im.size[0] * 3, im.size[1] * 3)
mask = Image.new('L', bigsize, 0)
draw = ImageDraw.Draw(mask) 
draw.ellipse((0, 0) + bigsize, fill=255)
mask = mask.resize(im.size, Image.ANTIALIAS)
im.putalpha(mask)

output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
output.putalpha(mask)
output.save('D:\collegeproject\gui\image\ok.png')

background = Image.open('D:\collegeproject\gui\image\ok.png')
background.paste(im, (150, 10), im)
background.save('D:\collegeproject\gui\image\ok.png')