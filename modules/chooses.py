import modules.turtles as turtles
def go(turt, x, y):
    turt.pu()
    turt.goto(x,y)
    turt.pd()
def color_choose():
    turtles.t_painter.color("black")
    go(turtles.t_painter, -100, 100)
    turtles.t_painter.write("Виберіть колір: ", font=("Verdana",20, "normal"))
    go(turtles.t_painter, -140, 0)
    clrs = ["red", "yellow", "orange", "green", "blue", "cyan", "purple", "pink", "saddlebrown"]
    clr = 0
    for i in range(3):
        for sub_clr in range(1,4):
            
            turtles.t_painter.begin_fill()
            turtles.t_painter.color("black")
            for i in range(4):
                turtles.t_painter.forward(80)
                turtles.t_painter.left(90)
            turtles.t_painter.color(clrs[clr])    
            turtles.t_painter.end_fill()
            clr += 1
            
            go(turtles.t_painter, turtles.t_painter.xcor() + 100, turtles.t_painter.ycor())
        go(turtles.t_painter, -140, turtles.t_painter.ycor() - 100)

def controls_choose():
    go(turtles.t_painter, -100, 100)
    turtles.t_painter.write("Виберіть контролери: ", font=("Verdana", 20, "normal"))
    go(turtles.t_painter, -150, 0)
    for i in range(2):
        turtles.t_painter.begin_fill()
        turtles.t_painter.color("black")
        for i in range(2):
            turtles.t_painter.forward(110)
            turtles.t_painter.right(90)
            turtles.t_painter.forward(70)
            turtles.t_painter.right(90)
        turtles.t_painter.color("goldenrod")
        turtles.t_painter.end_fill()
        go(turtles.t_painter, 40, 0)
    go(turtles.t_painter, -95, -40)
    turtles.t_painter.color("black")
    turtles.t_painter.write("WASD", align="center",font=("Verdana",20,"normal"))
    go(turtles.t_painter, 95, -40)
    turtles.t_painter.write("стрілки", align = "center",font=("Verdana",20,"normal"))

def build_standart_border():
    print("start border")
    turtles.t_painter.color("darkgrey")
    go(turtles.t_painter, -500, -500)
    turtles.t_painter.begin_fill()
    for i in range(4):
        turtles.t_painter.forward(1000)
        turtles.t_painter.left(90)
    turtles.t_painter.end_fill()
    go(turtles.t_painter,-200,-200)
    turtles.t_painter.color("white")
    turtles.t_painter.begin_fill()
    for i in range(4):
        turtles.t_painter.forward(400)
        turtles.t_painter.left(90)
    turtles.t_painter.end_fill()
    print("end border")