# READS IN DIRECTORIES AND COMBINES INTO ONE FILE

import csv
import os

# concatenate lists
final = [["" for x in range(0,3)] for y in range(0,9500)]
directory = './data'
# loop through directories
for dirs in os.walk(directory):
	if (dirs[0] is './data'):
		num_days = len(dirs[1])
	else:
		dirr = dirs[0]
		day = dirr[7:]
		out_file = 'data/googles_'+str(day)

		# open folder
		with open(out_file+'.csv', 'wb') as csvout:
			writer = csv.writer(csvout)

			# open file in folder
			do = 1
			for i in range(0,num_days):
				for filename in os.listdir(dirr):
					if ('.csv' in filename) and ('_'+str(do) in filename):
						# print filename
						with open(dirr+'/'+filename, 'rU') as csvin:
							reader = csv.reader(csvin)

							l = 0
							for row in reader:
								# print row 
								writer.writerow(row)
								l = l+1
							print filename, l

							csvin.close()
						do = do+1

			csvout.close()



