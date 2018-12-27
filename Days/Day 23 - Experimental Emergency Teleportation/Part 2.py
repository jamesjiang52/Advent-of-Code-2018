import math


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    positions = []
    radii = []
    for line in f:
        comps = line.split(", ")
        positions.append([int(i) for i in comps[0][5:-1].split(",")])
        radii.append(int(comps[1][2:]))

    positions_x = [position[0] for position in positions]
    positions_y = [position[1] for position in positions]
    positions_z = [position[2] for position in positions]

    width = 2**(int(math.log(max(positions_x) - min(positions_x), 2)) + 1)

    max_ = 0
    max_distance = 100000000000
    max_position = []
    for x in range(min(positions_x), max(positions_x) + 1, width):
        for y in range(min(positions_y), max(positions_y) + 1, width):
            for z in range(min(positions_z), max(positions_z) + 1, width):
                count = 0
                for i in range(len(positions)):
                    position = positions[i]
                    radius = radii[i]
                    if abs(x - position[0]) + abs(y - position[1]) + abs(z - position[2]) < width + radius:
                        count += 1
                if count > max_:
                    max_ = count
                    max_distance = abs(x) + abs(y) + abs(z)
                    max_position = [x, y, z]
                elif count == max_:
                    if abs(x) + abs(y) + abs(z) < max_distance:
                        max_distance = abs(x) + abs(y) + abs(z)
                        max_position = [x, y, z]

    x_range = [max_position[0] - width, max_position[0] + width]
    y_range = [max_position[1] - width, max_position[1] + width]
    z_range = [max_position[2] - width, max_position[2] + width]

    width = width//2

    while True:
        max_ = 0
        max_distance = 100000000000
        max_position = []
        for x in range(x_range[0], x_range[1], width):
            for y in range(y_range[0], y_range[1], width):
                for z in range(z_range[0], z_range[1], width):
                    count = 0
                    for i in range(len(positions)):
                        position = positions[i]
                        radius = radii[i]
                        if abs(x - position[0]) + abs(y - position[1]) + abs(z - position[2]) < width + radius:
                            count += 1
                    if count > max_:
                        max_ = count
                        max_distance = abs(x) + abs(y) + abs(z)
                        max_position = [x, y, z]
                    elif count == max_:
                        if abs(x) + abs(y) + abs(z) < max_distance:
                            max_distance = abs(x) + abs(y) + abs(z)
                            max_position = [x, y, z]

        if width == 1:
            print(max_distance)
            break

        x_range = [max_position[0] - width, max_position[0] + width]
        y_range = [max_position[1] - width, max_position[1] + width]
        z_range = [max_position[2] - width, max_position[2] + width]

        width = width//2


if __name__ == "__main__":
    main()
