def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    positions = []
    radii = []
    for line in f:
        comps = line.split(", ")
        positions.append([int(i) for i in comps[0][5:-1].split(",")])
        radii.append(int(comps[1][2:]))

    max_ = max(radii)
    position = positions[radii.index(max_)]
    count = 0
    for position_ in positions:
        if abs(position_[0] - position[0]) + abs(position_[1] - position[1]) + abs(position_[2] - position[2]) <= max_:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
