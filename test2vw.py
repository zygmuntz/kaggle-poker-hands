#!/usr/bin/env python

"transform test.csv to VW format"

import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

i_f = open( input_file )
o_f = open( output_file, 'wb' )

writer = csv.writer( o_f, delimiter = " " )
reader = csv.reader( i_f )
reader.next()

for line in reader:
	line.pop( 0 )
	new_line = []
	new_line.append( "1" )	# dummy test label
	new_line.append( '|x' )
	for i in range( 5 ):
		new_line.append( "{}_{}".format( line[i*2], line[i*2+1] ))
	writer.writerow( new_line )
	