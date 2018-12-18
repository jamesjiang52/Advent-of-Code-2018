def main():
    f = [line.rstrip("\n") for line in open("Data_P1.txt")]

    instructions = []
    before = []
    after = []

    for i in range(0, len(f), 4):
        instructions.append([int(j) for j in f[i + 1].split(" ")])
        before_comps = f[i].split(" ")
        after_comps = f[i + 2].split(" ")
        del after_comps[1]
        before.append([int(before_comps[1][1:2])] + [int(comp[0:1]) for comp in before_comps[2:]])
        after.append([int(after_comps[1][1:2])] + [int(comp[0:1]) for comp in after_comps[2:]])

    total = 0

    for i in range(len(instructions)):
        count = 0
        if after[i][instructions[i][3]] == before[i][instructions[i][1]] + before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] == before[i][instructions[i][1]] + instructions[i][2]:
            count += 1
        if after[i][instructions[i][3]] == before[i][instructions[i][1]]*before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] == before[i][instructions[i][1]]*instructions[i][2]:
            count += 1
        if after[i][instructions[i][3]] == before[i][instructions[i][1]] & before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] == before[i][instructions[i][1]] & instructions[i][2]:
            count += 1
        if after[i][instructions[i][3]] == before[i][instructions[i][1]] | before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] == before[i][instructions[i][1]] | instructions[i][2]:
            count += 1
        if after[i][instructions[i][3]] == before[i][instructions[i][1]]:
            count += 1
        if after[i][instructions[i][3]] == instructions[i][1]:
            count += 1

        if after[i][instructions[i][3]] == 1 and before[i][instructions[i][1]] > before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] == 1 and instructions[i][1] > before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] == 1 and before[i][instructions[i][1]] > instructions[i][2]:
            count += 1
        if after[i][instructions[i][3]] == 1 and before[i][instructions[i][1]] == before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] == 1 and instructions[i][1] == before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] == 1 and before[i][instructions[i][1]] == instructions[i][2]:
            count += 1

        if after[i][instructions[i][3]] != 1 and before[i][instructions[i][1]] <= before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] != 1 and instructions[i][1] <= before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] != 1 and before[i][instructions[i][1]] <= instructions[i][2]:
            count += 1
        if after[i][instructions[i][3]] != 1 and before[i][instructions[i][1]] != before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] != 1 and instructions[i][1] != before[i][instructions[i][2]]:
            count += 1
        if after[i][instructions[i][3]] != 1 and before[i][instructions[i][1]] != instructions[i][2]:
            count += 1

        if count >= 3:
            total += 1

    print(total)


if __name__ == "__main__":
    main()
