init python:
    class Actor:
        def __init__(self, name,hp, atk):
            self.name = name
            self.max_hp = hp
            self.hp = hp
            self.atk = atk
            self.is_dead = False
            self.is_defend = False

        def take_damage(self, dmg):
            if self.is_defend:
                dmg = int(dmg * 0.5)
                self.is_defend = False
            self.hp = max(0, self.hp - dmg)
            if self.hp <= 0:
                self.is_dead = True
                return f"{self.name} ถูกโจมตีและพ่ายแพ้!"
            return f"{self.name} ถูกโจมตีเสียหาย {dmg} หน่วย!"

        def heal(self):
            heal_amount = int(self.max_hp * 0.3)
            self.hp = min(self.max_hp, self.hp + heal_amount)
            return f"{self.name} ฟื้นฟู {heal_amount} HP!"

