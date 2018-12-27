def choose_target(group, immune_system, infection, targeted):
    damage = group[4]
    damage_type = group[5]
    num_units = group[0]
    max_damage = 0
    max_damage_unit = None

    if group[6] in [i[6] for i in immune_system]:
        for i in infection:
            weak = i[2]
            immunity = i[3]
            if i[6] in targeted:
                continue
            if damage_type in immunity:
                continue
            elif damage_type in weak:
                damage_multiplier = 2
            else:
                damage_multiplier = 1
            if damage_multiplier*damage*num_units > max_damage:
                max_damage = damage_multiplier*damage*num_units
                max_damage_unit = i
            elif damage_multiplier*damage*num_units == max_damage:
                if i[4]*i[0] > max_damage_unit[4]*max_damage_unit[0]:
                    max_damage_unit = i
                elif i[4]*i[0] == max_damage_unit[4]*max_damage_unit[0] and i[6] > max_damage_unit[6]:
                    max_damage_unit = i

    else:
        for i in immune_system:
            weak = i[2]
            immunity = i[3]
            if i[6] in targeted:
                continue
            if damage_type in immunity:
                continue
            elif damage_type in weak:
                damage_multiplier = 2
            else:
                damage_multiplier = 1
            if damage_multiplier*damage*num_units > max_damage:
                max_damage = damage_multiplier*damage*num_units
                max_damage_unit = i
            elif damage_multiplier*damage*num_units == max_damage:
                if i[4]*i[0] > max_damage_unit[4]*max_damage_unit[0]:
                    max_damage_unit = i
                elif i[4]*i[0] == max_damage_unit[4]*max_damage_unit[0] and i[6] > max_damage_unit[6]:
                    max_damage_unit = i

    return max_damage_unit


def attack(group, target_id, immune_system, infection):
    damage = group[4]
    damage_type = group[5]
    num_units = group[0]

    if group[6] in [i[6] for i in immune_system if i != "dead"]:
        ids = [i[6] if i != "dead" else None for i in infection]
        if target_id in ids:
            index_ = ids.index(target_id)
        else:
            return
        target = infection[index_]
        hp = target[1]
        weak = target[2]
        if damage_type in weak:
            damage_multiplier = 2
        else:
            damage_multiplier = 1
        effective_damage = damage*damage_multiplier*num_units
        effective_damage -= (effective_damage % hp)

        infection[index_][0] -= effective_damage//hp
        if infection[index_][0] <= 0:
            infection[index_] = "dead"

    else:
        ids = [i[6] if i != "dead" else None for i in immune_system]
        if target_id in ids:
            index_ = ids.index(target_id)
        else:
            return
        target = immune_system[index_]
        hp = target[1]
        weak = target[2]
        if damage_type in weak:
            damage_multiplier = 2
        else:
            damage_multiplier = 1
        effective_damage = damage*damage_multiplier*num_units
        effective_damage -= (effective_damage % hp)

        immune_system[index_][0] -= effective_damage//hp
        if immune_system[index_][0] <= 0:
            immune_system[index_] = "dead"



def main():
    immune_system = [
        [2743, 4149, tuple(), tuple(), 13, "radiation", 14],
        [8829, 7036, tuple(), tuple(), 7, "fire", 15],
        [1928, 10700, ("cold"), ("fire", "radiation", "slashing"), 50, "slashing", 3],
        [6051, 11416, tuple(), tuple(), 15, "bludgeoning", 20],
        [895, 10235, ("bludgeoning"), ("slashing"), 92, "bludgeoning", 10],
        [333, 1350, tuple(), tuple(), 36, "radiation", 12],
        [2138, 8834, ("bludgeoning"), tuple(), 35, "cold", 11],
        [4325, 1648, ("cold", "fire"), tuple(), 3, "bludgeoning", 8],
        [37, 4133, tuple(), ("radiation", "slashing"), 1055, "radiation", 1],
        [106, 3258, tuple(), ("slashing", "radiation"), 299, "cold", 13]
    ]

    infection = [
        [262, 8499, ("cold"), tuple(), 45, "cold", 6],
        [732, 47014, ("cold", "bludgeoning"), tuple(), 127, "bludgeoning", 17],
        [4765, 64575, tuple(), tuple(), 20, "radiation", 18],
        [3621, 19547, tuple(), ("radiation", "cold"), 9, "cold", 5],
        [5913, 42564, tuple(), ("radiation", "bludgeoning", "fire"), 14, "slashing", 9],
        [7301, 51320, ("radiation", "fire"), ("bludgeoning"), 11, "fire", 2],
        [3094, 23713, ("slashing", "fire"), tuple(), 14, "radiation", 19],
        [412, 36593, ("radiation", "bludgeoning"), tuple(), 177, "slashing", 16],
        [477, 35404, tuple(), tuple(), 146, "cold", 7],
        [332, 11780, ("fire"), tuple(), 70, "slashing", 4]
    ]

    all_ = immune_system + infection

    while True:
        all_.sort(key=lambda i: (i[4]*i[0], i[6]), reverse=True)

        target_dict = {}
        for group in all_:
            target = choose_target(group, immune_system, infection, target_dict.values())
            if target:
                target_dict[group[6]] = target[6]
            else:
                target_dict[group[6]] = None

        all_.sort(key=lambda i: i[6], reverse=True)

        for group in all_:
            if group == "dead":
                continue
            if target_dict[group[6]]:
                attack(group, target_dict[group[6]], immune_system, infection)

        immune_system = [i for i in immune_system if i != "dead"]
        infection = [i for i in infection if i != "dead"]

        if immune_system == []:
            print(sum([group[0] for group in infection]))
            break
        elif infection == []:
            print(sum([group[0] for group in immune_system]))
            break

        all_ = immune_system + infection


if __name__ == "__main__":
    main()
