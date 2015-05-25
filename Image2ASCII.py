from bisect import bisect_right
import random
import warnings

from PIL import Image

#Characters grouped into 'visual weight'
grayscale =  [" ",
              " ",
              ".,-",
              "_ivc=!/|\\~",
              "gjez2]/(YL)t[+T7Vf",
              "mdK4ZGbNDXY5P*Q",
              "W8KMA",
              "$&#%"]

#Benchmarks for when to use which character set
thresholds=[36,72,108,144,180,216]

def image2ASCII(im, scale=200, showimage=False):
	if showimage:
		im.show()
	#Make sure an image is selected
	if im == None:
		raise ValueError, "No Image Selected"

	#Make sure the output size is not too big
	if scale > 200:
		warnings.warn("Image cannot be more than 200 characters wide")
		scale = 200

	#Crop the image to be the largest possible square
	if im.size[0] > im.size[1]:
		im = im.crop((0, 0, im.size[1], im.size[1]))
	elif im.size[0] < im.size[1]:
		im = im.crop((0, 0, im.size[0], im.size[0]))

	#Shrink the image down to 200x200, then convert to grayscale.
	im = im.resize((scale,int(scale*0.5)),Image.BILINEAR).convert('L')

	#Begin with an empty string that will be added on to to create the image
	output=''

	#Create the ASCII string by assigning a character of appropriate
	#weight to each pixel
	for y in range(im.size[1]):
		for x in range(im.size[0]):
			luminosity = 255-im.getpixel((x,y))
			row=bisect_right(thresholds, luminosity)
			possiblechars = grayscale[row]
			output += possiblechars[random.randint(0,len(possiblechars)-1)]
		output += '\n'

	#return  the final string
	return output
