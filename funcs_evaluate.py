# HELPER FUNCTIONS TO EVALUATE THE LIST OF NAMES

import csv
import numpy
from decimal import Decimal

# Return a column of the list
# @param	listt - list of data or csv file name
#			typ - column to read
# @return 	data = names, means, or bin numbers
def read_col(listt, typ):
	data = []
	# from a csv file
	if ('.csv' in listt):
		with open(listt) as csvin:
			reader = csv.reader(csvin)
			for row in reader:
				if (typ is 'name'):
					data.append(row[0])
				elif (typ is 'mean'):
					data.append(float(row[1]))
				elif (typ is 'bin'):
					data.append(int(row[2]))
	# from final_list
	else:
		for f in listt:
			if (typ is 'name'):
				data.append(f[0])
			elif (typ is 'mean'):
				data.append(float(f[1]))
			elif (typ is 'bin'):
				data.append(int(f[2]))
	return data

# Return stats for data rounded to 5th decimal place
# @param	data - list of floats
# @return 	stats = [mean, med, std]
def get_stats(data):
	mean = round(Decimal(numpy.mean(data)),5)
	med = round(Decimal(numpy.median(data)),5)
	std = round(Decimal(numpy.std(data)),5)
	stats = [mean, med, std]
	return stats



# Reads in the ordered list from file
# @param 	in_file - the file to read
# @return	googles = a list of names and data for each day
def read_googles(in_file):
	googles = []
	with open(in_file, 'rU') as csvin:
		reader = csv.reader(csvin)
		for row in reader:
			googles.append(row)
	return googles

# Return a column of the list
# @param	listt - list of data or csv file name
#			typ - column to read
# @return 	data = names, means, or bin numbers
def read_googles_col(googles, typ):
	data = []
	for g in googles:
		if (typ is 'name'):
			data.append(g[1])
		elif (typ is 'mean'):
			data.append(float(g[2]))
		elif (typ is 'med'):
			data.append(float(g[3]))
	return data

# Gets stats [mean, med, stdev] for a bin
# @param	first - index to start
#			last - index to stop
#			googles - list of data
# @return	stats = [mean, med, std]
def bin_stats(first, last, googles):
	mean = []
	med = []
	std = []
	c = 0
	for g in googles:
		if (c >= first) and (c <= last):
			mean.append(float(g[2]))
			med.append(float(g[3]))
			std.append(float(g[4]))
		c=c+1
	stats = get_stats(mean)
	return stats

# Print stats for googles list
# @param	in_file - file to read in 
#			num_bins - number of bins
def stats(in_file, num_bins, n_per_bin):
	# read in data from file
	googles = read_googles(in_file)
	data = read_googles_col(googles, 'mean')
	# indices
	start = 0
	end = n_per_bin

	# bin stats
	for b in range(0,num_bins):
		# print b, [start,end], bin_stats(start,end,googles)
		print b, bin_stats(start,end,googles)
		start = start+n_per_bin+1
		end = start+n_per_bin
	# overall stats
	stats = get_stats(data)
	return stats



# Get stats for names in a specific bin of the list
# @param	final_list - list of data
#			bin_num	- [0 to 9]
#			n_test - number of trials of each bin number
# @return	bstats = [mean, median, std]
def list_bin_stats(final_list, bin_num, n_test):
	vals = [0 for x in range(0,n_test)]
	c = 0
	for f in final_list:
		if (int(f[2]) == bin_num):
			vals[c] = float(f[1])
			c = c+1
	bstats = get_stats(vals)
	return bstats

# Prints bin stats for list and returns overall stats
# @param	final_list - list of data
#			n_test - number of trials of each bin number
# @return 	stats = [mean, median, std]
def list_stats(final_list, n_test):
	# read in data
	names = read_col(final_list, 'name')
	data = read_col(final_list, 'mean')
	bins = read_col(final_list, 'bin')
	if ('.csv' in final_list):
		final_list = []
		for i in range(0,len(names)):
			row = [names[i], data[i], bins[i]]
			final_list.append(row)
			
	# bin stats
	for b in range(0,9):
		print b, list_bin_stats(final_list, b, n_test)
	# overall stats
	stats = get_stats(data)
	return stats



