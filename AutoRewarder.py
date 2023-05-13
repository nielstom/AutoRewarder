import keyboard
from time import sleep
from random_word import RandomWords
from random import randint

# Open edge
keyboard.press_and_release('win+r')
sleep(1)
keyboard.write('microsoft-edge:')
keyboard.press_and_release('enter')
sleep(2)

# Run 12 bing searches from edge (only need 10, but bonus 2 to make sure all 10 are counted)
nSearches = 12
r = RandomWords()
for i in range(nSearches):
    keyboard.write(r.get_random_word())
    keyboard.press_and_release('enter')
    sleep(0.5)
    keyboard.press_and_release('ctrl+t')
    sleep(0.5)

# Close edge
sleep(1)
keyboard.press_and_release('alt+f4')
