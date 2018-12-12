def power(x, y, serial_num):
    rack_id = x + 10
    power_ = rack_id*y
    power_ += serial_num
    power_ *= rack_id
    power_ = (power_//100) % 10
    return(power_ - 5)


def main():
    serial_num = 7403
    max_ = 0
    max_x = 0
    max_y = 0
    max_h = 0

    powers = [[0 for j in range(300)] for i in range(300)]
    for i in range(300):
        for j in range(300):
            powers[i][j] = power(j + 1, i + 1, serial_num)

    for h in range(1, 301):
        for i in range(301 - h):
            for j in range(301 - h):
                sum_ = 0
                for k in range(0, h):
                    for l in range(0, h):
                        sum_ += powers[i + k][j + l]

                if sum_ > max_:
                    max_ = sum_
                    max_x = j + 1
                    max_y = i + 1
                    max_h = h

        print(max_x, max_y, max_h)


if __name__ == "__main__":
    main()
