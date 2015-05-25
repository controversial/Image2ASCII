from Image2ASCII import *
image = Image.open("Test_Images/Calvin.jpg") #Open the image
ascii = image2ASCII(image)                   #Convert the image to ASCII
outputimage = RenderASCII(ascii)             #Render the ASCII
outputimage.show()                           #Show the final product
