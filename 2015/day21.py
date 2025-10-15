
def day20(p):
    ## creating equipment
    weapons, armors, rings = create_equipments()

    ## creating player
    player = char("Player", 100, 0, 0)

    if p == 1:
        print("Day 21, Part 1 solution: " + str(get_results(player, weapons, armors, rings, 1)))
    
    if p == 2:
        print("Day 21, Part 2 solution: " + str(get_results(player, weapons, armors, rings, 2)))

def get_results(plr, weapons, armors, rings, part):
    lowest_win = -1
    highest_loss = 0
    highest_loss_set = ""

    for weapon_index in range(0, len(weapons), 1): ## goes through weapons
        for armor_index in range(0, len(armors), 1): ## goes through armors, starting with 0 cost no armor
            for ring1_index in range(0, len(rings), 1): ## goes through rings for slot 1, starting with 0 cost no ring
                for ring2_index in range(ring1_index + 1, len(rings), 1): ## goes through rings for slot 2, starting with no cost ring
                    ## adds possible weapon/armor/ring stats to player
                    plr.damage = weapons[weapon_index].damage + rings[ring1_index].damage + rings[ring2_index].damage
                    plr.armor = armors[armor_index].armor + rings[ring1_index].armor + rings[ring2_index].armor

                    ## resetting health
                    plr.health = 100
                    enemy = get_boss()

                    ## checks if player wins
                    total_cost = weapons[weapon_index].cost + armors[armor_index].cost + rings[ring1_index].cost + rings[ring2_index].cost
                    winner = combat(plr, enemy)
                    if winner == "Player":
                        if lowest_win == -1 or total_cost < lowest_win:
                            lowest_win = total_cost
                    if winner == "Boss":
                        if highest_loss < total_cost:
                            highest_loss_set = weapons[weapon_index].name + " " + armors[armor_index].name + " " + rings[ring1_index].name + " " + rings[ring2_index].name
                            highest_loss = total_cost

    if part == 1:
        return lowest_win
    if part == 2:
        print(highest_loss_set)
        return highest_loss
    
    return 0

def combat(plr, enemy):
    while True:
        ## player hits
        enemy.gets_hit(plr.damage)
        if enemy.health == 0:
            return plr.name
        
        ## boss hits
        plr.gets_hit(enemy.damage)
        if plr.health == 0:
            return enemy.name

def create_equipments():
    weapons = []
    wep1 = eq("Dagger", 8, 4, 0)
    wep2 = eq("Shortsword", 10, 5, 0)
    wep3 = eq("Warhammer", 25, 6, 0)
    wep4 = eq("Longsword", 40, 7, 0)
    wep5 = eq("Greataxe", 74, 8, 0)
    weapons.append(wep1)
    weapons.append(wep2)
    weapons.append(wep3)
    weapons.append(wep4)
    weapons.append(wep5)

    armors = []
    noarm = eq("No armor", 0, 0, 0)
    arm1 = eq("Leather", 13, 0, 1)
    arm2 = eq("Chainmail", 31, 0, 2)
    arm3 = eq("Splimtmail", 53, 0, 3)
    arm4 = eq("Bandedmail", 75, 0, 4)
    arm5 = eq("Platemail", 102, 0, 5)
    armors.append(noarm)
    armors.append(arm1)
    armors.append(arm2)
    armors.append(arm3)
    armors.append(arm4)
    armors.append(arm5)

    rings = []
    noring1 = eq("No ring 1", 0, 0, 0)
    noring2 = eq("No ring 2", 0, 0, 0)
    ring1 = eq("Damage +1", 25, 1, 0)
    ring2 = eq("Damage +2", 50, 2, 0)
    ring3 = eq("Damage +3", 100, 3, 0)
    ring4 = eq("Defense +1", 20, 0, 1)
    ring5 = eq("Defense +2", 40, 0, 2)
    ring6 = eq("Defense +3", 80, 0, 3)
    rings.append(noring1)
    rings.append(noring2)
    rings.append(ring1)
    rings.append(ring2)
    rings.append(ring3)
    rings.append(ring4)
    rings.append(ring5)
    rings.append(ring6)

    return weapons, armors, rings

def get_boss():
    boss = char("Boss", 104, 8, 1)
    return boss

class char:
    name = ""
    health = 0
    damage = 0
    armor = 0

    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
    
    def gets_hit(self, damage):
        if damage - self.armor < 1:
            self.health -= 1
        else:
            self.health -= damage - self.armor
        
        if self.health < 0:
            self.health = 0

class eq:
    name = ""
    cost = 0
    damage = 0
    armor = 0

    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor
