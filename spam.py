import pyautogui,time
x=0
numSpam = int(input("how many?:"))
spamMessage = input("Message")
time.sleep(5)

while x!=numSpam:
    pyautogui.typewrite(spamMessage + "<-- //This spam is brought to you by dnxiego")
    pyautogui.press("enter")
    x+=1