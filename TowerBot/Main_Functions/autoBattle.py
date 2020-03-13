from TowerBot.Helper_Functions.helperFunctions import findFightButton, findHurryBattle, percent, isOutOfEnergy
import pyautogui

import pyautogui, time

def auto_battle(P1, P2, coords, grindMode, grindAmount):
    arrow = (percent(97 ,(P2[0] - P1[0])) + P1[0], percent(97 ,(P2[1] - P1[1])) + P1[1]) # Define que a Arrow está a 99% em X e 97% em Y
    button = findFightButton(P1, P2)
    while not button:
        button = findFightButton(P1, P2)
        if not button:
            button = findFightButton(P1, P2)
            if not button:
                if isOutOfEnergy(P1, P2, grindMode, grindAmount):
                    time.sleep(0.5)
                    pyautogui.click(coords)
    pyautogui.click(button)
    time.sleep(0.5)
    while not findHurryBattle(P1, P2):
        continue
    pyautogui.click(arrow)
    time.sleep(1)
    pyautogui.click(arrow)