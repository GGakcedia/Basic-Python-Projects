shields = {"iron": 20 ,"diamond": 50}
 
characters = {
    "character1" : {"weapon" : "sword",
                    "power" :  30,
                    "health" : 100,
                    "shield" : shields ["iron"]},
    "character2" : {"weapon" : "sword",
                    "power" :  30,
                    "health" : 100,
                    "shield" : shields ["diamond"]},            
}

def attack(attacking,attacked):
    pow = attacking["power"]
    heal = attacked["health"]
    shiel = attacked["shield"]
    damage = pow-shiel
    heal -= damage
    attacked["health"] = heal

print(characters["character2"]["health"])

attack(characters["character1"],characters["character2"])
print(characters["character2"]["health"])