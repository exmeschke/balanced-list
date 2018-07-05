from funcs_evaluate import stats
from funcs_evaluate import list_stats

# INPUTS
in_file = 'googles_all.csv'
list_file = 'hmf_list_v1.csv'
N = 9320
# number of bins
n_bins = 10
# number of trials per bin
n_per_bin = N/n_bins 
# number tested per bin
n_test = int(n_per_bin*(.10))


# print stats 
print stats(in_file, n_bins, n_per_bin)
# analyze list
print list_stats(list_file, n_test)