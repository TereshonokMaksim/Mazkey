import turtle
import modules.screen as screen
import modules.buttons as buttons
import modules.turtles as turtles
import modules.chooses as chooses
import modules.data as data
import time
# import launcher
if data.start != 1:
    chooses.color_choose()
    start = 1

screen.screen.onclick(buttons.click_color_choose, add=True)
