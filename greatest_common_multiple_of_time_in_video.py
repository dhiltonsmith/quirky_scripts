#!/usr/bin/env python3

import sys
import math

def video_time_calculation(video_time_array):
    video_time_int = 0

    multiplier = 1
    for i in reversed(video_time_array):
        integer = int(i)
        video_time_int += integer*multiplier
        multiplier *= 60

    return video_time_int

def divisible_by_calculation(integer):
    divisible_by=[]
    current_divisor=2

    integer_current = integer

    while integer_current >= current_divisor:
        if integer_current % current_divisor == 0:
            divisible_by.append(current_divisor)
            integer_current /= current_divisor
        else:
            current_divisor+=1

    return divisible_by

def closest_pair_calculation(combinations, divisible_by, total_number):
    closest_difference = total_number
    closest_pair = [1, total_number]
    attempt = 0

    while combinations >= attempt:
        current_attempt = attempt
        first_multiple = 1
        for idx, divisible in enumerate(reversed(divisible_by)):
            column = math.pow(2, (len(divisible_by)-idx)-1)
            if current_attempt >= column:
                first_multiple *= divisible
                current_attempt -= column

        second_multiple = total_number / first_multiple
        difference = math.fabs(first_multiple-second_multiple)

        if difference < closest_difference:
            closest_difference = difference
            closest_pair = [first_multiple, second_multiple]

        attempt += 1

    return closest_pair

def main ():
    if len(sys.argv) < 2:
        sys.stderr.write('\nUsage: python ' + sys.argv[0] + ' [arg]\n')
        sys.exit(1)

    video_time = sys.argv[1]
    video_time_split = str.split(video_time, ':')

    for item in video_time_split:
        if not item.isdigit():
            print("\nUsage: must provide colon <:> seperated integers")
            sys.exit(1)

    video_time_int = video_time_calculation(video_time_split)
    print("Total Video Time: " + str(video_time_int) + " Seconds")

    divisible_by=divisible_by_calculation(video_time_int)
    print("Divisible By: " + str(divisible_by))

    combinations = int(math.pow(2, len(divisible_by)))-1
    print("Combinations: " + str(combinations))

    closest_pair = closest_pair_calculation(combinations, divisible_by, video_time_int)
    print("Greatest Common Multiple: " + str(closest_pair))

if __name__ == "__main__":
    main()
