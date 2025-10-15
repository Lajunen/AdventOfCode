from copy import deepcopy

lowest_win_mana_consumption = -1

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

def part_one(plr, boss, path, rnd):
    for act in range(1, 6, 1):
        new_plr = deepcopy(plr)
        new_boss = deepcopy(boss)
        if act == 1:
            print("boss hp: " + str(new_boss.health) + " current path: " + path + "/mm")
            fight_round(new_plr, new_boss, act, path + "/mm", rnd)
        elif act == 2:
            print("boss hp: " + str(new_boss.health) + " current path: " + path + "/dr")
            fight_round(new_plr, new_boss, act, path + "/dr", rnd)
        elif act == 3:
            print("boss hp: " + str(new_boss.health) + " current path: " + path + "/sh")
            fight_round(new_plr, new_boss, act, path + "/sh", rnd)
        elif act == 4:
            print("boss hp: " + str(new_boss.health) + " current path: " + path + "/po")
            fight_round(new_plr, new_boss, act, path + "/po", rnd)
        elif act == 5:
            print("boss hp: " + str(new_boss.health) + " current path: " + path + "/re")
            fight_round(new_plr, new_boss, act, path + "/re", rnd)


def fight_round(plr, boss, act, path, rnd):
    global lowest_win_mana_consumption

    new_plr = deepcopy(plr)
    new_boss = deepcopy(boss)

    ## breaking out if more mana consumed than in record
    if new_plr.mana_spent > lowest_win_mana_consumption and lowest_win_mana_consumption != -1:
        return

    new_plr.affect_timer_tick()
    new_boss.affect_timer_tick()
    if new_boss.health == 0:
        if lowest_win_mana_consumption > new_plr.mana_spent or lowest_win_mana_consumption == -1:
            lowest_win_mana_consumption = new_plr.mana_spent
            return
    
    if act == 1: ## magic missile
        if new_plr.mana < 53:
            return
        new_plr.cast_magic_missile()
        new_boss.magic_missile_hits()
        if new_boss.health == 0:
            if lowest_win_mana_consumption > new_plr.mana_spent or lowest_win_mana_consumption == -1:
                lowest_win_mana_consumption == new_plr.mana_spent
                return
    if act == 2: ## drain
        if new_plr.mana < 73:
            return
        new_plr.cast_drain()
        new_boss.drain_hits()
        if new_boss.health == 0:
            if lowest_win_mana_consumption > new_plr.mana_spent or lowest_win_mana_consumption == -1:
                lowest_win_mana_consumption == new_plr.mana_spent
                return
    if act == 3: ## shield
        if new_plr.mana < 113 or new_plr.is_status_affect_active("shield"):
            return
        new_plr.activate_shield()
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
            return
    
    new_plr.take_physical_damage(new_boss.damage)
    if new_plr.health == 0:
        return

    part_one(new_plr, new_boss, path, rnd + 1)


def show(rnd, plr, boss):
    print("round: " + str(rnd))
    print("player hp: " + str(plr.health) + " mana " + str(plr.mana))
    print("boss hp: " + str(boss.health))

def get_player_array():
    hp = 50
    mana = 500
    armor = 0
    shield = 0
    recharge = 0
    plr_arr = [hp, mana, armor, shield, recharge]

    return plr_arr

def get_boss_array():
    hp = 58
    damage = 9
    poison = 0

    boss_arr = [hp, damage, poison]

    return boss_arr

def part_one_arrays(plr, boss, mana_consumed, rnd, path):
    for act in range(1, 6, 1):
        new_plr = deepcopy(plr)
        new_boss = deepcopy(boss)
        if act == 1:
            print("round: " + str(rnd) + " path: " + path + "/mm")
            fight_round_arrays(new_plr, new_boss, mana_consumed, act, rnd + 1, path + "/mm")
        elif act == 2:
            print("round: " + str(rnd) + " path: " + path + "/dr")
            fight_round_arrays(new_plr, new_boss, mana_consumed, act, rnd + 1, path + "/dr")
        elif act == 3:
            print("round: " + str(rnd) + " path: " + path + "/sh")
            fight_round_arrays(new_plr, new_boss, mana_consumed, act, rnd + 1, path + "/sh")
        elif act == 4:
            print("round: " + str(rnd) + " path: " + path + "/po")
            fight_round_arrays(new_plr, new_boss, mana_consumed, act, rnd + 1, path + "/po")
        elif act == 5:
            print("round: " + str(rnd) + " path: " + path + "/re")
            fight_round_arrays(new_plr, new_boss, mana_consumed, act, rnd + 1, path + "/re")

def fight_round_arrays(plr, boss, mana_spent, act, rnd, path):
    global lowest_win_mana_consumption
    fight_over = False

    if lowest_win_mana_consumption != -1 and lowest_win_mana_consumption < mana_spent:
        fight_over = True
        return
    ## player turn ticks
    new_plr, new_boss, fight_over = tick_arrays(plr, boss, mana_spent)
    if fight_over:
        return
    
    ## player action
    if act == 1:
        new_plr, new_boss, new_mana, fight_over = cast_magic_missile_arrays(new_plr, new_boss, mana_spent)
    if act == 2:
        new_plr, new_boss, new_mana, fight_over = cast_drain_arrays(new_plr, new_boss, mana_spent)
    if act == 3:
        new_plr, new_mana, fight_over = cast_shield_arrays(new_plr, mana_spent)
    if act == 4:
        new_plr, new_boss, new_mana, fight_over = cast_poison_arrays(new_plr, new_boss, mana_spent)
    if act == 5:
        new_plr, new_mana, fight_over = cast_recharge_arrays(new_plr, mana_spent)
    if fight_over:
        return
    
    ## boss turn ticks
    new_plr, new_boss, fight_over = tick_arrays(new_plr, new_boss, mana_spent)
    if fight_over:
        return
    
    ## boss attack
    new_plr, fight_over = take_physical_damage_arrays(new_plr, new_boss)
    if fight_over:
        return

    part_one_arrays(new_plr, new_boss, new_mana, rnd, path)
    
def cast_recharge_arrays(plr, mana_spent):
    fight_over = False

    if plr[1] < 229 or plr[4] > 0:
        fight_over = True
        return plr, mana_spent, fight_over
    plr[1] -= 229
    new_mana_spent = mana_spent + 229
    plr[4] = 5

    return plr, new_mana_spent, fight_over

def cast_poison_arrays(plr, boss, mana_spent):
    fight_over = False

    if plr[1] < 173 or boss[2] > 0:
        fight_over = True
        return plr, boss, mana_spent, fight_over
    plr[1] -= 173
    new_mana_spent = mana_spent + 173
    boss[2] = 6

    return plr, boss, new_mana_spent, fight_over

def cast_shield_arrays(plr, mana_spent):
    fight_over = False

    if plr[1] < 113 or plr[3] > 0:
        fight_over = True
        return plr, mana_spent, fight_over
    plr[1] -= 113
    new_mana_spent = mana_spent + 113
    plr[2] = 7
    plr[3] = 6

    return plr, new_mana_spent, fight_over

def cast_drain_arrays(plr, boss, mana_spent):
    global lowest_win_mana_consumption
    fight_over = False

    if plr[1] < 73:
        fight_over = True
        return plr, boss, mana_spent, fight_over
    plr[0] += 2
    plr[1] -= 73
    new_mana_spent = mana_spent + 73
    boss, fight_over = take_magic_damage_arrays(boss, 2)
    if fight_over:
        if new_mana_spent < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
            lowest_win_mana_consumption = new_mana_spent
            return plr, boss, new_mana_spent, fight_over
    
    return plr, boss, new_mana_spent, fight_over
    
def cast_magic_missile_arrays(plr, boss, mana_spent):
    global lowest_win_mana_consumption
    fight_over = False

    if plr[1] < 53:
        fight_over = True
        return plr, boss, mana_spent, fight_over
    plr[1] -= 53
    new_mana_spent = mana_spent + 53
    boss, fight_over = take_magic_damage_arrays(boss, 3)
    if fight_over:
        if new_mana_spent < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
            lowest_win_mana_consumption = new_mana_spent
            return plr, boss, new_mana_spent, fight_over
    
    return plr, boss, new_mana_spent, fight_over

def take_physical_damage_arrays(plr, boss):
    fight_over = False

    damage_done = boss[1] - plr[2]
    if damage_done < 1:
        damage_done = 1
    plr[0] -= damage_done
    if plr[0] <= 0:
        plr[0] = 0
        fight_over = True
    
    return plr, fight_over

def take_magic_damage_arrays(boss, dam):
    fight_over = False

    boss[0] -= 3
    if boss[0] <= 0:
        boss[0] = 0
        fight_over = True
        
    return boss, fight_over

def tick_arrays(plr, boss, mana_spent):
    global lowest_win_mana_consumption
    fight_over = False

    ## tick player array
    if plr[3] > 0: ## shield active
        plr[3] -= 1
    if plr[4] > 0: ## recharge active
        plr[4] -= 1
        plr[1] += 101
    
    ## tick boss array
    if boss[2] > 0: ## poison active
        boss[2] -= 1
        boss[0] -= 3
        if boss[0] < 0:
            boss[0] = 0
            fight_over == True
            if mana_spent < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                lowest_win_mana_consumption = mana_spent
    
    return plr, boss, fight_over

def part_one_old(plr, boss, mana_consumed, rnd):
    global lowest_win_mana_consumption

    ## arrived to start new round of combat
    for act in range(1, 6, 1): ## player actions
        if act == 1: ## magic missile: mana cost 53
            new_plr = deepcopy(plr)
            new_boss = deepcopy(boss)
            ## player turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed
                    print("player wins!")
                    return
            if new_plr.mana < 53:
                return
            new_plr.mana -= 53
            new_boss.take_magic_damage(4) 
            if new_boss.health == 0:
                if mana_consumed + 53 < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed + 53
                    print("player wins!")
                    return

            ## boss turn            
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed + 53 < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed + 53
                    print("player wins!")
                    return
            new_plr.take_physical_damage(new_boss.damage)
            if new_plr.health == 0:
                ##print("player loses")
                return
                
            part_one(new_plr, new_boss, mana_consumed + 53, rnd + 1)
        if act == 2: ## drain spell: mana cost 73
            new_plr = deepcopy(plr)
            new_boss = deepcopy(boss)
            ## player turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed
                    print("player wins!")
                    return
            if new_plr.mana < 73:
                ##print("player loses")
                return
            new_plr.mana -= 73
            new_plr.health += 2
            new_boss.take_magic_damage(2)
            if new_boss.health == 0:
                if mana_consumed + 73 < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed + 73
                    print("player wins!")
                    return
                
            ## boss turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed + 73 < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed + 73
                    print("player wins!")
                    return
            new_plr.take_physical_damage(new_boss.damage)
            if new_plr.health == 0:
                ##print("player loses")
                return

            part_one(new_plr, new_boss, mana_consumed + 73, rnd + 1) ## next round
        if act == 3: ## shield spell: mana cost 113
            new_plr = deepcopy(plr)
            new_boss = deepcopy(boss)
            ## player turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed
                    print("player wins!")
                    return
            if new_plr.mana < 113 or new_plr.is_status_affect_active("shield"):
                    ##print("player loses")
                    return
            new_plr.mana -= 113
            new_plr.activate_shield()

            ## boss turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed + 113 < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed + 113
                    print("player wins!")
                    return
            new_plr.take_physical_damage(new_boss.damage)
            if new_plr.health == 0:
                ##print("player loses")
                return
                
            part_one(new_plr, new_boss, mana_consumed + 113, rnd + 1)
        if act == 4: ## poison cast: mana cost 173
            new_plr = deepcopy(plr)
            new_boss = deepcopy(boss)
            ## player turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed
                    print("player wins!")
                    return
            if new_plr.mana < 173 or new_boss.is_status_affect_active("poison"):
                ##print("player loses")
                return
            new_plr.mana -= 173
            new_boss.activate_poison()

            ## boss turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed + 173 < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed + 173
                    print("player wins!")
                    return
            new_plr.take_physical_damage(new_boss.damage)
            if new_plr.health == 0:
                ##print("player loses")
                return
               
            part_one(new_plr, new_boss, mana_consumed + 173, rnd + 1)
        if act == 5: ## recharge spell: mana cost 229
            new_plr = deepcopy(plr)
            new_boss = deepcopy(boss)
            ## player turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed
                    print("player wins!")
                    return
            if new_plr.mana < 229  or new_plr.is_status_affect_active("recharge"):
                ##print("player loses")
                return
            new_plr.mana -= 229
            new_plr.activate_recharge()

            ## boss turn
            new_plr.affect_timer_tick()
            new_boss.affect_timer_tick()
            if new_boss.health == 0:
                if mana_consumed + 229 < lowest_win_mana_consumption or lowest_win_mana_consumption == -1:
                    lowest_win_mana_consumption = mana_consumed + 229
                    print("player wins!")
            new_plr.take_physical_damage(new_boss.damage)
            if new_plr.health == 0:
                ##print("player loses")
                return

            ##print("fight goes on!")
            part_one(new_plr, new_boss, mana_consumed + 229, rnd + 1)

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

day22(1)