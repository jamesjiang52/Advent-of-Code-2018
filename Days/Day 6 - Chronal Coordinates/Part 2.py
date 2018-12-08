def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    coordinates = []
    for line in f:
        coordinate = [int(i) for i in line.split(", ")]
        coordinates.append(coordinate)

    count = 0

    for i in range(400):
        for j in range(400):
            sum_ = 0
            for coordinate in coordinates:
                sum_ += abs(coordinate[0] - i) + abs(coordinate[1] - j)

            if sum_ < 10000:
                count += 1

    print(count)


if __name__ == "__main__":
    main()
