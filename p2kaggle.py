#!/usr/bin/env python

"transform VW's predictions to kaggle submission format"

import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]

i_f = open( input_file )
o_f = open( output_file, 'wb' )

reader = csv.reader( i_f )
writer = csv.writer( o_f )
writer.writerow( [ 'id', 'hand' ] )

counter = 0
for line in reader:
	counter += 1
	p = int( float( line[0] )) - 1
	writer.writerow( [ counter, p ] )
	