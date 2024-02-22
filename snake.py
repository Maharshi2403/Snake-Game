from turtle import Turtle
class Snake:
    start_position = []
    segments = []

    
    def __init__(self):
        self.start_position = [(0,0),(-20,0),(-40,0)]
        self.segments = []

        

    def create_Portion(self,position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def add_portion(self):
         for positions in self.start_position:
              self.create_Portion(positions)

    def extend_Snake(self):
         self.create_Portion(self.segments[-1].position())
        
    def move(self):

            for segment_num in range(len(self.segments)-1,0,-1):
                 num_x = self.segments[segment_num-1].xcor()
                 num_y = self.segments[segment_num-1].ycor()
                 self.segments[segment_num].goto(num_x,num_y)
            self.segments[0].forward(20)
            
    def Up(self):
        
        if self.segments[0].heading() != 270:
           self.segments[0].setheading(90)

        else:
             pass
           

    def Down(self):
           
        if self.segments[0].heading() != 90:
           self.segments[0].setheading(270)
           
        else:
             pass
    
    def Left(self):
        
        if self.segments[0].heading() != 0:
           self.segments[0].setheading(180)
        else:
             pass

    def Right(self):
           
        if self.segments[0].heading() != 180:
           self.segments[0].setheading(0)
        else:
             pass
           
