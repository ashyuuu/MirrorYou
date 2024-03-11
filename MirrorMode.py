import turtle

class MirrorMode:
    def __init__(self):
        self.isMirrorMode = False

        # Set up the screen
        self.screen = turtle.Screen()
        self.screen.setup(width=1.0, height=1.0)
        self.screen.bgcolor("black")

        # Create a turtle
        self.rectangle = turtle.Turtle()
        self.rectangle.color("black")
        self.rectangle.penup()

        # Move turtle to starting position
        self.rectangle.goto(-self.screen.window_width() / 2, self.screen.window_height() / 2)
        self.rectangle.pendown()

    def turnMirrorOn(self):
        self.isMirrorMode = True
        
        # Draw the rectangle
        self.rectangle.begin_fill()
        for _ in range(2):
            self.rectangle.forward(self.screen.window_width())
            self.rectangle.right(90)
            self.rectangle.forward(self.screen.window_height())
            self.rectangle.right(90)
        self.rectangle.end_fill()

        # Hide the turtle
        self.rectangle.hideturtle()

    def turnMirrorOff(self):
        self.isMirrorMode = False

        # Clear the rectangle
        self.rectangle.clear()

    def isMirrorModeOn(self) -> bool:
        return self.isMirrorMode