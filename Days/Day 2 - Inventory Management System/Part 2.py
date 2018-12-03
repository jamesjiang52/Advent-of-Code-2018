def differ(string_1, string_2):
    new_string = ""
    for i in range(len(string_1)):
        if string_1[i] == string_2[i]:
            new_string += string_1[i]

    return new_string


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]

    for i in range(len(f)):
        for j in range(i + 1, len(f)):
            if len(differ(f[i], f[j])) == len(f[i]) - 1:
                print(differ(f[i], f[j]))


if __name__ == "__main__":
    main()
