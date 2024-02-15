import random
import os

class Enemy():
    def __init__(self):
        self.alive = True
        self.health = random.randint(40,70)
        self.shield = random.randint(0,10)
        self.strength = random.randint(20,50)

    def attack(self, player):
        damage = self.strength - player.shield
        if damage > 0:
            player.health -= damage
        if player.health <= 0:
            player.alive = False

class Player():
    def __init__(self):
        self.alive = True
        self.health = 500
        self.shield = 20
        self.strength = 55

    def attack(self, enemy):
        damage = self.strength - enemy.shield
        if damage > 0:
            enemy.health -= damage
        if enemy.health <= 0:
            enemy.alive = False

enemys = [Enemy() for _ in range(6)]
player = Player()

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("Player Status -----> Health: {} ------ Strength: {} ------ Shield: {}".format(player.health, player.strength, player.shield))
    
    if not player.alive:
        print("Game Over! :(")
        break

    if not any(e.alive for e in enemys):
        print("!!Congratulations!!")
        break

    for index, enemy in enumerate(enemys):
        if enemy.alive:
            print("{}.enemy -----> Health: {} ------ Strength: {} ------ Shield: {}".format(index, enemy.health, enemy.strength, enemy.shield))

    while True:
        try:
            choose = int(input("Choose Enemy:"))
            if 0 <= choose < len(enemys) and enemys[choose].alive:
                break
            else:
                print("Invalid choice. Please choose a valid enemy.")
        except ValueError:
            print("Please enter a number.")

    chosen_enemy = enemys[choose]
    player.attack(chosen_enemy)

    # Let the enemies attack the player
    for enemy in enemys:
        if enemy.alive:
            enemy.attack(player)

attacker = enemys[random.randint(0,len(enemys)-1)]
attacker.attack(player)