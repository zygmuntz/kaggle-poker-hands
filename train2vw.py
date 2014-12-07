#!/usr/bin/env python

"transform train.csv to VW format"

import sys
import csv

label_index = 10

input_file = sys.argv[1]
output_file = sys.argv[2]

i_f = open( input_file )
o_f = open( output_file, 'wb' )

writer = csv.writer( o_f, delimiter = " " )
reader = csv.reader( i_f )
reader.next()

for line in reader:
	new_line = []
	new_line.append( str( int( line[label_index] ) + 1 ))
	new_line.append( '|x' )
	for i in range( 5 ):
		new_line.append( "{}_{}".format( line[i*2], line[i*2+1] ))
	writer.writerow( new_line )
	