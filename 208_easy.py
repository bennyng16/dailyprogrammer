# http://www.reddit.com/r/dailyprogrammer/comments/30ubcl/20150330_challenge_208_easy_culling_numbers/

import sys

def print_uniques (dict):
	s = ""
	for i in dict:
		s += str(i) + ' '
	print "Output:", s	

def get_input (dict):
	s = raw_input ("Input: ")
	ints = [int(s) for s in s.split()]
	return ints

def parse_ints (dict, ints):
	for i in ints:
		if dict.has_key(i) != True:
			dict[i] = 1


dict = {}

parse_ints (dict, get_input (dict))
print_uniques (dict)