from PIL import Image, ImageFont, ImageDraw


def RenderASCII(text, fontsize=5):
    '''Create an image of the ASCII text'''
    first, _, _ = text.partition('\n')
    linelist=text.split('\n')
    size = len(first)
    font = ImageFont.truetype("DejaVuSansMono.ttf", fontsize*4)
    width, height = font.getsize(first)

    image = Image.new("RGB", (width, width), (237, 237, 237))
    draw = ImageDraw.Draw(image)

    for x in range(len(linelist)):
        line = linelist[x]
        draw.text((0, x*height), line, (0, 0, 0), font=font)
    return image
