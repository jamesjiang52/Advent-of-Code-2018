def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    seen = [0]
    current = 0
    while True:
        for i in f:
            current += int(i)
            if current in seen:
                print(current)
                return
            else:
                seen.append(current)


if __name__ == "__main__":
    main()
