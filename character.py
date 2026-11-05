import random


class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power  # initial power, never changed

    def attack(self, other):
        # Damage is random: 30% to 90% of the initial attack power
        damage = round(random.uniform(0.3, 0.9) * self.attack_power, 1)
        other.hp = round(other.hp - damage, 1)
        print(f"{self.name} attacks {other.name} for {damage} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {max(self.hp, 0)} HP"
