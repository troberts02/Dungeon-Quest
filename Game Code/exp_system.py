import json
import os
import random

# File path for storing player stats and EXP
EXP_FILE = "player_exp.json"

class PlayerStats:
    def __init__(self, health=100, melee_damage=20, fireball_damage=20, level=1, experience=0):
        self.health = health
        self.melee_damage = melee_damage
        self.fireball_damage = fireball_damage
        self.level = level
        self.experience = experience

    def level_up(self):
        self.level += 1
        self.health += 5
        self.melee_damage += 5
        self.fireball_damage += 5
        print(f"Level up! You are now level {self.level}. Health: {self.health}, Melee Damage: {self.melee_damage}, Fireball Damage: {self.fireball_damage}")

    def add_experience(self, exp_gain):
        self.experience += exp_gain
        print(f"Gained {exp_gain} EXP. Total EXP: {self.experience}")

        # Level up every 30 EXP
        while self.experience >= self.level * 30:
            self.experience -= self.level * 30
            self.level_up()

    def save_to_file(self):
        data = {
            "health": self.health,
            "melee_damage": self.melee_damage,
            "fireball_damage": self.fireball_damage,
            "level": self.level,
            "experience": self.experience
        }
        with open(EXP_FILE, "w") as file:
            json.dump(data, file)

    def reset(self):
        self.__init__()  # Reset stats to default values
        self.save_to_file()
        print("Character stats reset due to defeat.")

    @staticmethod
    def load_from_file():
        if os.path.exists(EXP_FILE):
            with open(EXP_FILE, "r") as file:
                data = json.load(file)
                return PlayerStats(**data)
        else:
            # Return a new player with default stats if file doesn't exist
            return PlayerStats()

# Function to handle experience gain based on enemy type
def gain_exp_for_enemy(enemy_name):
    if enemy_name == "Baby Dragon":
        return random.randint(30, 50)
    else:
        return random.randint(10, 15)

# Example usage
if __name__ == "__main__":
    player = PlayerStats.load_from_file()

    # Save progress
    player.save_to_file()
