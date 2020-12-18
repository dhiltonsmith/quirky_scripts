#!/usr/bin/env python3

import sys
import math

def PrimeNumberCheck(number_to_check):
	for i in range(2,number_to_check):
		# Checked every value up to the square root for divisiblity, exit loop.
		if i * i > number_to_check:
			return True
		# If no remainder, then it's not prime, because it is divisible by a non zero and non-self.
		if number_to_check  % i == 0:
			return False

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
			if PrimeNumberCheck(number_to_check):
				return_string = "Number is Prime"
			else:
				return_string = "Number is not Prime"
		else:
			return_string = "Use a value greater than 1."
	else:
		return_string = "Use an integer value."

	print(return_string)

if __name__ == "__main__":
	main()
