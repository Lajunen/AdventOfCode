import readfile

maximum_score = 0

def day13(p):
    global maximum_score
    data = readfile.read_lines(13)

    persons = create_persons(data)

    if p == 1:
        find_seating_order(persons, [])
        print("Day 13, Part 1 solution: " + str(maximum_score))
    
    if p == 2:
        ## adding myself to other likes
        like = ["Me", 0]
        for per in persons:
            per[1].append(like)

        ## creating a person for me and adding likes to all others
        new_person = []
        new_likes = []

        for per in persons:
            new_like = [per[0], 0]
            new_likes.append(new_like)

        ## adding name and likes to new person array
        new_person.append("Me")
        new_person.append(new_likes)

        ## adding person to persons array
        persons.append(new_person)

        find_seating_order(persons, [])
        print("Day 13, Part 2 solution: " + str(maximum_score))
            



def find_seating_order(persons, seated):
    if len(seated) == 0:
        ## just arrived and no one seated yet.
        ## seating first person and starting next round
        new_seats = []
        new_seats.append(persons[0][0])
        find_seating_order(persons, new_seats)
        
        return
    
    if len(seated) == len(persons):
        ## everyone seated
        global maximum_score

        score = calculate_score(persons, seated)

        if maximum_score == 0:
            ## no finished seatings yet, automatically highest score
            maximum_score = score
        else:
            if maximum_score < score:
                ## new highest score
                maximum_score = score
    else:
        ## seating next one who is not yet seated
        for per in persons:
            if per[0] not in seated:
                ## person not yet seated
                new_seats = []
                for seat in seated:
                    new_seats.append(seat)
                new_seats.append(per[0])
                find_seating_order(persons, new_seats)
        return

def calculate_score(persons, seats):
    ## calculating score based on seating
    i = 0
    score = 0

    while i < len(seats):
        for per in persons:
            if per[0] == seats[i]:
                ## current seat person in per variable
                for next_to in persons:
                    if next_to[0] == seats[i-1]:
                        ## previous seat person in next_to variable
                        for like in next_to[1]:
                            if like[0] == per[0]:
                                score += like[1]
                for like in per[1]:
                    if like[0] == seats[i-1]:
                        score += like[1]
        i += 1
    
    return score

def create_persons(data):
    persons = []
    for line in data:
        line = line.replace(".", "")
        info = line.split(" ")

        if len(persons) == 0:
            ## first entry
            new_person = []
            new_likes = []
            like = []

            ## creating like
            like.append(info[10])
            amount = int(info[3])
            if info[2] == "lose":
                amount *= (-1)
                print(amount)
            like.append(amount)

            ## adding like to likes array
            new_likes.append(like)

            ## adding name and likes to new person array
            new_person.append(info[0])
            new_person.append(new_likes)

            ## adding person to persons array
            persons.append(new_person)
        else:
            person_found = False
            for per in persons:
                if per[0] == info[0]:
                    ## name found, adding like
                    like = []
                    like.append(info[10])
                    amount = int(info[3])
                    if info[2] == "lose":
                        amount *= (-1)
                    like.append(amount)
                    per[1].append(like)
                    person_found = True

            if not person_found:
                ## person was not yet in the list
                new_person = []
                new_likes = []
                like = []

                ## creating like
                like.append(info[10])
                amount = int(info[3])
                if info[2] == "lose":
                    amount *= (-1)
                like.append(amount)

                ## adding like to likes array
                new_likes.append(like)

                ## adding name and likes to new person array
                new_person.append(info[0])
                new_person.append(new_likes)

                ## adding person to persons array
                persons.append(new_person)
    
    return persons
