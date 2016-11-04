import random


class RandomBot:
    actions = ['fire_left', 'fire_right', 'fire_up', 'fire_down']

    def make_choice(self, x, y, field):
        return random.choice(self.actions)


class MoveBot:
    def make_choice(self, x, y, field):
        possible_actions = self.get_possible_actions(x, y, field)
        return random.choice(possible_actions)

    def get_possible_actions(self, x, y, field):

        res = []
        lenx = len(field[0])
        leny = len(field)
        return res


def make_choice(x, y, field):
    return RandomBot().make_choice(x, y, field)


if __name__ == "__main__":
    field = [
        ['0', '9', '9', '9'],
        ['0', '9', '9', '9'],
        ['0', '9', '9', '9'],
        ['0', '0', '0', '0']
    ]
    print(make_choice(3, 1, field))