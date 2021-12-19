class Unit:

    def __init__(self, max_hp: int, default_hp: int, default_defence: int, hp: int = 0, defence: int = 0, got_key: bool = False, coord: tuple = (0, 0)):
        self.max_hp = max_hp
        self.default_hp = default_hp

        if hp == 0:
            self.hp = self.max_hp
        else:
            self.hp = hp

        self.default_defence = default_defence

        if defence == 0:
            self.defence = self.default_defence
        else:
            self.defence = defence

        self.got_key = got_key
        self.coord = coord

    def has_key(self):
        return self.got_key

    def set_key(self):
        self.got_key = True

    def _is_alive(self):
        return self.hp > 0

    def get_damage(self, damage):
        if self.defence >= damage:
            damage = 0
        else:
            damage = damage - self.defence

        self.hp -= damage

        if not self._is_alive():
            raise UnitDied("Unit died")

    def set_coordinates(self, x, y):
        self.coord = (x, y)

    def get_coordinates(self):
        return self.coord[0], self.coord[1]


class UnitDied(Exception):
    pass


class Ghost(Unit):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = "Ghost"
