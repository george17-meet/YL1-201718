from turtle import *
class Ball(Turtle):
    def __init__(self, x, y, dx, dy, r, color):
        Turtle.__init__(self)
        self.pu()
        self.goto(x, y)
        self.dx = dx
        self.dy=dy
        self.r=r
        self.shape("circle")
        self.shapesize(r/10)
        self.color(color)

    def move(self, screen_width, screen_height):
        current_x = self.xcor()
        current_y = self.ycor()
        new_x = current_x+self.dx
        new_y = current_y+self.dy
        right_side_ball = new_x + self.r
        left_side_ball = new_x - self.r
        top_side_ball = new_y+self.dy
        bottom_side_ball = new_y - self.dy
        self.goto(new_x, new_y)
        if(right_side_ball>=screen_width or left_side_ball<=-screen_width):
            self.dx = -self.dx
        if(top_side_ball>=screen_height or bottom_side_ball<=-screen_height):
            self.dy=-self.dy
            
myBall = Ball(0, 0, 1, 4, 15, "blue")
