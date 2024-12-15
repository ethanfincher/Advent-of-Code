import re
import numpy as np
lines = open("2024/14/input.txt").read().strip().split("\n")


def calc_robot_positions(width, height, seconds):
    robot_positions = []
    for line in lines:
        numbers = [int(num) for num in re.findall(r"[-\d]+", line)]
        final_x = (numbers[0]+(numbers[2]*seconds)) % width
        final_y = (numbers[1]+(numbers[3]*seconds)) % height
        robot_positions.append((final_x, final_y))
    quad_1_robots = len([robot for robot in robot_positions if robot[0] < width // 2 and robot[1] < height // 2])
    quad_2_robots = len([robot for robot in robot_positions if robot[0] > width // 2 and robot[1] < height // 2])
    quad_3_robots = len([robot for robot in robot_positions if robot[0] < width // 2 and robot[1] > height // 2])
    quad_4_robots = len([robot for robot in robot_positions if robot[0] > width // 2 and robot[1] > height // 2])
    return quad_1_robots * quad_2_robots * quad_3_robots * quad_4_robots

# print(calc_robot_positions(101, 103, 100))

def find_christmas_tree(width, height, pictures, start, increment):
    for picture in range(1, pictures+1):
        robot_positions = []
        for line in lines:
            numbers = [int(num) for num in re.findall(r"[-\d]+", line)]
            final_x = (numbers[0]+(numbers[2]*(start+picture*increment))) % width
            final_y = (numbers[1]+(numbers[3]*(start+picture*increment))) % height
            robot_positions.append((final_x, final_y))
        robot_picture = np.full((height, width), ".")
        for robot in robot_positions:
            robot_picture[(robot[1], robot[0])] = "#"
        np.savetxt(f'pictures/output-{(start+picture*increment)}.txt', robot_picture, fmt='%s', delimiter='')

find_christmas_tree(101, 103, 1000, 128, 101)