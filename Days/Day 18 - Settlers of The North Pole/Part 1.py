def get_neighbor_counts(map_, x, y):
    open_count = 0
    wooded_count = 0
    lumber_count = 0

    if x > 0 and y > 0:
        if map_[y - 1][x - 1] == ".":
            open_count += 1
        elif map_[y - 1][x - 1] == "|":
            wooded_count += 1
        else:
            lumber_count += 1

    if y > 0:
        if map_[y - 1][x] == ".":
            open_count += 1
        elif map_[y - 1][x] == "|":
            wooded_count += 1
        else:
            lumber_count += 1

    if x < 49 and y > 0:
        if map_[y - 1][x + 1] == ".":
            open_count += 1
        elif map_[y - 1][x + 1] == "|":
            wooded_count += 1
        else:
            lumber_count += 1

    if x > 0:
        if map_[y][x - 1] == ".":
            open_count += 1
        elif map_[y][x - 1] == "|":
            wooded_count += 1
        else:
            lumber_count += 1

    if x < 49:
        if map_[y][x + 1] == ".":
            open_count += 1
        elif map_[y][x + 1] == "|":
            wooded_count += 1
        else:
            lumber_count += 1

    if x > 0 and y < 49:
        if map_[y + 1][x - 1] == ".":
            open_count += 1
        elif map_[y + 1][x - 1] == "|":
            wooded_count += 1
        else:
            lumber_count += 1

    if y < 49:
        if map_[y + 1][x] == ".":
            open_count += 1
        elif map_[y + 1][x] == "|":
            wooded_count += 1
        else:
            lumber_count += 1

    if x < 49 and y < 49:
        if map_[y + 1][x + 1] == ".":
            open_count += 1
        elif map_[y + 1][x + 1] == "|":
            wooded_count += 1
        else:
            lumber_count += 1

    return open_count, wooded_count, lumber_count


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    map_ = [list(line) for line in f]

    for i in range(10):
        new_map = [["."]*50 for j in range(50)]
        for j in range(50):
            for k in range(50):
                counts = get_neighbor_counts(map_, k, j)
                if map_[j][k] == ".":
                    if counts[1] >= 3:
                        new_map[j][k] = "|"
                    else:
                        new_map[j][k] = "."
                elif map_[j][k] == "|":
                    if counts[2] >= 3:
                        new_map[j][k] = "#"
                    else:
                        new_map[j][k] = "|"
                else:
                    if counts[1] >= 1 and counts[2] >= 1:
                        new_map[j][k] = "#"
                    else:
                        new_map[j][k] = "."

        map_ = new_map

    wooded_count = 0
    lumber_count = 0

    for i in range(50):
        wooded_count += map_[i].count("|")
        lumber_count += map_[i].count("#")

    print(wooded_count*lumber_count)


if __name__ == "__main__":
    main()
