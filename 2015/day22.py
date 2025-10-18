from copy import deepcopy

lowest_win_mana_consumption = -1
lowest_action_chain = ""

def day22(p):
    global lowest_win_mana_consumption
    plr = get_player()
    boss = get_boss()

    ##plr_array = get_player_array()
    ##boss_array = get_boss_array()

    if p == 1:
        ##part_one_arrays(plr_array, boss_array, 0, 0, "")
        part_one(plr, boss, "", 1)
        print("Day 22, Part 1 solution: " + str(lowest_win_mana_consumption))
    
    if p == 2:
        part_one(plr, boss, "", 2)
        print("Day 22, Part 2 solution: " + str(lowest_win_mana_consumption))

def part_one(plr, boss, path, part):
    for act in range(1, 6, 1):
        new_plr = deepcopy(plr)
        new_boss = deepcopy(boss)
        if act == 1:
            ## print("boss hp: " + str(new_boss.health) + " current path: " + path + "/mm")
            fight_round(new_plr, new_boss, act, path + "/mm", part)
        elif act == 2:
            ## print("boss hp: " + str(new_boss.health) + " current path: " + path + "/dr")
            fight_round(new_plr, new_boss, act, path + "/dr", part)
        elif act == 3:
            ## print("boss hp: " + str(new_boss.health) + " current path: " + path + "/sh")
            fight_round(new_plr, new_boss, act, path + "/sh", part)
        elif act == 4:
            ## print("boss hp: " + str(new_boss.health) + " current path: " + path + "/po")
            fight_round(new_plr, new_boss, act, path + "/po", part)
        elif act == 5:
            ## print("boss hp: " + str(new_boss.health) + " current path: " + path + "/re")
            fight_round(new_plr, new_boss, act, path + "/re", part)


def fight_round(plr, boss, act, path, part):
    global lowest_win_mana_consumption

    new_plr = deepcopy(plr)
    new_boss = deepcopy(boss)

    ## breaking out if more mana consumed than in record
    if new_plr.mana_spent > lowest_win_mana_consumption and lowest_win_mana_consumption != -1:
        return

    ## part 2 -1hp delivered
    if part == 2:
        new_plr.health -= 1
        if new_plr.health == 0:
            return
    
    new_plr.affect_timer_tick()
    new_boss.affect_timer_tick()
    if new_boss.health == 0:
        if lowest_win_mana_consumption > new_plr.mana_spent or lowest_win_mana_consumption == -1:
            lowest_win_mana_consumption = new_plr.mana_spent
            lowest_action_chain = path
            return
    
    if act == 1: ## magic missile
        if new_plr.mana < 53:
            return
        new_plr.cast_magic_missile()
        new_boss.magic_missile_hits()
        if new_boss.health == 0:
            if lowest_win_mana_consumption > new_plr.mana_spent or lowest_win_mana_consumption == -1:
                lowest_win_mana_consumption = new_plr.mana_spent
                lowest_action_chain = path
                return
    if act == 2: ## drain
        if new_plr.mana < 73:
            return
        new_plr.cast_drain()
        new_boss.drain_hits()
        if new_boss.health == 0:
            if lowest_win_mana_consumption > new_plr.mana_spent or lowest_win_mana_consumption == -1:
                lowest_win_mana_consumption = new_plr.mana_spent
                lowest_action_chain = path
                return
    if act == 3: ## shield
        if new_plr.mana < 113 or new_plr.is_status_affect_active("shield"):
            return
        new_plr.cast_shield()
    if act == 4: ## poison
        if new_plr.mana < 173 or new_boss.is_status_affect_active("poison"):
            return
        new_plr.cast_poison()
        new_boss.poison_hits()
    if act == 5: ## recharge
        if new_plr.mana < 229 or new_plr.is_status_affect_active("recharge"):
            return
        new_plr.cast_recharge()
    
    ## boss turn starts
    new_plr.affect_timer_tick()
    new_boss.affect_timer_tick()
    if new_boss.health == 0:
        if lowest_win_mana_consumption > new_plr.mana_spent or lowest_win_mana_consumption == -1:
            lowest_win_mana_consumption = new_plr.mana_spent
            lowest_action_chain = path
            return
    
    new_plr.take_physical_damage(new_boss.damage)
    if new_plr.health == 0:
        return

    part_one(new_plr, new_boss, path, part)


def show(rnd, plr, boss):
    print("round: " + str(rnd))
    print("player hp: " + str(plr.health) + " mana " + str(plr.mana))
    print("boss hp: " + str(boss.health))

def get_player():
    plr = character("Player", 50, 500, 0)
    return plr

def get_boss():
    boss = character("Boss", 58, 0, 9)
    return boss

class character:
    name = ""
    health = 0
    mana = 0
    damage = 0
    armor = 0
    mana_spent = 0
    status_affects = []

    def __init__(self, name, health, mana, damage):
        self.name = name
        self.health = health
        self.mana = mana
        self.damage = damage
        self.armor = 0
        self.mana_spent = 0
        self.status_affects = [["poison", 0], ["shield", 0], ["recharge", 0]]

    def take_physical_damage(self, amount):
        damage_done = amount - self.armor
        if damage_done < 1:
            damage_done = 1
        self.health -= damage_done
        if self.health < 0:
            self.health = 0

    def take_magic_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def affect_timer_tick(self):
        for affect_index in range(0, len(self.status_affects), 1):
            if self.status_affects[affect_index][1] > 0:
                if self.status_affects[affect_index][0] == "poison":
                    ## do poison stuff
                    self.health -= 3
                    self.status_affects[affect_index][1] -= 1
                    if self.health < 0:
                        self.health = 0
                elif self.status_affects[affect_index][0] == "shield":
                    ## do shield stuff
                    self.status_affects[affect_index][1] -= 1
                    if self.status_affects[affect_index][1] == 0:
                        self.armor = 0
                elif self.status_affects[affect_index][0] == "recharge":
                    ## do recharge stuff
                    self.mana += 101
                    self.status_affects[affect_index][1] -= 1

    def is_status_affect_active(self, affect):
        for affect_index in range(0, len(self.status_affects), 1):
            if self.status_affects[affect_index][0] == affect:
                if self.status_affects[affect_index][1] > 0:
                    return True
                else:
                    return False
                
    def activate_poison(self):
        for affect_index in range(0, len(self.status_affects), 1):
            if self.status_affects[affect_index][0] == "poison":
                ## add poison timer
                self.status_affects[affect_index][1] = 6
    
    def activate_shield(self):
        for affect_index in range(0, len(self.status_affects), 1):
            if self.status_affects[affect_index][0] == "shield":
                ## add shield timer and affect
                self.status_affects[affect_index][1] = 6
                self.armor = 7
    
    def activate_recharge(self):
        for affect_index in range(0, len(self.status_affects), 1):
            if self.status_affects[affect_index][0] == "recharge":
                ## add recharge timer
                self.status_affects[affect_index][1] = 5

    def cast_magic_missile(self):
        self.mana -= 53
        self.mana_spent += 53
    
    def magic_missile_hits(self):
        self.take_magic_damage(4)
    
    def cast_drain(self):
        self.health += 2
        self.mana -= 73
        self.mana_spent += 73

    def drain_hits(self):
        self.take_magic_damage(2)
    
    def cast_shield(self):
        self.mana -= 113
        self.mana_spent += 113
        self.activate_shield()
    
    def cast_poison(self):
        self.mana -= 173
        self.mana_spent += 173
    
    def poison_hits(self):
        self.activate_poison()
    
    def cast_recharge(self):
        self.mana -= 229
        self.mana_spent += 229
        self.activate_recharge()
