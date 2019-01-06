def is_in_range(map_, position_y, position_x, char):
    if char == "G":
        for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            if map_[position_y + direction[0]][position_x + direction[1]] == "E":
                return True
        return False
    else:
        for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            if map_[position_y + direction[0]][position_x + direction[1]] == "G":
                return True
        return False


def get_valid_locations(map_, char):
    locations = []
    if char == "G":
        for i in range(1, len(map_) - 1):
            for j in range(1, len(map_[0]) - 1):
                if map_[i][j] == "E":
                    for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                        if map_[i + direction[0]][j + direction[1]] == ".":
                            locations.append((i + direction[0], j + direction[1]))
        return locations
    else:
        for i in range(1, len(map_) - 1):
            for j in range(1, len(map_[0]) - 1):
                if map_[i][j] == "G":
                    for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                        if map_[i + direction[0]][j + direction[1]] == ".":
                            locations.append((i + direction[0], j + direction[1]))
        return locations


def find_path(map_, curr_position, targets):
    visited = [[0]*len(map_[0]) for i in range(len(map_))]
    check = [[curr_position]]
    visited[curr_position[0]][curr_position[1]] = 1

    while len(check) > 0:
        check_next = []
        while len(check) > 0:
            path = check.pop(0)
            position = path[-1]

            if position in targets:
                return path

            for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                direction_y = direction[0]
                direction_x = direction[1]
                if map_[position[0] + direction_y][position[1] + direction_x] == "." and visited[position[0] + direction_y][position[1] + direction_x] != 1:
                    visited[position[0] + direction_y][position[1] + direction_x] = 1
                    check_next.append(path + [(position[0] + direction_y, position[1] + direction_x)])

        check = sorted(check_next, key=lambda path: path[-1])

    return []


def attack(map_, units, position_y, position_x, char, power):
    positions = [unit[0:2] for unit in units]
    if char == "G":
        min_hp = 200
        for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            if map_[position_y + direction[0]][position_x + direction[1]] == "E":
                min_hp = min(min_hp, units[positions.index([position_y + direction[0], position_x + direction[1]])][3])

        for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            if map_[position_y + direction[0]][position_x + direction[1]] == "E" and units[positions.index([position_y + direction[0], position_x + direction[1]])][3] == min_hp:
                unit = units[positions.index([position_y + direction[0], position_x + direction[1]])]
                unit[3] -= 3
                if unit[3] <= 0:
                    map_[position_y + direction[0]][position_x + direction[1]] = "."
                    unit[0] = -1
                    unit[1] = -1
                return

    else:
        min_hp = 200
        for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            if map_[position_y + direction[0]][position_x + direction[1]] == "G":
                min_hp = min(min_hp, units[positions.index([position_y + direction[0], position_x + direction[1]])][3])

        for direction in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            if map_[position_y + direction[0]][position_x + direction[1]] == "G" and units[positions.index([position_y + direction[0], position_x + direction[1]])][3] == min_hp:
                unit = units[positions.index([position_y + direction[0], position_x + direction[1]])]
                unit[3] -= power
                if unit[3] <= 0:
                    map_[position_y + direction[0]][position_x + direction[1]] = "."
                    unit[0] = -1
                    unit[1] = -1
                return


def move(map_, units, new_position, position_y, position_x, char):
    map_[position_y][position_x] = "."
    map_[new_position[0]][new_position[1]] = char

    positions = [unit[0:2] for unit in units]
    index_ = positions.index([position_y, position_x])
    unit = units[index_]

    unit[0], unit[1] = new_position[0], new_position[1]


def over(units, char):
    if char == "G":
        for unit in units:
            if unit[2] == "E" and unit[3] > 0:
                return False
        return True

    else:
        for unit in units:
            if unit[2] == "G" and unit[3] > 0:
                return False
        return True


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    map_orig = [list(line) for line in f]
    units_orig = []
    num_elves = 0

    for i in range(len(map_orig)):
        for j in range(len(map_orig[0])):
            if map_orig[i][j] == "G":
                units_orig.append([i, j, "G", 200])
            elif map_orig[i][j] == "E":
                units_orig.append([i, j, "E", 200])
                num_elves += 1

    power = 4
    while True:
        map_ = [map_orig[i][:] for i in range(len(map_orig))]
        units = [units_orig[i][:] for i in range(len(units_orig))]
        rounds = 0
        done = False
        while True:
            units.sort()
            for unit in units:
                if unit[3] <= 0:
                    continue

                if over(units, unit[2]):
                    elves_health = [(unit_[3] > 0) for unit_ in units if unit_[2] == "E"]
                    if elves_health.count(True) == num_elves:
                        print(units)
                        print(power)
                        total_hp = sum([unit_[3] for unit_ in units if unit_[3] > 0])
                        print(rounds*total_hp)
                        return
                    else:
                        done = True
                        break

                if not is_in_range(map_, unit[0], unit[1], unit[2]):
                    locations = get_valid_locations(map_, unit[2])
                    path = find_path(map_, unit[0:2], locations)

                    if path != []:
                        move(map_, units, path[1], unit[0], unit[1], unit[2])

                if is_in_range(map_, unit[0], unit[1], unit[2]):
                    attack(map_, units, unit[0], unit[1], unit[2], power)

            if done:
                break
            else:
                rounds += 1

        power += 1


if __name__ == "__main__":
    main()
