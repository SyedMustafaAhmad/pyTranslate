# Config
DIR_PATH = '/home/syedm/Pictures/'
IMG_NAME = 'tmp.png'
TRANSLATE_FROM = 'de'
TRANSLATE_TO = 'en'
SAVE_TO = '/home/syedm/Documents/workspace/translator/translated/'
OPEN_WITH = 'mousepad'

# Imports
import time
import subprocess
import pytesseract
from PIL import Image
from deep_translator import GoogleTranslator

def getText():
    image = Image.open(DIR_PATH + IMG_NAME)
    image_text = pytesseract.image_to_string(image)
    return image_text

def processText(orignal_text):
    return orignal_text.replace('\n', ' ')

def translateText(to_translate):
    translated = GoogleTranslator(source=TRANSLATE_FROM, target=TRANSLATE_TO).translate(to_translate)
    return translated

def saveTranslation(orignal_text, translated_text):
    time_str = time.strftime("%Y%m%d-%H%M%S")
    f = open(SAVE_TO + time_str + '.txt', "w")
    f.write(translated_text)
    f.write("\n\n" + '-'*10 + "\n\n")
    f.write(orignal_text)
    f.close()
    return time_str

def openFile(file_name):
    subprocess.call([OPEN_WITH, SAVE_TO + file_name + '.txt'])

orignal_text = getText()
to_translate = processText(orignal_text)
translated_text = translateText(to_translate)
file_name = saveTranslation(to_translate, translated_text)
openFile(file_name)
