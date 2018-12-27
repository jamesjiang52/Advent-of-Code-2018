def main():
    depth = 11739
    target = [11, 718]

    geo_indices = [[0]*(target[0] + 1) for i in range(target[1] + 1)]

    for i in range(target[1] + 1):
        for j in range(target[0] + 1):
            if i == 0:
                geo_indices[i][j] = j*16807 % 20183
            elif j == 0:
                geo_indices[i][j] = i*48271 % 20183
            elif [i, j] == target:
                geo_indices[i][j] = 0
            else:
                geo_indices[i][j] = (geo_indices[i - 1][j] + depth)*(geo_indices[i][j - 1] + depth) % 20183

    risk = 0
    for i in range(target[1] + 1):
        for j in range(target[0] + 1):
            risk += ((geo_indices[i][j] + depth) % 20183) % 3

    print(risk)


if __name__ == "__main__":
    main()
