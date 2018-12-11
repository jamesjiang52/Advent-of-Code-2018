def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    positions_x = []
    positions_y = []
    velocities_x = []
    velocities_y = []

    for line in f:
        positions_x.append(int(line[10:16]))
        positions_y.append(int(line[18:24]))
        velocities_x.append(int(line[-7:-5]))
        velocities_y.append(int(line[-3:-1]))

    num = len(positions_x)
    count = 0

    while True:
        count += 1
        for i in range(num):
            positions_x[i] += velocities_x[i]
            positions_y[i] += velocities_y[i]

        min_x = min(positions_x)
        max_x = max(positions_x)
        min_y = min(positions_y)
        max_y = max(positions_y)

        if (max_x - min_x < 100) and (max_y - min_y < 100):
            for i in range(num):
                positions_x[i] -= min_x
                positions_y[i] -= min_y

            max_x -= min_x
            min_x = 0
            max_y -= min_y
            min_y = 0

            array = []
            for i in range(max_y + 1):
                arr = ["." for j in range(max_x + 1)]
                array.append(arr)

            for i in range(num):
                array[positions_y[i]][positions_x[i]] = "#"

            for i in range(max_y + 1):
                print("".join(array[i]))

            wait = input()


if __name__ == "__main__":
    main()
