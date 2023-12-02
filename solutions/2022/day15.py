import re

from util import read_input_file


def manhattan_distance_area(sensor_x, sensor_y, manhattan_distance, points, target, beacons):
    # Calculate all points within manhattan distance of sensor
    if target in range(sensor_y - manhattan_distance, sensor_y + manhattan_distance + 1):
        steps = abs(abs(sensor_y - target) - manhattan_distance)
        for i in range(-steps, steps + 1):
            if (sensor_x + i, target) not in beacons:
                points[sensor_x + i] = '#'
    return points


def solve(part):
    lines = read_input_file('../../inputs/2022/day15.txt')
    p = re.compile(r'\d+')

    if part == 1:
        desired_y = 10
    points = {}
    sensors = []
    beacons = []

    if part == 2:
        for i in range(4000000):
            points[i] = []
    print(points)

    for line in lines:
        nums = p.findall(line)
        sensor_x, sensor_y = int(nums[0]), int(nums[1])
        beacon_x, beacon_y = int(nums[2]), int(nums[3])
        sensors.append((sensor_x, sensor_y))
        beacons.append((beacon_x, beacon_y))
        # Find manhattan distance between sensor and beacon
        delta_y = abs(beacon_y - sensor_y)
        manhattan_distance = abs(beacon_x - sensor_x) + delta_y

        if part == 1:
            points = manhattan_distance_area(sensor_x, sensor_y, manhattan_distance, points, desired_y, beacons)

    pass


if __name__ == '__main__':
    solve(2)
