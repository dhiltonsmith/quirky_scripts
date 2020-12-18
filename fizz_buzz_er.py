#!/usr/bin/env python3

import sys
import math

fizz_buzz_er_dict = [
	{
		'Divisor' : 3,
		'Print'   : "fizz"
	},
	{
		'Divisor' : 5,
		'Print'   : "buzz"
	},
        {
                'Divisor' : 7,
                'Print'   : "er"
        }
]

def fizz_buzz_er(number_to_check):
	for number in range(1, number_to_check+1):
		print_string = ""
		for dict_object in fizz_buzz_er_dict:
			if number % dict_object['Divisor'] == 0:
				print_string += dict_object['Print']
		if print_string == "":
			print_string = number
		print(print_string)


def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def main ():
	if len(sys.argv) < 2:
		sys.stderr.write('\nUsage: python ' + sys.argv[0] + ' [arg]\n')
		sys.exit(1)

	number_to_check = sys.argv[1]
	return_string = ""
	if RepresentsInt(number_to_check):
		number_to_check = int(number_to_check)
		if number_to_check > 1:
			fizz_buzz_er(number_to_check)
			return_string = "\n\nCompleted!"
		else:
			return_string = "Use a value greater than 1."
	else:
		return_string = "Use an integer value."

	print(return_string)

if __name__ == "__main__":
	main()
