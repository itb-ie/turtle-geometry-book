import turtle
from english_text import text
from PIL import Image
import time
import chapter1

sleep_time = 3

font = ("Arial", 20, "normal")
font2 = ("Arial", 15, "normal")


def intro():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    pen.color("blue")
    pen.goto(turtle.Vec2D(-sc.window_width()//2 + 200, sc.window_height()//2-100))
    pen.write(text["welcome"], font=font)

    time.sleep(sleep_time)
    picture = turtle.Turtle()
    picture.shape("icon.gif")

    time.sleep(sleep_time)
    pen.goto(turtle.Vec2D(-sc.window_width()//2 + 200, -sc.window_height()//2+100))
    pen.color("black")
    pen.write(text["next"], font=font)

    sc.onkeypress(next_slide, "space")
    sc.listen()


stage = 0
script = {0:intro, 1: chapter1.Chapter1 }


chapter = 0

def next_slide():
    global stage
    global script
    global chapter

    print("sunt in next slide")
    if not chapter or not chapter.has_more_slides():
        stage += 1
        if stage not in script:
            print("We are done!")
            exit()
        chapter = script[stage](sc, font, font2, sleep_time)

    chapter.play_slide()
    #call the proper function
    sc.onkeypress(next_slide, "space")
    sc.listen()


sc = turtle.Screen()
sc.setup(0.8, 0.8)
sc.bgcolor("#BBBBBB")

im = Image.open('Bogdan-poza-tr.png')
im.save('icon.gif')
sc.addshape('icon.gif')

im = Image.open('220px-Euklid-von-Alexandria_1.jpg')
im.save('euclid.gif')
sc.addshape('euclid.gif')

#call the first slide
script[0]()


turtle.done()
