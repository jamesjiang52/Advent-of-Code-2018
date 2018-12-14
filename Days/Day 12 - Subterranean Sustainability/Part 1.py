def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    initial = "##.#...#.#.#....###.#.#....##.#...##.##.###..#.##.###..####.#..##..#.##..#.......####.#.#..#....##.#"
    buffer = "."*150
    initial = buffer + initial + buffer

    prev = []
    next_ = []
    for line in f:
        comps = line.split(" ")
        prev.append(comps[0])
        next_.append(comps[2])

    for i in range(101):
        new = ".."
        for j in range(2, len(initial) - 2):
            new += next_[prev.index(initial[j - 2:j + 3])]

        new += ".."
        initial = new

    total = 0
    for i in range(len(initial)):
        if initial[i] == "#":
            total += i - len(buffer)

    print(total)


if __name__ == "__main__":
    main()
