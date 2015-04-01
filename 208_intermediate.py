import sys

grad_scale = ".,:;xX&@"

def init_matrix (width, height):
	return [['.' for i in range (width)] for j in range (height)]

def print_matrix (matrix):
	for i in range (len(matrix)):
		for j in range (len(matrix[i])):
			sys.stdout.write (matrix[i][j])
		print 

try:
	# BEGIN #
	ins = raw_input ()
	width = int (ins.split ()[0])
	height = int (ins.split ()[1])

	# Type of Gradient #

	ins = raw_input ()
	s = ins.split ()[0]
	if s == "radial":
		# parse x y r
		s = ''
	elif s == "linear":
		# parse x1 y1 x2 y2
		s = ''
	else:
		raise ("Invalid input.")
	matrix = init_matrix (width, height)

	print_matrix (matrix)

except:
	print "You fucked up."
	exit()