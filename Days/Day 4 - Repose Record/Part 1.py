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

    times_dict = {}
    minutes = [0]*60
    current_id = 0
    i = 0

    while i < len(times):
        if times[i][5][0] == "G":
            current_id = int(times[i][5].split(" ")[1][1:])
            i += 1
        else:
            start = times[i][4]
            end = times[i + 1][4]
            if current_id not in times_dict:
                times_dict[current_id] = end - start
            else:
                times_dict[current_id] += end - start
            i += 2

    max_guard = max(times_dict, key=times_dict.get)

    i = 0
    found = False

    while i < len(times):
        if times[i][5][0] == "G":
            if int(times[i][5].split(" ")[1][1:]) != max_guard:
                i += 1
                found = False
            else:
                i += 1
                found = True
        else:
            if not found:
                i += 1
            else:
                start = times[i][4]
                end = times[i + 1][4]

                for j in range(start, end):
                    minutes[j] += 1

                i += 2

    print(max_guard*minutes.index(max(minutes)))


if __name__ == "__main__":
    main()
