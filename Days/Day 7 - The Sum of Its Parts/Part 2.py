def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    predecessors = []
    successors = []
    for line in f:
        comps = line.split(" ")
        predecessors.append(comps[1])
        successors.append(comps[-3])

    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    all_data = []
    done = []
    curr = [None, None, None, None, None]
    time_left = [0, 0, 0, 0, 0]

    for letter in letters:
        predecessors_curr = []
        for j in range(len(predecessors)):
            if successors[j] == letter:
                predecessors_curr.append(predecessors[j])
        all_data.append(predecessors_curr)

    time = 0
    while len(done) < 26:
        time += 1
        for i in range(5):
            if curr[i] is not None:
                time_left[i] -= 1
                if time_left[i] == 0:
                    done.append(curr[i])
                    for data in all_data:
                        if curr[i] in data:
                            data.remove(curr[i])
                    curr[i] = None

        for i in range(5):
            if curr[i] is not None:
                continue

            for j in range(len(all_data)):
                if len(all_data[j]) == 0:
                    curr[i] = letters[j]
                    time_left[i] = j + 61
                    all_data[letters.index(curr[i])] = ["visited"]
                    break

    print(time - 1)


if __name__ == "__main__":
    main()
