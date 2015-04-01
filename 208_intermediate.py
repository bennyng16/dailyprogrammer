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
	ins = raw_input ("Enter a radial gradient: ")
	ins = raw_input ("Enter either 'radial x y r' | 'linear x1 y1 x2 y2':)
	s = ins.split ()[0]
	if s == "radial":
		# parse x y r
		x = ins.split ()[1]
		y = ins.split ()[2]
		r = ins.split ()[3]
		print "You selected Radial Gradient"


	elif s == "linear":
		# parse x1 y1 x2 y2
		x1 = ins.split ()[1]
		y1 = ins.split ()[2]
		x2 = ins.split ()[3]
		y2 = ins.split ()[4]
		print "You selected Linear Gradient"

	else:
		raise ("Invalid input.")
	matrix = init_matrix (width, height)

	matrix[0][0] = grad_scale[4]
	print_matrix (matrix)

except:
	print "You fucked up."
	exit()