import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
    def draw(self, balls_to_draw):
        balls_drawn = []
        if balls_to_draw >= len(self.contents):
            return self.contents
        for i in range(balls_to_draw):
            balls_removed = random.choice(self.contents)
            balls_drawn.append(balls_removed)
            self.contents.pop(self.contents.index(balls_removed))
        return balls_drawn
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    probability = 0
    for i in range(num_experiments):
        copied = copy.deepcopy(hat)
        exact_group = copied.draw(num_balls_drawn)
        number_of_balls = {ball: exact_group.count(ball) for ball in set(exact_group)}
        result = True
        for key, value in expected_balls.items():
            if key not in number_of_balls or number_of_balls[key] < expected_balls[key]:
                result = False
                break
        if result:
            probability += 1
    return probability / num_experiments