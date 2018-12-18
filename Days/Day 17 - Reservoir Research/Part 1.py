def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    x = []
    y = []
    pairs = []

    for line in f:
        coordinates = line.split(" ")
        bounds = coordinates[1].split("..")
        for i in range(int(bounds[0][2:]), int(bounds[1]) + 1):
            if bounds[0][0] == "x":
                x.append(i)
                y.append(int(coordinates[0][2:-1]))
                pairs.append([i, int(coordinates[0][2:-1])])
            else:
                x.append(int(coordinates[0][2:-1]))
                y.append(i)
                pairs.append([int(coordinates[0][2:-1]), i])

    x.sort()
    x_min = x[0]
    x_max = x[-1]
    y.sort()
    y_min = y[0]
    y_max = y[-1]

    map_ = [["."]*(x_max + 2) for i in range(y_max + 2)]
    map_[0][500] = "|"

    for pair in pairs:
        map_[pair[1]][pair[0]] = "#"

    done = False

    while not done:
        done = True
        for i in range(y_max + 1):
            for j in range(x_min - 2, x_max + 2):
                if map_[i][j] == "|":
                    if map_[i + 1][j] == ".":
                        map_[i + 1][j] = "|"
                        done = False
                    elif map_[i + 1][j] in ["#", "~"]:
                        closed_left = False
                        closed_right = False
                        left = -1
                        right = 1

                        while map_[i][j + left] != "#" and map_[i + 1][j + left] in ["#", "~"]:
                            if map_[i][j + left] == ".":
                                map_[i][j + left] = "|"
                                done = False
                            left -= 1

                        if map_[i][j + left] == "#":
                            closed_left = True
                        elif map_[i][j + left] == ".":
                            map_[i][j + left] = "|"
                            done = False

                        while map_[i][j + right] != "#" and map_[i + 1][j + right] in ["#", "~"]:
                            if map_[i][j + right] == ".":
                                map_[i][j + right] = "|"
                                done = False
                            right += 1

                        if map_[i][j + right] == "#":
                            closed_right = True
                        elif map_[i][j + right] == ".":
                            map_[i][j + right] = "|"
                            done = False

                        if closed_left and closed_right:
                            for k in range(left + 1, right):
                                if map_[i][j + k] != "~":
                                    map_[i][j + k] = "~"
                                    done = False

    count = 0
    for i in range(y_min, y_max + 1):
        for j in range(x_max + 2):
            if map_[i][j] in ["|", "~"]:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
