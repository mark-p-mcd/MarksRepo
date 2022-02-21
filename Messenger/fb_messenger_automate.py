import pyautogui
import time
import webbrowser

# working method to start default browser from cmd 
# os.system('cmd /k "start https://www.messenger.com/t/513794188"')

webbrowser.open_new('https://www.messenger.com/t/4326842437416958')
pyautogui.moveTo(x=688, y=996, duration=6)
pyautogui.click(x=688, y=996, button='left')
localtime = time.asctime(time.localtime(time.time()))
pyautogui.typewrite('Hello! The local datetime is '+ localtime + '... please complete Wordle in less than 6 tries.')
pyautogui.press('enter')
pyautogui.typewrite('https://www.powerlanguage.co.uk/wordle/')
pyautogui.press('enter')
