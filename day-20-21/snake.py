from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Models a snake, makes it appearn on screena and handles all its movements"""

    def __init__(self):
        self.snake_blocks = []
        self.create_snake()
        # Mush be after creating the snake to not crash as non existant
        self.head = self.snake_blocks[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_block(position)

    def add_block(self, position):
        block = Turtle("square")
        block.penup()
        block.color("white")
        block.goto(position)
        self.snake_blocks.append(block)

    def extend(self):
        self.add_block(self.snake_blocks[-1].position())

    def move(self):
        # We cannot add keyword arguments here, since range comes from C and it doesn't accept it
        for block_num in range(len(self.snake_blocks) - 1, 0, -1):
            # The new coordinates for the block will be the coordinates of the block in front of it.
            # This is how we handle turning. (direction of subsequent blocks remains the same
            new_x = self.snake_blocks[block_num - 1].xcor()
            new_y = self.snake_blocks[block_num - 1].ycor()
            self.snake_blocks[block_num].goto(new_x, new_y)
        # We need the first block to move, so that all the blocks don't just lay on top of each other
        self.snake_blocks[0].forward(20)

    def move_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)

    def collision(self):
        pass
