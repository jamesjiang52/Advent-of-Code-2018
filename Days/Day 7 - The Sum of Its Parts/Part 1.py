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

    for letter in letters:
        predecessors_curr = []
        for j in range(len(predecessors)):
            if successors[j] == letter:
                predecessors_curr.append(predecessors[j])
        all_data.append(predecessors_curr)

    while len(done) < 26:
        for i in range(len(all_data)):
            if len(all_data[i]) == 0:
                done.append(letters[i])
                for data in all_data:
                    if letters[i] in data:
                        data.remove(letters[i])
                all_data[i] = ["visited"]
                break

    print("".join(done))


if __name__ == "__main__":
    main()
