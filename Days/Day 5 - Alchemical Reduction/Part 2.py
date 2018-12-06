def length_reduced(string_list):
    continue_ = True

    while continue_:
        continue_ = False

        i = 0
        while i < len(string_list) - 1:
            if string_list[i].islower():
                if string_list[i + 1] == string_list[i].upper():
                    del string_list[i:i + 2]
                    continue_ = True
                else:
                    i += 1
            else:
                if string_list[i + 1] == string_list[i].lower():
                    del string_list[i:i + 2]
                    continue_ = True
                else:
                    i += 1

    return len(string_list)


def main():
    string = list([line.rstrip("\n") for line in open("Data.txt")][0])

    min_length = len(string)

    for char in "abcdefghijklmnopqrstuvwxyz":
        lower = char
        upper = char.upper()

        string_cpy = "".join(string)
        string_cpy = string_cpy.replace(upper, "")
        string_cpy = string_cpy.replace(lower, "")

        min_length = min(min_length, length_reduced(list(string_cpy)))

    print(min_length)


if __name__ == "__main__":
    main()
