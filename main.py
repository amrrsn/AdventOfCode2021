def Day1():
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


def Day2():
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
    with open("./puzzle_inputs/Day3.txt") as input_file:
        pass


if __name__ == '__main__':
    print(f"Day1: {Day1()}")
    print(f"Day2: {Day2()}")
    print(f"Day3: {Day3()}")
