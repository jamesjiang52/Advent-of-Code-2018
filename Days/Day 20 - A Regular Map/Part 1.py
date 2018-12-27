def main():
    f = [line.rstrip("\n")[1:-1] for line in open("Data.txt")][0]

    directions = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}
    map_ = {}

    positions_stack = []
    curr_x, curr_y = 5000, 5000
    prev_x, prev_y = curr_x, curr_y
    distances = {(prev_x, prev_y): 0}

    for char in f:
        if char == "(":
            positions_stack.append([curr_x, curr_y])
        elif char == ")":
            position = positions_stack.pop(-1)
            curr_x = position[0]
            curr_y = position[1]
        elif char == "|":
            position = positions_stack[-1]
            curr_x = position[0]
            curr_y = position[1]
        else:
            direction_x, direction_y = directions[char]
            curr_x += direction_x
            curr_y += direction_y

            if (curr_x, curr_y) not in map_:
                map_[(curr_x, curr_y)] = [(prev_x, prev_y)]
            else:
                map_[(curr_x, curr_y)].append((prev_x, prev_y))

            if (curr_x, curr_y) not in distances:
                distances[(curr_x, curr_y)] = distances[(prev_x, prev_y)] + 1
            else:
                distances[(curr_x, curr_y)] = min(distances[(curr_x, curr_y)], distances[(prev_x, prev_y)] + 1)

        prev_x, prev_y = curr_x, curr_y

    print(max(distances.values()))


if __name__ == "__main__":
    main()
