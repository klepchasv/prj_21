class GameItem:

    def __init__(self, name):
        self.name = name

    def step_on(self, unit):
        return unit


class Door(GameItem):

    def __init__(self):
        name = "Door"
        super().__init__(name)
        self.is_locked = True

    def step_on(self, unit):
        if self._try_open(unit):
            raise LevelPassed("Done!")

    def _try_unlock(self, unit):
        if unit.has_key():
            self.is_locked = False

    def _try_open(self, unit):
        self._try_unlock(unit)
        if not self.is_locked:
            return True
        return False


class Key(GameItem):

    def __init__(self):
        name = "Key"
        super().__init__(name)

    def step_on(self, unit):
        unit.set_key()


class Trap(GameItem):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.damage = damage

    def step_on(self, unit):
        unit.get_damage(self.damage)


class FieldItem(GameItem):
    pass


class Grass(FieldItem):

    def __init__(self):
        name = "Grass"
        super().__init__(name)


class Wall(FieldItem):

    def __init__(self):
        name = "Wall"
        super().__init__(name)


class LevelPassed(Exception):
    pass
