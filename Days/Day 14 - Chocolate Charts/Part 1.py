def main():
    num_recipes = 939601

    recipes = [3, 7]
    first_index = 0
    second_index = 1

    while len(recipes) < num_recipes + 10:
        first_score = recipes[first_index]
        second_score = recipes[second_index]
        new = first_score + second_score

        if new < 10:
            recipes.append(new)
        else:
            recipes.extend([new//10, new % 10])

        first_index = (first_index + recipes[first_index] + 1) % len(recipes)
        second_index = (second_index + recipes[second_index] + 1) % len(recipes)

    print("".join([str(i) for i in recipes[num_recipes:num_recipes + 10]]))


if __name__ == "__main__":
    main()
