"""
usage
$ python drawPSTH.py target_dir

ex.
$ python drawPSTH.py 1234567
"""

import os
import sys
import math
import glob
import numpy as np

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pylab as plt


def readdata_rn_pn(file):
    with open(file, "r") as f:
        interval = float(f.readline().split()[-1])
        delay = float(f.readline().split()[-1])
        num_data = int(f.readline().split()[-1])
        tstop = float(f.readline().split()[-1])/1000

        lines = f.readlines()
        column = len(lines)-1
        row = 1
        data = np.ndarray([column])
        count_under = 0
        count_upper = 0
        for i, line in enumerate(lines[:-1]):
            data[i] = float(line.split()[0])
            if data[i] < 500:
                count_under += 1
            elif data[i] > 99000 and data[i] < 99500:
                count_upper += 1
    data /= 1000
    return count_under, count_upper


def index(x):
    return int(math.floor(x/bin))

def fild_all_files(directory):
    for root, dirs, files in os.walk(directory):
        yield root
        for file in files:
            yield os.path.join(root, file)


if __name__ == "__main__":
    # files = glob.glob("{0}*Spike.dat".format(input_dir))
    # print "{0} files was imported.".format(len(files))

    duration = 1. #temporary
    bin = 0.1
    dose = 3000

    # for file in files:
    for file in fild_all_files(sys.argv[1]):
        if os.path.isdir(file):
            input_dir = file + "/"
            continue
        if not 'dat' in file:
            continue
        cell_gid = file.split("/")[-1][:6]
        if cell_gid[0] == "2":
            print file
            count_under, count_upper = readdata_rn_pn(file)
            print (count_under, count_upper)

