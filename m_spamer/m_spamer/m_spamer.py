
### Spam program ###
import os, sys
import pyautogui as pyau
from time import sleep

# list of images
discord_home = os.path.join(sys.path[0], 'discord_home.png')

discord_gear = os.path.join(sys.path[0], 'Discord_Gear.png')

discord_name = os.path.join(sys.path[0], 'discord_name.png')


# failsafe
pyau.FAILSAFE = True

# grabs the list of words to send from the writen txt flie
with open(os.path.join(sys.path[0], 'Bees.txt'), 'r+') as wor:
    word = wor.read()
    words = word.split(' ')
    count = len(words)

# finds where to write
pyau.typewrite(['win'])
pyau.typewrite('discord')
pyau.typewrite(['enter'])
sleep(0.5)
img = pyau.screenshot()

try:
    name = pyau.locateCenterOnScreen(discord_name)
    pyau.moveTo(name)
    pyau.moveRel(0, 40)
    pyau.click()
except Exception as e:
    print(e)
finally:
    sleep(0.5)
    img = pyau.screenshot()
    gear = pyau.locateCenterOnScreen(discord_gear)
    pyau.moveTo(gear)
    pyau.moveRel(100, -25)
    pyau.click()


# starts writing\sending the word list
for i in range(count):
    phrase = str(words[i])
    pyau.typewrite(phrase, interval = 0.08)
    pyau.typewrite(['enter'])
    pyau.PAUSE = 0.35
