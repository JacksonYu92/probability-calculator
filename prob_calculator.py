import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **args):
        self.args = args
        self.contents = []
        for key, value in args.items():
            # number of color(key) based on the value amount
            for i in range(value):
                self.contents.append(key)

    def draw(self, amount):
        draw_list = []
        if amount >= len(self.contents):
            return self.contents
        for i in range(amount):
            color = self.contents.pop(random.randint(0, len(self.contents)-1))
            draw_list.append(color)
        return draw_list




def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        draw_list_exp = hat_copy.draw(num_balls_drawn)
        match = True
        for key,value in expected_balls.items():
            if draw_list_exp.count(key) < value:
                match = False
                break
        if match:
            count +=1
    return count/num_experiments