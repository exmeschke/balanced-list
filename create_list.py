from funcs_evaluate import read_googles
from funcs_evaluate import stats
from funcs_evaluate import list_stats
import random
import numpy
import csv

# INPUT
in_file = 'googles_all.csv'
out_file = 'hmf_list_v2.csv'
days = 4
N = 9320
# number of bins
n_bins = 10
# number of trials per bin
n_per_bin = N/n_bins - 1
# number tested per bin
n_test = int(n_per_bin*(.10))


# HELPER FUNCTIONS
# create random bins
def create_bin(first, last, n_per_bin, n_test, googles):
	options = [['' for x in range(0,2)] for y in range(first,last)]
	c = 0
	o = 0
	# select options from list
	for g in googles:
		if (c >= first) and (c < last):
			# print g
			options[o][0] = g[1]
			options[o][1] = g[2]
			o=o+1
		c = c+1

	# select random indices
	rands = [0 for x in range(0,n_test)]
	r = 0
	while (rands[-1] == 0):
		# random index
		rand = random.randint(1,n_per_bin-1)
		# check for a repeat
		repeat = 0
		for j in rands:
			if (rand == j):
				repeat = 1
		# if not a repeat, add index and move on
		if (repeat != 1):
			rands[r] = rand
			# print rands[r]
			r = r+1

	# select choices
	choices = [['' for x in range(0,3)] for y in range(0,n_test)]
	for i in range(0,n_test):
		choices[i][0] = rands[i]
		choices[i][1] = options[rands[i]][0]
		choices[i][2] = options[rands[i]][1]
	return choices

# combine bins
def combine_bins():
	st = 0
	fi = n_per_bin
	bins = [['' for x in range(0,1)] for y in range(0,n_bins)]
	for i in range(0,n_bins):
		bins[i] = create_bin(st, fi, n_per_bin, n_test, googles)
		st = st+n_per_bin+1
		fi = st+n_per_bin
	return bins

# random permutation list
def rand_perms(n_test):
	perm_list = []
	for i in range(0,n_test):
		plist = numpy.random.permutation(10)
		perm_list = numpy.concatenate((perm_list,plist))
	return perm_list

# create list
def create_list(n_bins, n_per_bin, n_test):
	bins = combine_bins()

	final_list = [['' for x in range(0,3)] for y in range(0,n_test*n_bins)]
	indices = [0 for x in range(0,10)]
	perm_list = rand_perms(n_test)
	i = 0
	for p in perm_list:
		ind = int(p)
		# relevant info
		curr_bin = bins[ind]
		curr_ind = indices[ind]

		# select celeb
		final_list[i][0] = curr_bin[curr_ind][1]
		final_list[i][1] = curr_bin[curr_ind][2]
		final_list[i][2] = ind

		# increase index
		indices[ind] = indices[ind]+1
		i = i+1
	return final_list

# write list
def write_list(out_file, final_list):
	with open(out_file, 'wb') as csvout:
		writer = csv.writer(csvout)

		for f in final_list:
			writer.writerow(f)


# print stats 
print stats(in_file, n_bins, n_per_bin)
# read in googles
googles = read_googles(in_file)
# create list
final_list = create_list(n_bins, n_per_bin, n_test)
# analyze list
print list_stats(final_list, n_test)
# write list
write_list(out_file, final_list)





