from PIL import Image

#I am sorry doing my homework the bad way - completelly using PIL
#1. scaling image using particulat pixels (newSizeXY), don't keep aspect ratio
def scaleImage(inputFile, outputFile, newSizeX, newSizeY):
    image = Image.open(inputFile)
    if (newSizeX > 0) and (newSizeY > 0):
        newim = image.resize((newSizeX, newSizeY), Image.ANTIALIAS)
        newim.save(outputFile)

#2. 3 filtres remove 3 corol from the RGB specter (it is like one function) *but it was fun to do more this stuff)
def removeRed(inputFile, outputFile):
    image = Image.open(inputFile)
    newim = image.load()
    s = image.size
    for x in range(s[0]):
        for y in range(s[1]):
            r, g, b = newim[x, y]
            newim[x, y] = 0, g, b
    image.save(outputFile)
    
def removeGreen(inputFile, outputFile):
    image = Image.open(inputFile)
    newim = image.load()
    s = image.size
    for x in range(s[0]):
        for y in range(s[1]):
            r, g, b = newim[x, y]
            newim[x, y] = r, 0, b
    image.save(outputFile)
    
def removeBlue(inputFile, outputFile):
    image = Image.open(inputFile)
    newim = image.load()
    s = image.size
    for x in range(s[0]):
        for y in range(s[1]):
            r, g, b = newim[x, y]
            newim[x, y] = r, g, 0
    image.save(outputFile)

#3. function for multiply colors from RGB, but there is a problem with float (please just integer)
def multiplyColors(inputFile, outputFile, redCoef, greenCoef, blueCoef):
    image = Image.open(inputFile)
    newim = image.load()
    s = image.size
    for x in range(s[0]):
        for y in range(s[1]):
            r, g, b = newim[x, y]
            newim[x, y] = r * redCoef, g * greenCoef, b * blueCoef
    image.save(outputFile)

#4. i use another part of PIL library (againg feeling sadness and disability)
from PIL import ImageOps
def invertColors(inputFile, outputFile):
    image = Image.open(inputFile)
    newim = ImageOps.invert(image)
    newim.save(outputFile)

def mirrorImage(inputFile, outputFile):
    image = Image.open(inputFile)
    newim = ImageOps.mirror(image)
    newim.save(outputFile)

#5. add colorful border with PIL
def addWhiteBorder(inputFile, outputFile, borderSize, color):
    image = Image.open(inputFile)
    bordim = ImageOps.expand(image, borderSize, color)
    bordim.save(outputFile)

#6. draw and write into the image
from PIL import ImageDraw, ImageFont
def drawCircle(inputFile, outputFile, color):
    image = Image.open(inputFile)
    drawim = ImageDraw.Draw(image)
    drawim.ellipse((120, 30, 160, 60), color)
    image.save(outputFile)

def writeSent(inputFile, outputFile, text, color):
    image = Image.open(inputFile)
    writim = ImageDraw.Draw(image)
    writim.text((100, 100), text, color)
    fontsFolder = 'FONT_FOLDER'
    image.save(outputFile)


def demo(inputFile):
    scaleImage(inputFile , "out1.png", 640, 0)
    removeRed(inputFile, "out2.png")
    removeGreen(inputFile, "out3.png")
    removeBlue(inputFile, "out4.png")
    multiplyColors(inputFile , "out5.png", 1, 2, 1)
    invertColors(inputFile , "out6.png")
    mirrorImage(inputFile, "out7.png")
    addWhiteBorder(inputFile , "out8.png", 10, "white")
    drawCircle(inputFile , "out9.png", "red")
    writeSent(inputFile , "out10.png", "Just a message", "blue")

demo("moonm.jpg")
#it's really simple but I like it ;) and I really have fun thank you :)
#and I don't expect that I will have full-point homework
