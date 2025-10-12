import readfile

shortest = 0

def day09(p):
    global shortest
    distances = readfile.read_lines(9)

    routes = sort_distances(distances)
    
    visited = []

    if p == 1:
        find_routes(routes, visited, 0, 1)
        print("Day 09, Part 1 solution: " + str(shortest))
    
    if p == 2:
        find_routes(routes, visited, 0, 2)
        print("Day 09, Part 2 solution: " + str(shortest))

def find_routes(routes, visited, length, part):
    global shortest
    ## first visit to loop, adding starting point but no length yet
    if len(visited) == 0:
        for route in routes:
            new_visits = []
            new_visits.append(route[0])

            find_routes(routes, new_visits, 0, part)

    ## mid journey, finding next destination and adding it there
    if len(visited) > 0 and len(visited) < 8:
        for route in routes:
            if route[0] == visited[-1] and route[1] not in visited:
                new_visits = []
                for visit in visited:
                    new_visits.append(visit)
                new_visits.append(route[1])
                find_routes(routes, new_visits, length + route[2], part)
            if route[1] == visited[-1] and route[0] not in visited:
                new_visits = []
                for visit in visited:
                    new_visits.append(visit)
                new_visits.append(route[0])
                find_routes(routes, new_visits, length + route[2], part)
        return

    if len(visited) == 8:
        if part == 1:
            if shortest == 0 or (shortest > 0 and length > 0 and length < shortest):
                shortest = length
        if part == 2:
            if shortest == 0 or (shortest > 0 and length > 0 and length > shortest):
                shortest = length
    
    return


def sort_distances(distances):
    routes = []

    for line in distances:
        info = line.split(" ")
        new_route = (info[0], info[2], int(info[4]))
        routes.append(new_route)
    return routes