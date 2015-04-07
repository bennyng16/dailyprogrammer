import sys

# April 6, 2015
# /r/dailyprogrammer 209 Easy. 
# This is the quick implementation of a /r/thebutton sim.
# Possible additional features is a help option for additional information
# and possibly a title/display at the start of the program with 
# additional information.

class User:
	def __init__ (self, name, timestamp):
		self.name = name
		self.timestamp = timestamp

	def print_user (self):
		print self.name, self.timestamp

# Main

user_objects = []
output = []

count = int(raw_input ("Enter number of users: "))
clock_remaining = 60.0
check_point = 0.0

for i in range (0, count):
	ins = raw_input ("Enter user " + str(i) + ": ")
	user_objects.append (User (ins.split()[0], float(ins. split()[1])))

user_objects = sorted (user_objects, key=lambda user: user.timestamp)

for user in user_objects:
	diff = user.timestamp - check_point
	output.append (User (user.name, int (clock_remaining - diff)))
	check_point = user.timestamp

for user in output:
	user.print_user ()