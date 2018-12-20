import math


def main():
    num = 10551298

    sum_ = 0
    for i in range(1, round(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            if i**2 == num:
                sum_ += 1
            else:
                sum_ += i + num//i

    print(sum_)


if __name__ == "__main__":
    main()
