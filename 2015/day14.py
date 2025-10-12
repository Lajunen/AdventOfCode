import readfile

def day14(p):
    data = readfile.read_lines(14)

    deers = parse_data(data)

    if p == 1:
        deers = fly_for_time(deers, 2503)
        fastest = deer()
        for d in deers:
            if d.travelled > fastest.travelled:
                fastest = d
        print("Day 14, Part 1 solution: " + str(fastest.travelled))
    
    if p == 2:
        deers = fly_for_time(deers, 2503)
        first = deer()
        for d in deers:
            if d.points > first.points:
                first = d
        print("Day 14, Part 2 solution: " + str(first.points))

def parse_data(data):
    deers = []

    for line in data:
        info = line.split(" ")

        new_deer = deer()
        new_deer.name = info[0]
        new_deer.speed = int(info[3])
        new_deer.fly_time = int(info[6])
        new_deer.rest_time = int(info[13])

        deers.append(new_deer)
    
    return deers

def fly_for_time(deers, time):
    for i in range(time):
        first_distance = 0

        ## flying each deer for one second and taking note of first place deer distance
        for d in deers:
            d.travel()
            if d.travelled > first_distance:
                first_distance = d.travelled

        ## awarding points to first place deer(s)
        for d in deers:
            if d.travelled == first_distance:
                d.award_point()
        
    return deers

class deer:
    name = ""
    speed = 0
    fly_time = 0
    flown_time = 0
    rest_time = 0
    rested_time = 0
    resting = False
    travelled = 0
    points = 0

    def award_point(self):
        self.points += 1

    def travel(self):
        if self.resting:
            self.rested_time += 1
            if self.rested_time == self.rest_time:
                self.rested_time = 0
                self.resting = False
        else:
            self.travelled += self.speed
            self.flown_time += 1
            if self.flown_time == self.fly_time:
                self.flown_time = 0
                self.resting = True
