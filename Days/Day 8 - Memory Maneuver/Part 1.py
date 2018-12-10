def sum_metadata(data):
    num_children = data.pop(0)
    num_metadata = data.pop(0)
    return sum([sum_metadata(data) for i in range(num_children)]) + sum([data.pop(0) for i in range(num_metadata)])


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    data = [int(i) for i in f[0].split(" ")]
    print(sum_metadata(data))


if __name__ == "__main__":
    main()
