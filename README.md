# Balanced List

Includes the number of Google results for top 10,000 celebrities on IMDb and top 1,000 Billboard artists. Contains code to parse data collected and combine into a balanced list of stimuli. 

## Procedure

1. concatenate_lists.py
Reads in all directories and combines the individual files into one file for each day. 

2. combine_days.py
Reads in files and combines across days so each row includes the celebrity name, mean # of results, median # of results, and stdeviation of results.

3. sort_list.py
Sorts list in order from largest to smallest mean number of google results.

4. create_list.py
Creates sampled, balanced list of names, means, and bin number.

5. analyze_list.py
Compares means of the sampled list and full list to show the sampled list is an appropriate representation of the population. 


funcs_evaluate.py
Includes helper functions that read, parse, and analyze compiled data. 