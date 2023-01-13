import keyboard
from time import sleep

# Open edge
keyboard.press_and_release('win+r')
sleep(1)
keyboard.write('microsoft-edge:')
keyboard.press_and_release('enter')
sleep(1)

# Run 10 bing searches from edge
nSearches = 12
for i in range(nSearches):
    keyboard.write('search ' + str(i))
    keyboard.press_and_release('enter')
    sleep(0.5)
    keyboard.press_and_release('ctrl+t')
    sleep(0.5)

# Close edge
sleep(1)
keyboard.press_and_release('alt+f4')
