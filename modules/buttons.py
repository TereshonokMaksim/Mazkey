import modules.mazes.level_1 as lvl1
import modules.screen as screen
import modules.turtles as turtles
import modules.data as data
import modules.chooses as chooses
import modules.player_movement as player_movement
import webbrowser as webbrowser
import modules.mazes.endscreen as endscr
contin = False
def click_color_choose(x,y):
    global contin
    if  data.color_choose_finished == 0:
        if 0 < y < 80:
            if -140 < x < -60:
                turtles.t_player.color("red")
                contin = True
            elif -40 < x < 40:
                turtles.t_player.color("yellow")
                contin = True
            elif 60 < x < 140:
                turtles.t_player.color("orange")
                contin = True
        elif -100 < y < -20:
            if -140 < x < -60:
                turtles.t_player.color("green")
                contin = True
            elif -40 < x < 40:
                turtles.t_player.color("blue")
                contin = True
            elif 60 < x < 140:
                turtles.t_player.color("cyan")
                contin = True
        elif -200 < y < -120:
            if -140 < x < -60:
                turtles.t_player.color("purple")
                contin = True
            elif -40 < x < 40:
                turtles.t_player.color("pink")
                contin = True
            elif 60 < x < 140:
                turtles.t_player.color("saddlebrown")
                contin = True
        if contin == True:
            turtles.t_player.forward(100)
            print("OK")
            data.color_choose_finished = 1
            turtles.t_painter.clear()
            chooses.controls_choose()
            screen.screen.onclick(click_color_choose)
        else:
            print("BAD")
    elif data.controllers_choose_finished == 0:
        if -70 < y < 0:
            if -150 < x < -40:
                data.controls = "WASD"
                print("WASD + TRUE")
                
                trigger = True
                player_movement.controls()
            elif 40 < x < 150:
                data.controls = "arrows"
                print("ARROWS + TRUE")
                turtles.t_painter.clear()
                trigger = True
                player_movement.controls()
        if trigger == True and data.level == 0:
            turtles.t_painter.clear()
            data.controllers_choose_finished = 1
            data.level = 1
            chooses.build_standart_border()
            lvl1.level_one_draw()
            player_movement.controls()
    elif data.endscreen == 1:
        if 170 < x < 250 and 200 < y < 250:
            webbrowser.open("https://github.com/TereshonokMaksim?tab=repositories")
        elif -100 < x < -20 and -40 < y < 40:
            turtles.turtle.Terminator()
        # elif 20 < x < 100 and -40 < y < 40:
        #     data.achivments_scr == 1
        #     data.endscreen = 0
        #     data.test = 1
        #     turtles.t_mazeer.clear()
        #     endscr.draw_achivments()
        #     player_movement.time.sleep(1)
    # elif data.achivments_scr == 1:
    #     if -250 < x < -170 and 200 < y < 250:
    #         data.endscreen = 1
    #         data.achivments_scr = 0
    #         turtles.t_mazeer.clear()
    #         endscr.endscreen()
    #         print("1") 
    #         data.test = 2
        else:
            print("0")
    else:
        print("Absolute 0")
        print(data.achivments_scr, "achivment")
        print(data.endscreen, "endscr")
        print(data.test)