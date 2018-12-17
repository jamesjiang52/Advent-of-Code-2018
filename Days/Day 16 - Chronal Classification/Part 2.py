def main():
    f = [line.rstrip("\n") for line in open("Data_P1.txt")]
    instructions_ = [[int(i) for i in line.rstrip("\n").split(" ")] for line in open("Data_P2.txt")]

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

    op_codes = [list(range(16)) for i in range(16)]

    for j in range(16):
        for i in range(len(instructions)):
            if instructions[i][0] != j:
                continue

            if after[i][instructions[i][3]] != before[i][instructions[i][1]] + before[i][instructions[i][2]]:
                if j in op_codes[0]:
                    op_codes[0].remove(j)

            if after[i][instructions[i][3]] != before[i][instructions[i][1]] + instructions[i][2]:
                if j in op_codes[1]:
                    op_codes[1].remove(j)

            if after[i][instructions[i][3]] != before[i][instructions[i][1]]*before[i][instructions[i][2]]:
                if j in op_codes[2]:
                    op_codes[2].remove(j)

            if after[i][instructions[i][3]] != before[i][instructions[i][1]]*instructions[i][2]:
                if j in op_codes[3]:
                    op_codes[3].remove(j)

            if after[i][instructions[i][3]] != before[i][instructions[i][1]] & before[i][instructions[i][2]]:
                if j in op_codes[4]:
                    op_codes[4].remove(j)

            if after[i][instructions[i][3]] != before[i][instructions[i][1]] & instructions[i][2]:
                if j in op_codes[5]:
                    op_codes[5].remove(j)

            if after[i][instructions[i][3]] != before[i][instructions[i][1]] | before[i][instructions[i][2]]:
                if j in op_codes[6]:
                    op_codes[6].remove(j)

            if after[i][instructions[i][3]] != before[i][instructions[i][1]] | instructions[i][2]:
                if j in op_codes[7]:
                    op_codes[7].remove(j)

            if after[i][instructions[i][3]] != before[i][instructions[i][1]]:
                if j in op_codes[8]:
                    op_codes[8].remove(j)

            if after[i][instructions[i][3]] != instructions[i][1]:
                if j in op_codes[9]:
                    op_codes[9].remove(j)


            if after[i][instructions[i][3]] != 1 and before[i][instructions[i][1]] > before[i][instructions[i][2]]:
                if j in op_codes[10]:
                    op_codes[10].remove(j)

            if after[i][instructions[i][3]] != 1 and instructions[i][1] > before[i][instructions[i][2]]:
                if j in op_codes[11]:
                    op_codes[11].remove(j)

            if after[i][instructions[i][3]] != 1 and before[i][instructions[i][1]] > instructions[i][2]:
                if j in op_codes[12]:
                    op_codes[12].remove(j)

            if after[i][instructions[i][3]] != 1 and before[i][instructions[i][1]] == before[i][instructions[i][2]]:
                if j in op_codes[13]:
                    op_codes[13].remove(j)

            if after[i][instructions[i][3]] != 1 and instructions[i][1] == before[i][instructions[i][2]]:
                if j in op_codes[14]:
                    op_codes[14].remove(j)

            if after[i][instructions[i][3]] != 1 and before[i][instructions[i][1]] == instructions[i][2]:
                if j in op_codes[15]:
                    op_codes[15].remove(j)


            if after[i][instructions[i][3]] == 1 and before[i][instructions[i][1]] <= before[i][instructions[i][2]]:
                if j in op_codes[10]:
                    op_codes[10].remove(j)

            if after[i][instructions[i][3]] == 1 and instructions[i][1] <= before[i][instructions[i][2]]:
                if j in op_codes[11]:
                    op_codes[11].remove(j)

            if after[i][instructions[i][3]] == 1 and before[i][instructions[i][1]] <= instructions[i][2]:
                if j in op_codes[12]:
                    op_codes[12].remove(j)

            if after[i][instructions[i][3]] == 1 and before[i][instructions[i][1]] != before[i][instructions[i][2]]:
                if j in op_codes[13]:
                    op_codes[13].remove(j)

            if after[i][instructions[i][3]] == 1 and instructions[i][1] != before[i][instructions[i][2]]:
                if j in op_codes[14]:
                    op_codes[14].remove(j)

            if after[i][instructions[i][3]] == 1 and before[i][instructions[i][1]] != instructions[i][2]:
                if j in op_codes[15]:
                    op_codes[15].remove(j)

    op_codes_dict = {}

    while True:
        for i in range(16):
            if len(op_codes[i]) == 1 and i not in op_codes_dict:
                taken = op_codes[i][0]
                op_codes_dict[i] = taken
                for j in range(16):
                    if j == i:
                        continue
                    while taken in op_codes[j]:
                        op_codes[j].remove(taken)
        if all(len(possible) == 1 for possible in op_codes):
            break

    op_codes_dict = {value: key for key, value in op_codes_dict.items()}

    reg_dict = {0: 0, 1: 0, 2: 0, 3: 0}
    for instruction in instructions_:
        if op_codes_dict[instruction[0]] == 0:
            reg_dict[instruction[3]] = reg_dict[instruction[1]] + reg_dict[instruction[2]]
        if op_codes_dict[instruction[0]] == 1:
            reg_dict[instruction[3]] = reg_dict[instruction[1]] + instruction[2]
        if op_codes_dict[instruction[0]] == 2:
            reg_dict[instruction[3]] = reg_dict[instruction[1]]*reg_dict[instruction[2]]
        if op_codes_dict[instruction[0]] == 3:
            reg_dict[instruction[3]] = reg_dict[instruction[1]]*instruction[2]
        if op_codes_dict[instruction[0]] == 4:
            reg_dict[instruction[3]] = reg_dict[instruction[1]] & reg_dict[instruction[2]]
        if op_codes_dict[instruction[0]] == 5:
            reg_dict[instruction[3]] = reg_dict[instruction[1]] & instruction[2]
        if op_codes_dict[instruction[0]] == 6:
            reg_dict[instruction[3]] = reg_dict[instruction[1]] | reg_dict[instruction[2]]
        if op_codes_dict[instruction[0]] == 7:
            reg_dict[instruction[3]] = reg_dict[instruction[1]] | instruction[2]
        if op_codes_dict[instruction[0]] == 8:
            reg_dict[instruction[3]] = reg_dict[instruction[1]]
        if op_codes_dict[instruction[0]] == 9:
            reg_dict[instruction[3]] = instruction[1]

        if op_codes_dict[instruction[0]] == 10:
            if reg_dict[instruction[1]] > reg_dict[instruction[2]]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if op_codes_dict[instruction[0]] == 11:
            if instruction[1] > reg_dict[instruction[2]]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if op_codes_dict[instruction[0]] == 12:
            if reg_dict[instruction[1]] > instruction[2]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if op_codes_dict[instruction[0]] == 13:
            if reg_dict[instruction[1]] == reg_dict[instruction[2]]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if op_codes_dict[instruction[0]] == 14:
            if instruction[1] == reg_dict[instruction[2]]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if op_codes_dict[instruction[0]] == 15:
            if reg_dict[instruction[1]] == instruction[2]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0

    print(reg_dict[0])


if __name__ == "__main__":
    main()
