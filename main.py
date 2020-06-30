import pyautogui

image = pyautogui.screenshot()
image.save('goldcoin.png')

greed = True
while (greed is True):
    try:
        coin = pyautogui.locateOnScreen('goldcoin.png')
        print(coin)

        coinx, coiny = pyautogui.center(coin)
        pyautogui.click(coinx, coiny)  # clicks the center of where the coin was found
    except:
        pass
