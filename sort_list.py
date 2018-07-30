# MERGE SORT IMPLEMENTATION TO SORT LIST FROM HIGHEST TO LOWEST 
# NUMBER OF GOOGLE SEARCH RESULTS

import csv

# Read in file
def read_file(in_file):
	unsorted_list = []
	with open('all_data.csv') as csvin:
		reader = csv.reader(csvin)
		for row in reader:
			unsorted_list.append(row)
	return unsorted_list

# Write to file
def write_file(out_file, listt):
	n = len(out_file)
	with open(out_file, 'wb') as csvout:
		writer = csv.writer(csvout)
		i = 0
		for i in range(0,n):
		    writer.writerow(listt[i])
		    i = i+1

def merge(left, right):
	res = []
	while (len(left) > 0) and (len(right) > 0):
		if (left[0] > right[0]):
			res.append(left[0])
			left.pop(0)
		else:
			res.append(right[0])
			right.pop(0)

	while (len(left) > 0):
		res.append(left[0])
		left.pop(0)
	while (len(right) > 0):
		res.append(right[0])
		right.pop(0)

	return res

def merge_sort(m):
	n = len(m)
	if (n <= 1):
		return m

	mid = n//2
	left = m[:mid]
	right = m[mid+1:]

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)


unsorted_list = read_file('all_data.csv')
merge_sort(unsorted_list)

write_file('all_data_ordered.csv', unsorted_lis)



