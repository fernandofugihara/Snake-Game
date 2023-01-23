from turtle import Turtle

INICIAL_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def create_snake(self):
        for position in INICIAL_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        
        self.snake_head.forward(20)
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)

    def increase_tail(self):
        self.add_segment(self.segments[-1].position())
    
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.snake_head = self.segments[0]

    def go_up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    
    def go_down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    
    def turn_left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def turn_right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)        
