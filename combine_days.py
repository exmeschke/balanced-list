# COMBINES FILES ACROSS DAYS

import csv
import os
import numpy

def repeat_name(final_list, name, start_index):
	repeat = 0
	l = 0
	for row in final_list:
		if (l > start_index):
			if (name == row[0]):
				repeat = 1
		l = l+1

	if (repeat == 1):
		return 1
	else: 
		return 0

def is_num(col):
	try: 
		float(col)
		return 1
	except ValueError:
		return 0

# combine across days
final_list = [["" for x in range(0,7)] for y in range(0,9450)]
directory = './data'
for root, dirs, files in os.walk(directory):
	# only look in current directory
	if (root is './data'):
		day = 1
		# loop through these files
		for fs in files:
			# only check files that end with .csv and are not already compiled
			if ('.csv' in fs) and ('googles' in fs):
				fs = 'data/'+fs
				# open the file
				with open(fs, 'rU') as csvin:
					reader = csv.reader(csvin)
					l = 0
					# if the first day, save name, imdb, googles mean
					if (day == 1):
						for row in reader:
							# clean up name
							name = row[0]
							if (name[0] is ' '):
								name = name[1:]
							final_list[l][0] = name
							final_list[l][1] = row[1]
							final_list[l][2] = row[2]
							l = l+1
						day = day+1
					# if not the first day, only save googles mean
					else:
						for row in reader:
							final_list[l][day+1] = row[2]
							l = l+1
						day = day+1

# output to file
with open('all_data.csv', 'wb') as csvout:
	writer = csv.writer(csvout)
	start = 0
	for f in final_list:
		if (repeat_name(final_list, f[0], start) is 0):
			days = []
			d = 0
			for col in f:
				if (is_num(col) and d > 1):
					days.append(float(col))
				d = d+1
			mean = numpy.mean(days)
			med = numpy.median(days)
			std = numpy.std(days)

			writer.writerow([f,f[0],mean,med,std])
		start = start+1

	