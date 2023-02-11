import turtles
import data
import standart_settings as stand
import player_movement
import mazes.level_3 as lvl3
def go(x,y):
    turtles.t_mazeer.pu()
    turtles.t_mazeer.goto(x,y)
    turtles.t_mazeer.pd()

def level_two_draw():
    go(-200,-50)
    turtles.t_mazeer.color("lightgray")
    # turtles.t_mazeer.speed(2)
    stand.rectangle(400,150,-90)
    go(-200, 0)
    stand.rectangle(75,10,90)
    go(-135,0)
    stand.rectangle(10,25,90)
    go(-135,40)
    stand.rectangle(10,25,90)
    go(-200,60)
    stand.rectangle(75,140,90)
    go(-178,20)
    # turtles.t_mazeer.speed(0)
    turtles.t_mazeer.color("yellow")
    turtles.t_mazeer.begin_fill()
    turtles.t_mazeer.circle(16)
    turtles.t_mazeer.end_fill()
    go(-125,200)
    turtles.t_mazeer.color("lightgray")
    stand.rectangle(250,40,-90)
    go(-100,-50)
    stand.rectangle(20,180,90)
    go(-100,130)
    stand.rectangle(100,20,-90)
    go(-20,130)
    stand.rectangle(20,150,-90)
    go(-20, -30)
    stand.rectangle(20,20,-90)
    go(-20,-30)
    turtles.t_mazeer.color("saddlebrown")
    stand.rectangle(20,30,90)
    go(30,200)
    turtles.t_mazeer.color("lightgray")
    stand.rectangle(170,400,-90)
    go(-75,105)
    turtles.t_mazeer.color("darkgreen")
    stand.rectangle(50,50,-90)
    go(-70,100)
    turtles.t_mazeer.color("lime")
    stand.rectangle(40,40,-90)

def level_two_hitboxes():
    x = turtles.t_player.xcor()
    y = turtles.t_player.ycor()
    if -200 < x < 200 and -200 < y < -50:
        stand.kill()
    elif 30 < x < 200 and -200 < y < 200:
        stand.kill()
    elif -200 < x < -125 and 0 < y < 10:
        stand.kill()
    elif -136 < x < -125 and 0 < y < 25:
        stand.kill()
    elif -136 < x < -125 and 40 < y < 65:
        stand.kill()
    elif -200 < x < -125 and 60 < y < 200:
        stand.kill()
    elif -194 < x < -162 and 20 < y < 52 and data.coin[0] == 0:
        data.coin[0] = 1
        go(-20,-30)
        turtles.t_mazeer.color("white")
        stand.rectangle(20,30,90)
        go(-178,20)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.circle(16)
        turtles.t_mazeer.end_fill() 
        go(-17,-30)
        turtles.t_mazeer.color("lightgray")
        stand.rectangle(3,15,90)
    elif -20 < x < 0 and -30 < y < 0 and data.coin[0] == 0:
        stand.kill()
    elif -17 < x < -14 and -30 < y < -15 and data.coin[0] == 1:
        stand.kill()
    # elif 
    elif -75 < x < -25 and 55 < y < 105:
        stand.level_complete()
        player_movement.controls()
        lvl3.level_three_draw()
    elif -20 < x < 0 and 0 < y < 130:
        stand.kill()
    elif -100 < x < 0 and 110 < y < 130:
        stand.kill()
    elif -100 < x < -80 and -50 < y < 130:
        stand.kill()
    elif -20 < x < 0 and -200 < y < -30:
        stand.kill()
    elif -200 < x < 200 and 160 < y < 200:
        stand.kill()