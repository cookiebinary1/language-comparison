import random
import math
import numpy as np

width = 30
height = 30
diagonal = math.sqrt(width * height)
BG = 255, 255, 255
FOOD_C = 128, 0, 0
BODY_C = 0, 0, 0
sqr_size = 10
SPEED = 1


def find_inputs(snake, food):
    inputs = []
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for direction in directions:
        xpos = snake.body[0][0]
        ypos = snake.body[0][1]
        wall_d = diagonal
        cell_d = diagonal
        food_d = diagonal

        for i in range(1, 30):
            xpos += direction[0]
            ypos += direction[1]

            # check wall
            if xpos > width or xpos < 0 or ypos > height or ypos < 0:
                wall_d = i
                break

            # check tail
            for cell in snake.body:
                if cell[0] == xpos and cell[1] == ypos:
                    cell_d = i
                    break

            # check food
            if food.pos[0] == xpos and food.pos[1] == ypos:
                food_d = i
                break

        inputs.append(float(wall_d))
        inputs.append(float(cell_d))
        inputs.append(float(food_d))

    return inputs


def sigmoid(x):
    # applying the sigmoid function
    return 1 / (1 + np.exp(-x))


def compute_outputs(inputs, synaptic_weights):
    print(type(inputs[0]))
    return sigmoid(np.dot(inputs, synaptic_weights))


def dist(a, b):
    return math.sqrt((b.pos[0] - a.pos[0]) ** 2 + (b.pos[1] - a.pos[1]) ** 2)


def check_food(snake, food):  # Check if food is eaten
    if dist(snake, food) > 0:
        return False
    else:
        return True


def loser(snake, food):  # Check if lost the game
    if snake.pos[0] <= 0 or snake.pos[0] >= width:
        return True
    if snake.pos[1] <= 0 or snake.pos[1] >= height:
        return True
    for i in snake.body[1:]:
        if i == snake.pos:
            return True


# def game_speed(snake):
#     if (10 + snake.score() // 2) < 30:
#         return 1000 + snake.score() // 2
#     else:
#         return 3000


class Snake(object):
    def __init__(self):
        self.pos = [random.randint(1, 10),
                    random.randint(1, 10)]
        self.mov = "UP"
        self.body = [self.pos[:]]

    def change_mov(self, key):  # Decide where to move
        if key == "UP" and self.mov != "DOWN":
            self.mov = key
        if key == "DOWN" and self.mov != "UP":
            self.mov = key
        if key == "RIGHT" and self.mov != "LEFT":
            self.mov = key
        if key == "LEFT" and self.mov != "RIGHT":
            self.mov = key

    def score(self):
        return len(self.body)

    def move(self, eat):  # Snake movement
        if self.mov == "UP": self.pos[1] = self.pos[1] - SPEED
        if self.mov == "DOWN": self.pos[1] = self.pos[1] + SPEED
        if self.mov == "LEFT": self.pos[0] = self.pos[0] - SPEED
        if self.mov == "RIGHT": self.pos[0] = self.pos[0] + SPEED
        self.body.insert(0, self.pos[:])
        if not eat:
            self.body.pop()


class Food(object):
    def __init__(self):
        self.pos = [random.randint(1, 10),
                    random.randint(1, 10)]
