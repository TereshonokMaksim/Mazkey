import turtle
import screen
import buttons
import turtles
import chooses
import data
import time
# import launcher
if data.start != 1:
    chooses.color_choose()
    start = 1

screen.screen.onclick(buttons.click_color_choose, add=True)

print("test")
turtle.mainloop()