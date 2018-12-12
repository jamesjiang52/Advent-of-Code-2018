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

    powers = [[0 for j in range(300)] for i in range(300)]
    for i in range(300):
        for j in range(300):
            powers[i][j] = power(j + 1, i + 1, serial_num)

    for i in range(298):
        for j in range(298):
            sum_ = 0
            for k in range(0, 3):
                for l in range(0, 3):
                    sum_ += powers[i + k][j + l]

            if sum_ > max_:
                max_ = sum_
                max_x = j + 1
                max_y = i + 1

    print(max_x, max_y)


if __name__ == "__main__":
    main()
