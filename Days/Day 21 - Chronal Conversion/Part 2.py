def main():
    reg_dict = {0: 0, 1: 0, 2: 6, 3: 0, 4: 0, 5: 0}
    pointer = 6
    seen = []

    while True:
        if pointer == 28:
            if reg_dict[3] in seen:
                print(seen[-1])
                break
            else:
                seen.append(reg_dict[3])
                pointer = 6

        elif pointer == 6:
            reg_dict[4] = reg_dict[3] | 65536
            reg_dict[3] = 2176960
            pointer = 8

        elif pointer == 8:
            reg_dict[1] = reg_dict[4] % 256
            reg_dict[3] = (((reg_dict[3] + reg_dict[1]) % 16777216)*65899) % 16777216

            if 256 > reg_dict[4]:
                pointer = 28
            else:
                pointer = 17

        elif pointer == 17:
            reg_dict[1] = 0
            pointer = 18

        else:  # pointer == 18
            reg_dict[5] = (1 + reg_dict[1])*256

            if reg_dict[5] > reg_dict[4]:
                reg_dict[4] = reg_dict[1]
                pointer = 8
            else:
                reg_dict[1] += 1


if __name__ == "__main__":
    main()
