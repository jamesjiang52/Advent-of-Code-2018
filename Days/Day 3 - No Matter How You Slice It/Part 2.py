def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    comps = [string.split(" ") for string in f]

    left = [int(comp[2].split(",")[0]) for comp in comps]
    right = [int(comp[2].split(",")[1][:-1]) for comp in comps]
    width = [int(comp[3].split("x")[0]) for comp in comps]
    height = [int(comp[3].split("x")[1]) for comp in comps]

    all_ = 1000000*[0]

    for i in range(len(f)):
        x_start = left[i]
        y_start = right[i]

        for j in range(x_start, x_start + width[i]):
            for k in range(y_start, y_start + height[i]):
                if all_[1000*j + k] == 1:
                    all_[1000*j + k] = 2
                else:
                    all_[1000*j + k] = 1

    for i in range(len(f)):
        it = 1

        x_start = left[i]
        y_start = right[i]

        for j in range(x_start, x_start + width[i]):
            for k in range(y_start, y_start + height[i]):
                if all_[1000*j + k] == 2:
                    it = 0
                    break

        if it == 1:
            print(i + 1)
            return


if __name__ == "__main__":
    main()
