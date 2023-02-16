import turtle
import modules.screen as screen
import modules.buttons as buttons
import modules.chooses as chooses
import modules.data as data
if data.start != 1:
    chooses.color_choose()
    start = 1

screen.screen.onclick(buttons.click_color_choose, add=True)
turtle.done()