def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    coordinates = []
    for line in f:
        coordinate = [int(i) for i in line.split(", ")]
        coordinates.append(coordinate)

    all_ = []
    for i in range(400):
        all_.append(["."]*400)

    for i in range(len(coordinates)):
        all_[coordinates[i][1]][coordinates[i][0]] = i

    dict_counts = {}

    for i in range(400):
        for j in range(400):
            min_dist = 1000000
            num = 0
            count = 0

            for coordinate in coordinates:
                dist = abs(coordinate[0] - i) + abs(coordinate[1] - j)
                min_dist = min(min_dist, dist)

            for coordinate in coordinates:
                dist = abs(coordinate[0] - i) + abs(coordinate[1] - j)
                if dist == min_dist:
                    num = all_[coordinate[1]][coordinate[0]]
                    count += 1

            if count > 1:
                pass
            else:
                if num not in dict_counts:
                    dict_counts[num] = 1
                else:
                    dict_counts[num] += 1
                all_[j][i] = num

    edges = []
    for i in range(400):
        edges.append(all_[0][i])
        edges.append(all_[399][i])
        edges.append(all_[i][0])
        edges.append(all_[i][399])

    edges = list(set(edges))

    max_ = 0
    for key, value in dict_counts.items():
        if key in edges:
            continue
        else:
            max_ = max(max_, value)

    print(max_)


if __name__ == "__main__":
    main()
