import csv

unsorted_list = [['' for x in range(0,5)] for y in range(0,9450)]
with open('all_data.csv') as csvin:
	reader = csv.reader(csvin)
	for row in reader:
		unsorted_list = row

for ul in unsorted_list:
	print ul