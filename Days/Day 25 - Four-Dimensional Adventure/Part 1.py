def create_new_constellation(positions_):
    positions = [i[:] for i in positions_]
    constellation = [positions.pop(0)]
    while True:
        for i in range(len(positions)):
            position = positions[i]
            for star in constellation:
                if abs(star[0] - position[0]) + abs(star[1] - position[1]) + abs(star[2] - position[2]) + abs(star[3] - position[3]) <= 3:
                    constellation.append(position)
                    positions[i] = "remove"
                    break

        if "remove" not in positions:
            return constellation

        positions = [i for i in positions if i != "remove"]


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    stars = [[int(i) for i in line.split(",")] for line in f]
    constellations = []

    while len(stars) > 0:
        new_constellation = create_new_constellation(stars)
        constellations.append(new_constellation)

        for star in new_constellation:
            stars.remove(star)

    print(len(constellations))


if __name__ == "__main__":
    main()
