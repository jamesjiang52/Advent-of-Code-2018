def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    print(sum(map(int, f)))


if __name__ == "__main__":
    main()
