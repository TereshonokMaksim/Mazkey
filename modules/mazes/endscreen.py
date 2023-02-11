import turtles
import data
import standart_settings as stand
def go(x,y):
    turtles.t_mazeer.pu()
    turtles.t_mazeer.goto(x,y)
    turtles.t_mazeer.pd()
def rect_no_fill(width,height,angle):
    for i in range(2):
        turtles.t_painter.forward(width)
        turtles.t_mazeer.left(angle)
        turtles.t_mazeer.forward(height)
        turtles.t_mazeer.left(angle)
def endscreen():
    go(0, 50)
    turtles.t_mazeer.color("black")
    turtles.t_mazeer.write("THE END", align="center", font=["Verdana", 35, "normal"])
    go(-140,-40)
    turtles.t_mazeer.color("goldenrod")
    stand.rectangle(120,70,90)
    turtles.t_mazeer.width(5)
    turtles.t_mazeer.color("black")
    rect_no_fill(120,70,90)
    go(-80,-30)
    turtles.t_mazeer.write("Вийти", align="center", font=["Verdana",20,"normal"])
    go(20,-40)
    turtles.t_mazeer.color("goldenrod")
    stand.rectangle(120,70,90)
    turtles.t_mazeer.color("black")
    rect_no_fill(120,70,90)
    go(80,-30)
    turtles.t_mazeer.write("Досягнення", align="center", font=["Verdana",16,"normal"])
    go(170,200)
    turtles.t_mazeer.color("goldenrod")
    stand.rectangle(80,50,90)
    turtles.t_mazeer.color("black")
    rect_no_fill(80,50,90)
    go(210,205)
    turtles.t_mazeer.write("GitHub", align="center", font=["Verdana",16,"normal"])

def draw_achivments():
        data.achivments[0] = 1
        go(-60, 25)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.color("black")
        for i in range(2):
            turtles.t_mazeer.forward(120)
            turtles.t_mazeer.left(90)
            turtles.t_mazeer.forward(50)
            turtles.t_mazeer.left(90)
        turtles.t_mazeer.color("gold")  
        turtles.t_mazeer.end_fill()
        go(-55,30)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.color("black")
        for i in range(4):
            turtles.t_mazeer.forward(40)
            turtles.t_mazeer.left(90)
        turtles.t_mazeer.color("white")
        turtles.t_mazeer.end_fill()
        go(-35, 35)
        turtles.t_mazeer.seth(0)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.circle(15)
        turtles.t_mazeer.color("yellow")
        turtles.t_mazeer.end_fill()
        go(-35, 36)
        turtles.t_mazeer.color("darkgoldenrod")
        turtles.t_mazeer.write("C", align="center", font=("Verdana", 20, "normal"))
        go(20, 35)
        if data.achivments[0] == 1:
            turtles.t_mazeer.color("red")
            turtles.t_mazeer.write("oh no", align="center", font=("Verdana", 17, "normal"))
        elif data.achivments[0] == 0:
            turtles.t_mazeer.color("black") 
            turtles.t_mazeer.write("Йдіть вверх на 1 уровні", align="center", font=["Verdana",12,"normal"])
        turtles.t_mazeer.color("goldenrod")
        go(-250,250)
        stand.rectangle(80,50,-90)
        turtles.t_mazeer.color("black")
        go(-210,215)
        turtles.t_mazeer.write("Меню", align="center", font=["Verdana", 15, "normal"])
