from game_items import Wall, Grass, Door, Key, Trap
from units import Unit, Ghost
from mapping import mapping


class Cell:

    def __init__(self, obj):
        self.obj = obj

    def get_obj(self):
        return self.obj

    def get_name(self):
        return self.obj.name

    def remove_unit(self):
        self.obj = Grass()

    def set_door(self):
        self.obj = Door()

    def set_grass(self):
        self.obj = Grass()

    def set_wall(self):
        self.obj = Wall()

    def set_key(self):
        self.obj = Key()

    def set_trap(self):
        self.obj = Trap()

    def set_unit(self):
        self.obj = Unit()


class Level:

    def __init__(self, level_filename):
        self.area = []
        self.level_filename = level_filename

    def fill_area(self):
        with open(self.level_filename, "r") as file:
            for line in file:
                new_str = []
                for sign in line:
                    if sign == "W":
                        obj = Wall()
                    elif sign == "g":
                        obj = Grass()
                    elif sign == "G":
                        obj == Ghost()
                    elif sign == "D":
                        obj = Door()
                    elif sign == "K":
                        obj = Key()
                    elif sign == "T":
                        obj = Trap()
                    else:
                        continue
                    new_str.append(obj)
                self.area.append(new_str)

    def get_area(self):
        return self.area

    def print(self):
        for line in self.area:
            for i in range(len(line)):
                print(line[i], end="")
            print()


class Field:

    def __init__(self, level, unit):
        self.level = level
        self.field = self.level.area
        self.unit = unit

    def movement(self, command):
        if command.lower() == "up":
            self.move_unit_up()
        elif command.lower() == "down":
            self.move_unit_down()
        elif command.lower() == "right":
            self.move_unit_right()
        elif command.lower() == "left":
            self.move_unit_left()
        else:
            print("Please, type: up, down, right or left")

    def move_unit_up(self):
        if self.unit.coord[0] > 0:
            self.unit.coord = (self.unit.coord[0] - 1, self.unit.coord[1])

    def move_unit_down(self):
        if self.unit.coord[0] < len(self.field - 1):
            self.unit.coord = (self.unit.coord[0] + 1, self.unit.coord[1])

    def move_unit_right(self):
        if self.unit.coord[1] < len(self.field[0] - 1):
            self.unit.coord = (self.unit.coord[0], self.unit.coord[1] + 1)

    def move_unit_left(self):
        if self.unit.coord[0] > 0:
            self.unit.coord = (self.unit.coord[0], self.unit.coord[1] + 1)

    def print(self):
        for line in self.field:
            for cell in line:
                print(cell, end=" ")

    def get_field(self):
        return self.field


class Gui:

    def __init__(self, mapping: dict):
        self.mapping = mapping

    def make_field(self, field):
        for line in field:
            for i in range(len(line)):
                line[i] = self.mapping[line[i]]
