import modules.turtles as turtles
import modules.data as data
import modules.standart_settings as stand
import modules.mazes.level_2 as lvl2
def go(x,y):
    turtles.t_mazeer.pu()
    turtles.t_mazeer.goto(x,y)
    turtles.t_mazeer.pd()
    
def writ(text, font_size):
    turtles.t_mazeer.write(text, align="center", font=["Verdana",font_size,"normal"])

def level_one_draw():
    turtles.t_mazeer.color("lightgray")
    go(-200, -50)
    turtles.t_player.goto(-175,-25)
    go(-200, -50)
    stand.rectangle(400,150,-90)
    go(-20, -50)
    stand.rectangle(15,100,90)
    go(-200, 200)
    stand.rectangle(120,200,-90)
    go(45,200)
    stand.rectangle(155,200,-90)
    go(-80,200)
    stand.rectangle(130,100,-90)
    go(165, -10)
    turtles.t_mazeer.color("lime")
    stand.rectangle(20,40,-90)
    turtles.t_mazeer.color("darkgreen")
    go(168,-13)
    stand.rectangle(14,34,-90)

    # Update: V1.02

    go(-55,-60)
    turtles.t_mazeer.color("white")
    stand.rectangle(240,100,-90)
    turtles.t_mazeer.color("black")
    go(70,-80)
    writ("Бачишь у кінці зелений прямокутник?", 10)
    go(70,-100)
    writ("Звісно бачишь! Це - фініш!", 11)
    go(70,-120)
    writ("Твоя ціль - дістатися його!", 11)
    go(70,-140)
    writ("Удачі!", 15)



def lvl_one_hitboxes(x,y):
    if y < -50:
        stand.kill()
    if -20 < x < -5 and -50 < y < 50:
        stand.kill()
    if -200 < x < -80 and 0 < y < 200:
        stand.kill()
    if 45 < x < 200 and 0 < y < 200:
        stand.kill()
    if -70 < x < 40 and 95 < y < 195 and data.achivments[0] == 0:
        data.achivments[0] = 1
        go(-175, -175)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.color("black")
        for i in range(2):
            turtles.t_mazeer.forward(120)
            turtles.t_mazeer.left(90)
            turtles.t_mazeer.forward(50)
            turtles.t_mazeer.left(90)
        turtles.t_mazeer.color("gold")  
        turtles.t_mazeer.end_fill()
        go(-170,-170)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.color("black")
        for i in range(4):
            turtles.t_mazeer.forward(40)
            turtles.t_mazeer.left(90)
        turtles.t_mazeer.color("white")
        turtles.t_mazeer.end_fill()
        go(-150, -165)
        turtles.t_mazeer.seth(0)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.circle(15)
        turtles.t_mazeer.color("yellow")
        turtles.t_mazeer.end_fill()
        go(-150, -164)
        turtles.t_mazeer.color("darkgoldenrod")
        turtles.t_mazeer.write("C", align="center", font=("Verdana", 20, "normal"))
        go(-90, -165)
        turtles.t_mazeer.color("red")
        turtles.t_mazeer.write("oh no", align="center", font=("Verdana", 17, "normal"))
        go(-120, -115)
        turtles.t_mazeer.color("black")
        turtles.t_mazeer.write("Досягнення отримано!", align="center", font=("Arial", 12, "normal"))
    if 165 < x < 185 and -50 < y < 0:
        stand.level_complete()
        lvl2.level_two_draw()
        