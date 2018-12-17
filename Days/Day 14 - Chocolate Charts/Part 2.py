def main():
    num_recipes = 939601
    num_recipes_list = [int(i) for i in str(num_recipes)]

    recipes = [3, 7]
    first_index = 0
    second_index = 1

    while True:
        first_score = recipes[first_index]
        second_score = recipes[second_index]
        new = first_score + second_score

        if new < 10:
            recipes.append(new)
            if recipes[-7:-1] == num_recipes_list:
                print(len(recipes) - 7)
                break
        else:
            recipes.extend([new//10, new % 10])
            if recipes[-7:-1] == num_recipes_list:
                print(len(recipes) - 7)
                break
            if recipes[-8:-2] == num_recipes_list:
                print(len(recipes) - 8)
                break


        first_index = (first_index + recipes[first_index] + 1) % len(recipes)
        second_index = (second_index + recipes[second_index] + 1) % len(recipes)


if __name__ == "__main__":
    main()
