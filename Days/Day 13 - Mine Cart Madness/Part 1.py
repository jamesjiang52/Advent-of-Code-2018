def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    map_ = [list(line) for line in f]

    info = []

    for i in range(len(map_)):
        for j in range(len(map_[0])):
            if map_[i][j] == "v":
                info.append([i, j, "down", "left"])
                map_[i][j] = "|"
            elif map_[i][j] == ">":
                info.append([i, j, "right", "left"])
                map_[i][j] = "-"
            elif map_[i][j] == "^":
                info.append([i, j, "up", "left"])
                map_[i][j] = "|"
            elif map_[i][j] == "<":
                info.append([i, j, "left", "left"])
                map_[i][j] = "-"

    done = False
    while not done:
        info.sort()
        for i in info:
            y, x = i[0], i[1]
            if i[2] == "down":
                if map_[y + 1][x] == "/":
                    i[2] = "left"
                elif map_[y + 1][x] == "\\":
                    i[2] = "right"
                elif map_[y + 1][x] == "+":
                    if i[3] == "left":
                        i[2] = "right"
                        i[3] = "straight"
                    elif i[3] == "straight":
                        i[2] = "down"
                        i[3] = "right"
                    elif i[3] == "right":
                        i[2] = "left"
                        i[3] = "left"
                positions = [info_[0:2] for info_ in info]
                i[0] += 1

                if [y + 1, x] in positions:
                    print(x, y + 1)
                    done = True
                    break

            elif i[2] == "right":
                if map_[y][x + 1] == "/":
                    i[2] = "up"
                elif map_[y][x + 1] == "\\":
                    i[2] = "down"
                elif map_[y][x + 1] == "+":
                    if i[3] == "left":
                        i[2] = "up"
                        i[3] = "straight"
                    elif i[3] == "straight":
                        i[2] = "right"
                        i[3] = "right"
                    elif i[3] == "right":
                        i[2] = "down"
                        i[3] = "left"
                positions = [info_[0:2] for info_ in info]
                i[1] += 1

                if [y, x + 1] in positions:
                    print(x + 1, y)
                    done = True
                    break

            elif i[2] == "up":
                if map_[y - 1][x] == "/":
                    i[2] = "right"
                elif map_[y - 1][x] == "\\":
                    i[2] = "left"
                elif map_[y - 1][x] == "+":
                    if i[3] == "left":
                        i[2] = "left"
                        i[3] = "straight"
                    elif i[3] == "straight":
                        i[2] = "up"
                        i[3] = "right"
                    elif i[3] == "right":
                        i[2] = "right"
                        i[3] = "left"
                positions = [info_[0:2] for info_ in info]
                i[0] -= 1

                if [y - 1, x] in positions:
                    print(x, y - 1)
                    done = True
                    break

            elif i[2] == "left":
                if map_[y][x - 1] == "/":
                    i[2] = "down"
                elif map_[y][x - 1] == "\\":
                    i[2] = "up"
                elif map_[y][x - 1] == "+":
                    if i[3] == "left":
                        i[2] = "down"
                        i[3] = "straight"
                    elif i[3] == "straight":
                        i[2] = "left"
                        i[3] = "right"
                    elif i[3] == "right":
                        i[2] = "up"
                        i[3] = "left"
                positions = [info_[0:2] for info_ in info]
                i[1] -= 1

                if [y, x - 1] in positions:
                    print(x - 1, y)
                    done = True
                    break


if __name__ == "__main__":
    main()
