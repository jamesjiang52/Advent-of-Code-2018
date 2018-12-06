def main():
    string = list([line.rstrip("\n") for line in open("Data.txt")][0])

    continue_ = True

    while continue_:
        continue_ = False

        i = 0
        while i < len(string) - 1:
            if string[i].islower():
                if string[i + 1] == string[i].upper():
                    del string[i:i + 2]
                    continue_ = True
                else:
                    i += 1
            else:
                if string[i + 1] == string[i].lower():
                    del string[i:i + 2]
                    continue_ = True
                else:
                    i += 1

    print(len(string))


if __name__ == "__main__":
    main()
