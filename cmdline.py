#!/usr/bin/python

import sys
import getopt

def main(argv):
	inputfile = ""
	outputfile = ""

	try:
		opts, args = getopt.getopt(argv, "hi:o:",["ifile=","ofile="])
	except getopt.GetoptError:
		print "Incorrect arguments. Type 'python cmdline.py -h' for help."
		sys.exit(2)
	
	for opt, arg in opts:
		if opt == '-h':
			print "cmdline.py -i <inputfile> -o <outputfile>"
			sys.exit()
		elif opt in ("-i", "--ifile"):
			inputfile = arg
		elif opt in ("-o", "--ofile"):
			outputfile = arg

	print "Input file is ", inputfile
	print "Output file is ", outputfile

if __name__ == "__main__" and len(sys.argv) > 1:
	main(sys.argv[1:])
else:
	print "Require arguments."
	sys.exit(2)