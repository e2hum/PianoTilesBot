import pyautogui
import time
from mss import mss
from win32gui import GetForegroundWindow, GetWindowText

# Top left corner of game window.
start_x = 650
start_y = 560
gamebox = start_x, start_y, start_x + 510, start_y + 1

pos_x = [0, 170, 340, 500]

# Function used to test how long it takes to screenshot 100 times


def test_time():
    with mss() as sct:
        t1 = time.time()
        for i in range(100):
            img = sct.grab(gamebox)
        t2 = time.time()
        print(t2 - t1)


# test_time()

# Function for locating positions on the screen to check if there is a tile to be clicked
def print_mouse_pos():
    pyautogui.displayMousePosition()
    while True:
        print(pyautogui.position())
        time.sleep(1)


# print_mouse_pos()

# runs the bot
def start():
    YOUR_BROWSER = "Google Chrome"
    activeWin = ''
    while YOUR_BROWSER not in activeWin:
        activeWin = GetWindowText(GetForegroundWindow())

    with mss() as sct:
        while 'Google Chrome' in activeWin:
            activeWin = GetWindowText(GetForegroundWindow())
            img = sct.grab(gamebox)
            for pos in pos_x:
                if img.pixel(pos, 0)[0] < 100:
                    pyautogui.click(start_x + pos, start_y)
                    break


start()
