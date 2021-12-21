import numpy as np
import matplotlib.pyplot as plt


def remove_duplicates(input_list):
    return list(set([i for i in input_list]))


def Day1() -> int:
    with open("./puzzle_inputs/Day1.txt") as depth_measurements:
        depth_measurements = list(map(int, depth_measurements))

        num_increased = 0
        windows = []
        for depth1, depth2, depth3 in zip(depth_measurements, depth_measurements[1:], depth_measurements[2:]):
            windows.append(depth1 + depth2 + depth3)
        for prev_window, window in zip(windows, windows[1:]):
            if window > prev_window:
                num_increased += 1
    return num_increased


def Day2() -> int:
    sub_horizontal = 0
    sub_depth = 0
    sub_aim = 0

    with open("./puzzle_inputs/Day2.txt") as sub_commands:
        for command in sub_commands:
            instruction, value = command.split(" ")
            value = int(value)
            if instruction == "forward":
                sub_horizontal += value
                sub_depth += sub_aim * value
            elif instruction == "down":
                # sub_depth += value
                sub_aim += value
            elif instruction == "up":
                # sub_depth -= value
                sub_aim -= value
            else:
                print("What The Heck Did You Do???")

    return sub_depth * sub_horizontal


def Day3():
    gamma_rate = []
    epsilon_rate = []
    nums = []
    oxy_nums = []
    co2_nums = []
    with open("./puzzle_inputs/Day3.txt") as input_file:
        for line in input_file:
            tmp = [char for char in line.strip()]
            nums.append(tmp)
            oxy_nums.append(tmp)
            co2_nums.append(tmp)
    for i in range(12):
        ones = 0
        zeros = 0
        for num in nums:
            if num[i] == "0":
                zeros += 1
            else:
                ones += 1
        if ones > zeros:
            gamma_rate.append(1)
            epsilon_rate.append(0)
            for num in oxy_nums:
                if len(oxy_nums) == 1:
                    break
                if num[i] != "1":
                    oxy_nums.remove(num)
            for num in co2_nums:
                if len(co2_nums) == 1:
                    break
                if num[i] != "0":
                    co2_nums.remove(num)
        elif ones < zeros:
            gamma_rate.append(0)
            epsilon_rate.append(1)
            for num in oxy_nums:
                if len(oxy_nums) == 1:
                    break
                if num[i] != "0":
                    oxy_nums.remove(num)
            for num in co2_nums:
                if len(co2_nums) == 1:
                    break
                if num[i] != "1":
                    co2_nums.remove(num)
        else:
            for num in oxy_nums:
                if len(oxy_nums) == 1:
                    break
                if num[i] != "1":
                    oxy_nums.remove(num)
            for num in co2_nums:
                if len(co2_nums) == 1:
                    break
                if num[i] != "0":
                    co2_nums.remove(num)

    gamma_rate = "".join(map(str, gamma_rate))
    epsilon_rate = "".join(map(str, epsilon_rate))
    co2_rating = "".join(map(str, co2_nums[0]))
    oxy_rating = "".join(map(str, oxy_nums[0]))
    return int(gamma_rate, 2) * int(epsilon_rate, 2), int(co2_rating, 2) * int(oxy_rating, 2)


def Day13():
    coords = []
    new_coords = []
    with open("./puzzle_inputs/Day13.txt") as input_file:
        for line in input_file:
            if "," in line:
                tmp = line.strip().split(",")
                coords.append((int(tmp[0]), int(tmp[1])))
            if "fold" in line:
                tmp = line.strip().split(" ")
                fold = tmp[2].split("=")
                for i in range(len(coords)):
                    coord = coords[i]
                    if fold[0] == "x":
                        if coord[0] < int(fold[1]):
                            new_coords.append(coord)
                            continue
                        coord = (coord[0] - 2 * (coord[0] - int(fold[1])), coord[1])
                    elif fold[0] == "y":
                        if coord[1] < int(fold[1]):
                            new_coords.append(coord)
                            continue
                        coord = (coord[0], coord[1] - 2 * (coord[1] - int(fold[1])))
                    new_coords.append(coord)
                new_coords = remove_duplicates(new_coords)
                coords = new_coords
                new_coords = []
        coords = remove_duplicates(coords)
        plt.scatter(*zip(*coords))
        plt.axis((-5, 40, 15, -10))
        plt.show()
        return coords


if __name__ == '__main__':
    print(f"Day 1: {Day1()}")
    print(f"Day 2: {Day2()}")
    # print(f"Day 3: {Day3()}")
    print(f"Day 13: {Day13()}")
