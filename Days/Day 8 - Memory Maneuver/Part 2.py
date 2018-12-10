def value(data):
    num_children = data.pop(0)
    num_metadata = data.pop(0)

    values = [value(data) for i in range(num_children)]
    metadata = [data.pop(0) for i in range(num_metadata)]

    if num_children == 0:
        return sum(metadata)
    else:
        sum_ = 0
        for i in metadata:
            if i >= 1 and i <= num_children:
                sum_ += values[i - 1]
        return sum_


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    data = [int(i) for i in f[0].split(" ")]
    print(value(data))


if __name__ == "__main__":
    main()
