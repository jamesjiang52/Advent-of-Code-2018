import heapq


def time(types, target):
    times_dict = {}
    queue = [(0, 0, 0, "torch")]

    while len(queue) > 0:
        time_, pos_y, pos_x, curr_item = heapq.heappop(queue)
        key = (pos_y, pos_x, curr_item)

        if key in times_dict and times_dict[key] <= time_:
            continue

        times_dict[key] = time_

        if key == target:
            return time_

        for item in ["neither", "torch", "climbing gear"]:
            if item != curr_item and item != ["neither", "torch", "climbing gear"][types[pos_y][pos_x]]:
                heapq.heappush(queue, (time_ + 7, pos_y, pos_x, item))

        for direction in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            new_y = pos_y + direction[0]
            new_x = pos_x + direction[1]
            if new_y < 0:
                continue
            if new_y > len(types) - 1:
                continue
            if new_x < 0:
                continue
            if new_x > len(types[0]) - 1:
                continue
            if types[new_y][new_x] == ["neither", "torch", "climbing gear"].index(curr_item):
                continue

            heapq.heappush(queue, (time_ + 1, new_y, new_x, curr_item))


def main():
    depth = 11739
    target = [11, 718]

    geo_indices = [[0]*(3*target[0]) for i in range(3*target[1])]
    types = [[0]*(3*target[0]) for i in range(3*target[1])]

    for i in range(3*target[1]):
        for j in range(3*target[0]):
            if i == 0:
                geo_indices[i][j] = j*16807 % 20183
            elif j == 0:
                geo_indices[i][j] = i*48271 % 20183
            elif [i, j] == target:
                geo_indices[i][j] = 0
            else:
                geo_indices[i][j] = (geo_indices[i - 1][j] + depth)*(geo_indices[i][j - 1] + depth) % 20183

    for i in range(3*target[1]):
        for j in range(3*target[0]):
            types[i][j] = ((geo_indices[i][j] + depth) % 20183) % 3

    print(time(types, (target[1], target[0], "torch")))


if __name__ == "__main__":
    main()
