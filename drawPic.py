from PIL import Image
from PIL.ImageDraw import ImageDraw
from PIL.ImageFont import ImageFont

infile='F:\\temporaryFiles\\tou.png'
outfile = 'F:\\temporaryFiles\\tou2.png'
im = Image.open(infile)
draw = ImageDraw.Draw(im)
ttfront = ImageFont.truetype('simsun.ttc', 64)
draw.text("4")
im.save(outfile)
cao nima de gui tian da sha bi 
