# PvZ-Coin-Collection
In Plants vs. Zombies, the plants in Zen Garden drop coins or diamonds periodically. Given an image of coin/diamond, look for the coin/diamond on the screen and click the center to collect them.

# Environment & Requirement
OS: Windows 7\
Python: 3.6\
Package: pyautogui

# Setup and usage
1. `pip install pyautogui`
2. Capture a screenshot of the game using `pyautogui.screenshot()`
3. Manually crop the coin or diamond image and save it to a location
4. Pass location of image to `pyautogui.locateOnScreen()`

# Note
Capturing the image of coin using Window's screenshot function does not work. Must use pyautogui's screenshot() method.

# To-do
1. Refactor code for easier usage.
2. Code forces clicks too frequently; making mouse unusable.
3. Need to accommodate for different resolution window sizes.
