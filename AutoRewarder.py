import keyboard
from time import sleep

keyboard.press_and_release('win+r')
sleep(1)
keyboard.write('microsoft-edge:')
keyboard.press_and_release('enter')
sleep(1)

nSearches = 10
for i in range(nSearches):
    keyboard.write('search ' + str(i))
    keyboard.press_and_release('enter')
    sleep(0.5)
    keyboard.press_and_release('ctrl+t')
    sleep(0.5)

keyboard.press_and_release('alt+f4')
