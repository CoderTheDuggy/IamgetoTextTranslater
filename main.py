import PIL.Image
import os

filePath = input('Please enter the path to your image: ')
print(filePath)
if os.path.exists(filePath):
    if os.path.isfile(filePath):
        image = PIL.Image.OPEN(filePath)

    else:
        print("File " + filePath + " isn't a file!")
else:
    print("File " + filePath + "doesn't exist!")


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
