"""
Main code from https://github.com/aaltoimaginglanguage/study_template
"""
import subprocess
import sys
import timeit
import numpy as np


def call(script, *params):
    """Call a script and exit if the script failed."""
    # print('\n---- Running %s %s ----\n' % (script, ' '.join(params)))
    return_code = subprocess.call(['python', script] + list(params))
    if return_code != 0:
        # Something went wrong when executing the script. Drop everything and
        # exit the master script.
        sys.exit(return_code)


iter_count = 100

func_array = np.zeros(iter_count)
script_array = np.zeros(iter_count)

for i in range(iter_count):
    start_time = timeit.default_timer()
    call('primes_func.py')
    func_array[i] = timeit.default_timer() - start_time

for i in range(iter_count):
    start_time = timeit.default_timer()
    call('primes_script.py')
    script_array[i] = timeit.default_timer() - start_time

func_avg = np.average(func_array)
script_avg = np.average(script_array)

print("Function call avg: ", func_avg)
print("Script call avg: ", script_avg)
print("func avg / script avg = ", func_avg / script_avg)
