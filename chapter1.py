import time
import turtle
from english_text import text


class Chapter1():

    def __init__(self, screen, font, font2, sleep_time):
        self.screen = screen
        self.font = font
        self.font2 = font2
        self.sleep_time = sleep_time
        if self.sleep_time > 0:\
            self.draw_speed = 1
        else:
            self.draw_speed = 0
        self.counter = 0
        self.slides = [self.slide1, self.slide2, self.slide3]
        self.text = text["chapter1"]
        self.text_pos = 0
        self.next = text["next"]
        return

    '''
    def chapter1(sc, font, font2, sleep_time):


        time.sleep(sleep_time)
        #show the explanation
        pen.goto(turtle.Vec2D(-sc.window_width() // 2 + 450, sc.window_height() // 2 - 220))
        pen.write(self.text[self.text_pos], font=font2)
        self.text_pos += 1
        pen.hideturtle()
        pen.speed(0)

        # Second part
        time.sleep(sleep_time)
        pen.goto(turtle.Vec2D(-sc.window_width() // 2 + 200, sc.window_height() // 2 - 380))
        pen.write(self.text[self.text_pos], font=font2)
        self.text_pos += 1
        time.sleep(sleep_time)
        # draw two points and then the line
        pen.showturtle()
        pen.speed(1)


        # write the line example
        time.sleep(sleep_time)
        pen.hideturtle()
        pen.speed(0)
        pen.goto(turtle.Vec2D(-sc.window_width() // 2 + 800, sc.window_height() // 2 - 500))
        pen.write(self.text[self.text_pos], font=font2)
        self.text_pos += 1

        time.sleep(sleep_time)
        pen.goto(turtle.Vec2D(-sc.window_width() // 2 + 200, - sc.window_height() // 2 + 100))
        pen.write(text["next"], font=font2)
        return
    '''

    def draw_plane(self, pen):
        #ox
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 150, self.screen.window_height() // 2 - 530))
        pen.pendown()
        pen.forward(600)

        # draw the X
        pos = pen.pos()
        pen.left(135)
        pen.forward(10)
        pen.back(10)
        pen.right(2*135)
        pen.forward(10)
        pen.back(10)
        pen.setheading(0)
        pen.penup()
        pen.goto(pos[0] - 10, pos[1]-40)
        pen.write("X", font=self.font2)

        #oy
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 450, self.screen.window_height() // 2 - 830))
        pen.left(90)
        pen.pendown()
        pen.forward(600)

        # draw the X
        pos = pen.pos()
        pen.left(135)
        pen.forward(10)
        pen.back(10)
        pen.right(2 * 135)
        pen.forward(10)
        pen.back(10)
        pen.setheading(0)
        pen.penup()
        pen.goto(pos[0] + 10, pos[1]-30)
        pen.write("Y", font=self.font2)

        pen.setheading(90)
        pen.back(300)
        pen.write("0", font=self.font2)

    def draw_line(self, pen, point1, point2):
        cur_pos = pen.pos()
        pen.forward(200)
        pen.dot(5, "red")
        pos_a = pen.pos()
        pen.forward(200)
        pen.dot(5, "red")
        pos_b = pen.pos()

        pen.goto(pos_a[0]-10, pos_a[1]-40)
        pen.write(point1, font=self.font2)
        pen.goto(pos_b[0]-10, pos_b[1]-40)
        pen.write(point2, font=self.font2)

        pen.goto(cur_pos)
        for i in range(3):
            pen.pendown()
            pen.forward(10)
            pen.penup()
            pen.forward(10)

        pen.pendown()
        pen.forward(450)
        pen.penup()
        pen.forward(10)
        for i in range(3):
            pen.pendown()
            pen.forward(10)
            pen.penup()
            pen.forward(10)


    def has_more_slides(self):
        return self.counter < len(self.slides)

    def play_slide(self):
        self.slides[self.counter]()
        self.counter += 1

    def slide1(self):
        self.screen.clear()

        self.screen.bgcolor("#BBBBBB")
        pen = turtle.Turtle()
        pen.penup()
        pen.hideturtle()
        pen.color("blue")
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 200, self.screen.window_height() // 2 - 80))
        pen.write(self.text[self.text_pos], font=self.font)
        self.text_pos += 1

        time.sleep(self.sleep_time)

        pen.color("black")
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 150, self.screen.window_height() // 2 - 200))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 150, self.screen.window_height() // 2 - 230))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        # draw the plane
        pen.showturtle()
        pen.color("black")
        pen.speed(self.draw_speed) # should be 1
        pen.pensize(2)
        self.draw_plane(pen)
        pen.pensize(1)
        pen.hideturtle()
        time.sleep(self.sleep_time)

        pen.color("black")
        pen.hideturtle()
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 300))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        # draw 3 points A(5,7), B(-6, 2), C(-3,-3)
        coord_oo = (-self.screen.window_width() // 2 + 450, self.screen.window_height() // 2 - 530)
        coord_a = (coord_oo[0] + 30 * 5, coord_oo[1] + 30 * 7)
        coord_b = (coord_oo[0] - 30 * 6, coord_oo[1] + 30 * 2)
        coord_c = (coord_oo[0] - 30 * 3, coord_oo[1] - 30 * 3)
        pen.showturtle()
        pen.speed(self.draw_speed) # should be 1
        pen.goto(coord_a)
        pen.dot(5, "red")
        pen.goto(coord_a[0] + 5, coord_a[1] - 30)
        pen.write("A", font=self.font2)
        pen.goto(coord_b)
        pen.dot(5, "red")
        pen.goto(coord_b[0] + 5, coord_b[1] - 30)
        pen.write("B", font=self.font2)
        pen.goto(coord_c)
        pen.dot(5, "red")
        pen.goto(coord_c[0] + 5, coord_c[1] - 30)
        pen.write("C", font=self.font2)
        pen.hideturtle()
        pen.speed(0)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 330))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 360))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 390))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        # draw the coordinates of B
        pen.color("#999999")
        pen.setheading(0)
        pen.showturtle()
        pen.speed(self.draw_speed) # should be 1
        pen.goto(coord_b)
        pen.pendown()
        pen.forward(30*6)
        pen.penup()
        pen.right(45)
        pen.forward(10)
        pen.color("black")
        pen.write("2", font=self.font2)
        pen.goto(coord_b)
        pen.color("#999999")
        pen.setheading(270)
        pen.pendown()
        pen.forward(30*2)
        pen.penup()
        pen.forward(40)
        pen.right(45)
        pen.color("black")
        pen.write("-6", font=self.font2)
        pen.hideturtle()

        # add more text
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 420))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 450))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time*3)


        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, -self.screen.window_height() // 2 + 100))
        pen.color("black")
        pen.write(self.next, font=self.font2)

    def slide2(self):
        self.screen.clear()
        self.screen.bgcolor("#BBBBBB")
        pen = turtle.Turtle()
        
        pen.penup()
        pen.hideturtle()
        pen.color("blue")
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 200, self.screen.window_height() // 2 - 80))
        pen.write(self.text[self.text_pos], font=self.font)
        self.text_pos += 1

        pen.color("black")
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 200, self.screen.window_height() // 2 - 150))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1


        # draw the plane
        pen.showturtle()
        pen.color("black")
        pen.speed(self.draw_speed) # should be 1
        pen.pensize(2)
        self.draw_plane(pen)
        pen.pensize(1)
        pen.hideturtle()
        time.sleep(self.sleep_time)

        # draw some lines and points
        coord_oo = (-self.screen.window_width() // 2 + 450, self.screen.window_height() // 2 - 530)
        #print(coord_oo)
        #pen.goto(coord_oo)
        #pen.write("AICI E MIJ")
        coord_a = (coord_oo[0] - 30 * 8, coord_oo[1] + 30 * 7)
        coord_b = (coord_oo[0] - 30 * 9, coord_oo[1] - 30 * 2)
        coord_c = (coord_oo[0] - 30 * 5, coord_oo[1] - 30 * 8)

        pen.setheading(0)
        pen.showturtle()
        pen.speed(self.draw_speed)
        pen.goto(coord_a)
        pen.right(20)
        pen.color("#ffff00")
        self.draw_line(pen, "A", "B")

        pen.goto(coord_b)
        pen.setheading(0)
        pen.right(20)
        pen.color("#ff00ff")
        self.draw_line(pen, "C", "D")

        pen.goto(coord_c)
        pen.setheading(0)
        pen.right(-70)
        pen.color("#007700")
        self.draw_line(pen, "E", "F")

        pen.speed(0)
        pen.hideturtle()
        pen.up()

        # lines explanation
        pen.color("black")
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 250))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 310))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 370))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 430))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, self.screen.window_height() // 2 - 490))
        pen.write(self.text[self.text_pos], font=self.font2)
        self.text_pos += 1
        time.sleep(self.sleep_time)


        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, -self.screen.window_height() // 2 + 100))
        pen.color("black")
        pen.write(self.next, font=self.font2)

    def slide3(self):
        self.screen.clear()
        self.screen.bgcolor("#BBBBBB")
        pen = turtle.Turtle()
        pic = turtle.Turtle()
        pic.penup()
        pic.hideturtle()

        pen.penup()
        pen.hideturtle()
        pen.color("blue")
        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 200, self.screen.window_height() // 2 - 80))
        pen.write(self.text[self.text_pos], font=self.font)
        self.text_pos += 1

        pic.setpos(turtle.Vec2D(self.screen.window_width() // 2 - 200, self.screen.window_height() // 2 - 150))
        pic.shape('euclid.gif')
        pic.showturtle()

        pen.goto(turtle.Vec2D(-self.screen.window_width() // 2 + 700, -self.screen.window_height() // 2 + 100))
        pen.color("black")
        pen.write(self.next, font=self.font2)




