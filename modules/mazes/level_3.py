import turtles
import data
import standart_settings as stand
import mazes.endscreen as endscreen
def go(x,y):
    turtles.t_mazeer.pu()
    turtles.t_mazeer.goto(x,y)
    turtles.t_mazeer.pd()
def level_three_draw():
    go(-200,200)
    turtles.t_mazeer.color("lightgray")
    stand.rectangle(400,400,-90)
    go(-200,0)
    turtles.t_mazeer.color("white")
    # Спавн
    stand.rectangle(50, 50,-90)
    go(-150,-10)
    # Коридор спавн-комната, основной коридор
    stand.rectangle(180,30,-90)
    go(30,10)
    # Комната 1
    stand.rectangle(70,70,-90)
    go(65,-40)
    # Монетка 1
    turtles.t_mazeer.begin_fill()
    turtles.t_mazeer.color("yellow")
    turtles.t_mazeer.circle(15)
    turtles.t_mazeer.end_fill()
    turtles.t_mazeer.color("white")
    go(0,-40)
    # Основной коридор
    stand.rectangle(20,240,90)
    go(-80,30)
    # Комната 2
    stand.rectangle(70,70,90)
    go(-45,50)
    # Монетка 2
    turtles.t_mazeer.begin_fill()
    turtles.t_mazeer.color("yellow")
    turtles.t_mazeer.circle(15)
    turtles.t_mazeer.end_fill()
    turtles.t_mazeer.color("white")
    # ОБУЧЕНИЕ
    go(45,35)
    stand.rectangle(120,100,90)
    go(95,115)
    turtles.t_mazeer.color("black")
    turtles.t_mazeer.write("Бачишь перешкоди?", align="center", font=["Verdana", 7, "normal"])
    go(105,95)
    turtles.t_mazeer.write("Їх треба перестрибнути!", align="center", font=["Verdana", 7, "normal"])
    go(95,75)
    turtles.t_mazeer.write("Щоб стрибати ", align="center", font=["Verdana",8,"normal"])
    go(95,57)
    turtles.t_mazeer.write(" натискайте на:", align="center", font=["Verdana",8,"normal"])
    go(95,40)
    if data.controls == "WASD":
        text = "Стрілки"
    elif data.controls == "arrows":
        text = "w, a, s, d"
    else:
        text = "ERROR"
    turtles.t_mazeer.write(text,align="center",font=["Verdana",12,"normal"])
    turtles.t_mazeer.color("white")
    # ОБУЧЕНИЕ
    go(-10,55)
    # Проход в комнату 2
    stand.rectangle(10,20,90)
    go(2,198)
    turtles.t_mazeer.color("darkgreen")
    # Чекпоинт 1
    stand.rectangle(16,16,-90)
    go(4,196)
    turtles.t_mazeer.color("lime")
    # Чекпоинт 2
    stand.rectangle(12,12,-90)
    go(2,10)
    turtles.t_mazeer.color("gray")
    # Шипы, 1 слой
    for i in range(3):
        stand.rectangle(3,3,-90)
        go(turtles.t_mazeer.xcor() + 6, turtles.t_mazeer.ycor())
    go(2, 16)
    # Шипы, 2 слой
    for i in range(3):
        stand.rectangle(3,3,-90)
        go(turtles.t_mazeer.xcor() + 6, turtles.t_mazeer.ycor())
    go(0,150)
    turtles.t_mazeer.color("saddlebrown")
    # Дверь 2
    stand.rectangle(20,5,90)
    go(0,130)
    # Дверь 1
    stand.rectangle(20,5,90)

def level_three_hitboxes():
    x = turtles.t_player.xcor()
    y = turtles.t_player.ycor()
    # Нижняя часть
    if x < 30 and y < -50:
        stand.kill()
        print("0")
    # Комната 1, нижняя часть
    elif y < -60 and x > 30:
        stand.kill()
        print("1")
    # Правая часть комнаты 1, правая часть основного коридора
    elif x > 100:
        stand.kill()
        print("2")
    # Верхняя часть спавна, левая часть комнаты 2
    elif x < -80 and y > 0:
        stand.kill()
        print("3")
    # Нижняя часть коридора Спавн-Комната 1
    elif -150 < x < 30 and y < -40:
        stand.kill()
        print("4")
    # Нижняя часть комнаты 2
    elif x < 0 and -10 < y < 30:
        stand.kill()
        print("5")
    # Верхняя часть комнаты 2, левая часть основного коридора
    elif x < -10 and y > 100:
        stand.kill()
        print("6")
    # Верхняя часть коридора Спавн-Комната 1
    elif -150 < x < 0 and -10 < y < 20:
        stand.kill()
        print("7")
    # Перегородка комнаты 1
    elif 20 < x < 30 and -10 < y:
        stand.kill()
        print("8")
    # Перегородки комнаты 2
    elif -10 < x < 0 and 30 < y < 55:
        stand.kill()
        print("9")
    elif -10 < x < 0 and  75 < y < 100:
        stand.kill()
        print("10")
    # Верхняя часть комнаты 1
    elif x > 20 and y > 10:
        stand.kill()
        print("11")
    # Шипы
    elif 0 < x < 20 and 10 < y < 20 and data.jumping == 0:
        stand.kill()
        print("spikes kill")
    # Монетка 1
    elif 50 < x < 80 and -40 < y < -10 and data.coin[0] == 0:
        data.coin[0] = 1
        turtles.t_mazeer.color("white")
        go(65,-40)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.circle(15)
        turtles.t_mazeer.end_fill()
        go(0,130)
        stand.rectangle(20,5,90)
    # Монетка 2
    elif -60 < x < -30 and 50 < y < 80 and data.coin[1] == 0:
        data.coin[1] = 1
        turtles.t_mazeer.color("white")
        go(-45,50)
        turtles.t_mazeer.begin_fill()
        turtles.t_mazeer.circle(15)
        turtles.t_mazeer.end_fill()
        go(0,150)
        stand.rectangle(20,5,90)
    # Дверь 1
    elif 0 < x < 20 and 130 < y < 136 and data.coin[0] == 0:
        stand.kill()
    # Дверь 2
    elif 0 < x < 20 and 150 < y < 156 and data.coin[1] == 0:
        stand.kill()
    # Финиш
    elif y > 180:
        turtles.t_mazeer.clear()
        turtles.t_player.ht()
        data.level = "endscreen"
        endscreen.endscreen()
        data.endscreen = 1