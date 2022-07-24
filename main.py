import PIL.Image
import os
import numpy
import sys


def logOK(msg):
    print('\033[92m[+] ' + msg + '\033[0m')


def logFATAL(msg):
    print('\033[91m[-] ' + msg + '\033[0m')


def logWARNING(msg):
    print('\033[93m[!] ' + msg + '\033[0m')


def getColorChar(rgbAverage):
    if 0 <= rgbAverage < 17:
        return '.'
    elif 17 <= rgbAverage < 34:
        return '_'
    elif 34 <= rgbAverage < 51:
        return '*'
    elif 51 <= rgbAverage < 68:
        return ':'
    elif 68 <= rgbAverage < 85:
        return '-'
    elif 85 <= rgbAverage < 102:
        return '~'
    elif 102 <= rgbAverage < 119:
        return '>'
    elif 119 <= rgbAverage < 136:
        return '/'
    elif 136 <= rgbAverage < 153:
        return '!'
    elif 153 <= rgbAverage < 170:
        return '|'
    elif 170 <= rgbAverage < 187:
        return '§'
    elif 187 <= rgbAverage < 204:
        return '&'
    elif 204 <= rgbAverage < 221:
        return '$'
    elif 221 <= rgbAverage < 238:
        return '%'
    elif 238 <= rgbAverage <= 255:
        return '#'


createFile = True
if len(sys.argv) > 1:
    if sys.argv[1] == "--no-file":
        createFile = False
        logWARNING("Save result to file disabled with arg --no-file!")
    else:
        logWARNING("The command line argument " + sys.argv[1] + " is unknown and skipped!" + (
            "(Along with " + str(len(sys.argv) - 2) + " other argument(s)!" if len(sys.argv) > 3 else ""))

filePath = input('\033[92m[+] Please enter the path to your image:\033[0m ')
if os.path.exists(filePath):
    if os.path.isfile(filePath):
        image = PIL.Image.open(filePath)
        width = input("\033[92m[+] Enter width (or nothing/0 to calculate it from height):\033[0m  ")
        width = width if width else 0

        height = input("\033[92m[+] Enter height (or nothing/0 to calculate it from width):\033[0m ")
        height = height if height else 0

        if not str(width).isnumeric():
            logFATAL("The width (" + width + ") is not numeric!")
            exit(0)
        if not str(height).isnumeric():
            logFATAL("The height (" + height + ") is not numeric!")
            exit(0)

        height = int(height)
        width = int(width)

        resultHeight = height
        resultWidth = width
        if height == 0 and width != 0:
            resultHeight = round(
                image.height * (image.width / width) if width > image.width else image.height / (image.width / width))
        elif height != 0 and width == 0:
            resultWidth = round(image.width * (image.height / height) if height > image.height else image.width / (
                        image.height / height))
        elif height == 0 and width == 0:
            logFATAL("Either height or width must be greater than 0!")
            exit(0)

        offset = input("\033[92m[+] Enter a offset for the text (or nothing to calculate the default offset):\033[0m ")
        if offset:
            if not str(offset).isnumeric():
                logFATAL("The offset must be numeric!")
                exit(0)
            else:
                offset = " "*int(offset)

        logOK("Creating text of image with dimension (HxW) " + str(resultHeight) + "x" + str(resultWidth) + "!")

        resizedImage = image.resize((resultHeight, resultWidth))
        result = ""
        pixels = resizedImage.load()

        for y in range(0, resizedImage.height):
            for x in range(0, resizedImage.width):
                rgb = numpy.array(pixels[x, y])
                rgbAverage = round((rgb[0] + rgb[1] + rgb[2]) / 3)
                colorChar = getColorChar(rgbAverage)
                if not offset:
                    if 100 <= resizedImage.height < 200 or 100 <= resizedImage.width < 200:
                        offset = " "
                    elif resizedImage.height >= 200 or resizedImage.width >= 200:
                        offset = " "*round(resizedImage.height / 2 / 100)
                print(colorChar + offset, end="")
                result = result + colorChar + offset
            print("")
            result = result + "\n"

        if createFile:
            resultFileName = "result-" + os.path.basename(filePath) + ".txt"
            file = open("./" + resultFileName, "w")
            file.write(result)
            file.close()
            logOK("Saved result to file " + resultFileName + "!")
    else:
        logFATAL("File " + filePath + " isn't a file!")
else:
    logFATAL("File " + filePath + "doesn't exist!")
