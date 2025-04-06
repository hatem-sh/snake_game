from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:
    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]
        self.up()

    def create_snake(self):
        for position in STARTING_POSITION:
            new_turtle = Turtle(shape="turtle")
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.goto(position)
            self.all_turtles.append(new_turtle)


    def reset(self):
        for turts in self.all_turtles:
            turts.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]




    def add_turtle(self):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        x = self.all_turtles[:len(self.all_turtles): -1]
        self.all_turtles.append(new_turtle)

    def move(self):

        for turt in range(len(self.all_turtles) - 1, 0, -1):
            turt_x = self.all_turtles[turt - 1].xcor()
            turt_y = self.all_turtles[turt - 1].ycor()
            self.all_turtles[turt].goto(turt_x, turt_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:

            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
