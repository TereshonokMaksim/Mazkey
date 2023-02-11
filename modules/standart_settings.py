import turtles
import data
import chooses
def rectangle(width,height,angle):
    turtles.t_mazeer.begin_fill()
    for i in range(2):
        turtles.t_mazeer.forward(width)
        turtles.t_mazeer.left(angle)
        turtles.t_mazeer.forward(height)
        turtles.t_mazeer.left(angle)
    turtles.t_mazeer.end_fill()
def kill():
    turtles.t_player.goto(-175,-25)
    data.deaths += 1
def level_complete():
    data.level += 1

    # turtles.t_player.speed(0)
    turtles.t_player.goto(-175,-25)
    # turtles.t_player.speed(5)

    data.coin = [0,0]
    turtles.t_mazeer.clear()
    chooses.build_standart_border()
def scan_movement():
    x = turtles.t_player.xcor()
    y = turtles.t_player.ycor()
    if x > 200:
        turtles.t_player.goto(x - 20, y)
    if x < -200:
        turtles.t_player.goto(x + 20, y)
    if y > 200:
        turtles.t_player.goto(x, y - 20)
    if y < -200:
        turtles.t_player.goto(x, y + 20)