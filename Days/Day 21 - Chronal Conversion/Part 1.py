def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]

    instructions = []
    for line in f:
        instruction = line.split(" ")
        instruction[1:] = [int(i) for i in instruction[1:]]
        instructions.append(instruction)

    reg_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

    while reg_dict[2] < len(instructions):
        if reg_dict[2] == 28:
            break

        instruction = instructions[reg_dict[2]]

        if instruction[0] == "addr":
            reg_dict[instruction[3]] = reg_dict[instruction[1]] + reg_dict[instruction[2]]
        if instruction[0] == "addi":
            reg_dict[instruction[3]] = reg_dict[instruction[1]] + instruction[2]
        if instruction[0] == "mulr":
            reg_dict[instruction[3]] = reg_dict[instruction[1]]*reg_dict[instruction[2]]
        if instruction[0] == "muli":
            reg_dict[instruction[3]] = reg_dict[instruction[1]]*instruction[2]
        if instruction[0] == "banr":
            reg_dict[instruction[3]] = reg_dict[instruction[1]] & reg_dict[instruction[2]]
        if instruction[0] == "bani":
            reg_dict[instruction[3]] = reg_dict[instruction[1]] & instruction[2]
        if instruction[0] == "borr":
            reg_dict[instruction[3]] = reg_dict[instruction[1]] | reg_dict[instruction[2]]
        if instruction[0] == "bori":
            reg_dict[instruction[3]] = reg_dict[instruction[1]] | instruction[2]
        if instruction[0] == "setr":
            reg_dict[instruction[3]] = reg_dict[instruction[1]]
        if instruction[0] == "seti":
            reg_dict[instruction[3]] = instruction[1]

        if instruction[0] == "gtrr":
            if reg_dict[instruction[1]] > reg_dict[instruction[2]]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if instruction[0] == "gtir":
            if instruction[1] > reg_dict[instruction[2]]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if instruction[0] == "gtri":
            if reg_dict[instruction[1]] > instruction[2]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if instruction[0] == "eqrr":
            if reg_dict[instruction[1]] == reg_dict[instruction[2]]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if instruction[0] == "eqir":
            if instruction[1] == reg_dict[instruction[2]]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0
        if instruction[0] == "eqri":
            if reg_dict[instruction[1]] == instruction[2]:
                reg_dict[instruction[3]] = 1
            else:
                reg_dict[instruction[3]] = 0

        reg_dict[2] += 1

    print(reg_dict[3])


if __name__ == "__main__":
    main()
