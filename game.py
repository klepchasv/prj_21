from game_field import Field, Level, Gui
from units import Unit


class GameController:

    def __init__(self, level, field):
        self.level = level
        self.field = field

    def get_command(self, command):
        self.field.movement(command)
        self.field.print()


curr_level = Level("levels/level_1.txt")
curr_level.fill_area()

hero = Unit(max_hp=100, default_hp=100, default_defence=20)

field = Field(curr_level, hero)
