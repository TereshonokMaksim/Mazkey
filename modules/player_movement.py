import modules.turtles as turtles
import modules.screen as screen
import modules.data as data
import modules.standart_settings as standart_settings
import modules.mazes.level_1 as lvl1
import modules.mazes.level_2 as lvl2
import modules.mazes.level_3 as lvl3
import time
def controls():
    def hitboxes_scan():
        standart_settings.scan_movement()
        if data.level == 1:
            lvl1.lvl_one_hitboxes(turtles.t_player.xcor(),turtles.t_player.ycor())
        elif data.level == 2:
            lvl2.level_two_hitboxes()
        elif data.level == 3:
            lvl3.level_three_hitboxes()
        elif data.level == "endscreen":
            if turtles.t_player.xcor() != -175 and turtles.t_player.ycor() != -25:
                standart_settings.kill()
    turtles.t_player.st()
    def up_key():
        for i in range(2):
            turtles.t_player.goto(turtles.t_player.xcor(), turtles.t_player.ycor() + 5)
            hitboxes_scan()
    def left_key():
        for i in range(2):
            turtles.t_player.goto(turtles.t_player.xcor() - 5, turtles.t_player.ycor())
            hitboxes_scan()
    def down_key():
        for i in range(2):
            turtles.t_player.goto(turtles.t_player.xcor(), turtles.t_player.ycor() - 5)
            hitboxes_scan()
    def right_key():
        for i in range(2):
            turtles.t_player.goto(turtles.t_player.xcor() + 5, turtles.t_player.ycor())
            hitboxes_scan()

    def jump_up():
        if data.jump_cooldown <= time.time() and data.jumping == 0:
            data.jump_cooldown = time.time() + 3
            data.jumping = 1
            for i in range(10):
                turtles.t_player.goto(turtles.t_player.xcor(), turtles.t_player.ycor() + 5)
                hitboxes_scan()
            data.jumping = 0
    def jump_left():
        if data.jump_cooldown <= time.time() and data.jumping == 0:
            data.jump_cooldown = time.time() + 3
            data.jumping = 1
            for i in range(10):
                turtles.t_player.goto(turtles.t_player.xcor() - 5, turtles.t_player.ycor())
                hitboxes_scan()
            data.jumping = 0
    def jump_down():
        if data.jump_cooldown <= time.time() and data.jumping == 0:
            data.jump_cooldown = time.time() + 3
            data.jumping = 1
            for i in range(10):
                turtles.t_player.goto(turtles.t_player.xcor(), turtles.t_player.ycor() - 5)
                hitboxes_scan()
            data.jumping = 0
    def jump_right():
        if data.jump_cooldown <= time.time() and data.jumping == 0:
            data.jump_cooldown = time.time() + 3
            data.jumping = 1
            for i in range(10):
                turtles.t_player.goto(turtles.t_player.xcor() + 5, turtles.t_player.ycor())
                hitboxes_scan()
            data.jumping = 0
    if data.controls == "WASD":
        screen.screen.listen()
        screen.screen.onkey(up_key, "w")
        screen.screen.onkey(left_key, "a")
        screen.screen.onkey(down_key, "s")
        screen.screen.onkey(right_key, "d")
        if data.level >= 3:
            screen.screen.listen()
            screen.screen.onkey(jump_up, "Up")
            screen.screen.onkey(jump_left, "Left")
            screen.screen.onkey(jump_down, "Down")
            screen.screen.onkey(jump_right, "Right")
    elif data.controls == "arrows":
        screen.screen.listen()
        screen.screen.onkey(up_key, "Up")
        screen.screen.onkey(left_key, "Left")
        screen.screen.onkey(down_key, "Down")
        screen.screen.onkey(right_key, "Right")
        if data.level >= 3:
            screen.screen.onkey(jump_up, "w")
            screen.screen.onkey(jump_left, "a")
            screen.screen.onkey(jump_down, "s")
            screen.screen.onkey(jump_right, "d")