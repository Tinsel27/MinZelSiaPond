init python:
    class actor:
        def __init__(self, id, name, hp, max_hp, atk, is_player=True):
            self.id=id
            self.name=name
            self.hp=hp
            self.max_hp=max_hp
            self.atk=atk
            self.is_player=is_player
            self.isdie=False
        def take_damage(self, damage):
            self.hp -= damage
            if self.hp <= 0:
                self.hp = 0
                self.is_dead = True
                return f"{self.name} die"
            return f"{self.name} take {damage} damage"