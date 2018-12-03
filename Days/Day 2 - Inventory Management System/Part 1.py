def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    two = 0
    three = 0

    seen_two = False
    seen_three = False

    for string in f:
        seen_two = False
        seen_three = False

        for letter in list("abcdefghijklmnopqrstuvwxyz"):
            if string.count(letter) == 2 and not seen_two:
                two += 1
                seen_two = True
            if string.count(letter) == 3 and not seen_three:
                three += 1
                seen_three = True

    print(two*three)


if __name__ == "__main__":
    main()