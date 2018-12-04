def mode(list_):
    return max(set(list_), key=list_.count)


def main():
    f = [line.rstrip("\n") for line in open("Data.txt")]
    comps = [string.split(" ") for string in f]
    times = []

    for info in comps:
        day = [int(i) for i in info[0][1:].split("-")]
        time = [int(i) for i in info[1][:-1].split(":")]
        info_string = [" ".join(info[2:])]
        times.append(day + time + info_string)

    times.sort()

    minutes = []
    for i in range(60):
        minutes.append([])

    current_id = 0
    i = 0

    while i < len(times):
        if times[i][5][0] == "G":
            current_id = int(times[i][5].split(" ")[1][1:])
            i += 1
        else:
            start = times[i][4]
            end = times[i + 1][4]

            for j in range(start, end):
                minutes[j].append(current_id)

            i += 2

    max_element = []
    max_size = 0
    max_index = 0

    for i in range(60):
        if len(minutes[i]) > max_size:
            max_element = minutes[i]
            max_size = len(minutes[i])
            max_index = i

    print(mode(max_element)*max_index)


if __name__ == "__main__":
    main()
