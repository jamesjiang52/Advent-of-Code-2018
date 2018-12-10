from collections import deque


def main():
    num_players = 424
    num_marbles = 7148200
    scores = [0]*num_players
    marbles = deque([0])

    current_player = 0

    for current_marble in range(1, num_marbles + 1):
        if current_marble % 23 == 0:
            marbles.rotate(8)
            scores[current_player] += current_marble + marbles.pop()
            marbles.rotate(-2)
        else:
            marbles.append(current_marble)
            marbles.rotate(-1)

        current_marble += 1
        current_player = (current_player + 1) % num_players

    print(max(scores))


if __name__ == "__main__":
    main()
