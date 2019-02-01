from turtle import *
from random import randint

width, height = 720, 480

screen = Screen()
screen.setup(width, height)
screen.title("python海龟画图的彩色粒子效果")
screen.bgcolor("black")
screen.colormode(255)
screen.delay(0)


class Particle(Turtle):

    def __init__(self):

        Turtle.__init__(self, visible=False, shape="circle")
        self.penup()
        self.speed(0)
        c = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.color(c, c)
        self.shapesize(0.1, 0.1)        # 形状为1/10
        self.accspeed = -0.1            # 加速度
        self.initmove()                 # 初始化移动

    def initmove(self):
        self.goto(0, 0)
        self.xspeed = randint(-2, 2)
        self.yspeed = randint(3, 5)
        self.showturtle()
        self.move()

    def move(self):
        x = self.xcor() + self.xspeed    # 水平方向移动
        y = self.ycor() + self.yspeed    # 垂直方向受重力移动
        if y > -height/2:                # 没到屏幕最下面,那么就移动到新位置
            self.yspeed = self.yspeed + self.accspeed
            self.goto(x, y)
            screen.ontimer(self.move, 10)
        else:
            self.hideturtle()           # 隐藏粒子
            self.initmove()             # 继续移到(0,0)坐标,重生.


if __name__ == "__main__":

    p = []
    for i in range(60):
        p.append(Particle())

    screen.mainloop()
