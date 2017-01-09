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
        for i, line in enumerate(lines[:-1]):
            data[i] = float(line.split()[0])
    data /= 1000
    return tstop, data


def readdata_ln(file):
    with open(file, "r") as f:
        interval = float(f.readline().split()[-1])
        delay = float(f.readline().split()[-1])
        num_data = int(f.readline().split()[-1])
        tstop = float(f.readline().split()[-1])/1000

        comps = map(int, f.readline().split()[-4:])

        row, column = map(int, f.readline().split())
        lines = f.readlines()

        data = np.ndarray([column, row])
        print file
        for i in xrange(row):
            # print map(float, lines[i].split())
            data[:, i] = map(float, lines[i].split())
    data /= 1000
    return tstop, comps, data


def index(x):
    return math.floor(x/bin)


def draw_PSTH_rn_pn():
    PSTH = np.zeros([math.ceil(tstop/bin)])

    time = np.arange(math.ceil(tstop/bin))*bin
    for var in data:
        PSTH[index(var)] += 1
        # print index(var)
    # print PSTH[-10:]
    # print data[-10:]
    plt.plot(time, PSTH, "-", label=str(dose))
    plt.title("{2}: {0} ng, {1} ms".format(dose, duration*1000, cell_gid))
    plt.xlabel("time")
    plt.ylabel("PSTH")
    plt.xlim(0, round(time[-1]))
    plt.ylim(0,30)
    plt.legend()

    target_file = "{0}_PSTH.png".format(cell_gid)
    print input_dir+target_file
    plt.savefig(input_dir+target_file)
    plt.close()


def draw_PSTH_ln():
    PSTH = np.zeros([4, math.ceil(tstop/bin)])

    time = np.arange(math.ceil(tstop/bin))*bin
    for i in xrange(4):
        for var in data[i]:
            # print var, index(var)
            if var != 0:
                PSTH[i, index(var)] += 1
        # print index(var)
    # print PSTH[-10:]
    # print data[-10:]
    plt.plot(time, PSTH[0], "-", color="green", label=comps[0])
    plt.plot(time, PSTH[1], "-", color="blue", label=comps[1])
    plt.plot(time, PSTH[2], "-", color="red", label=comps[2])
    plt.plot(time, PSTH[3], "-", color="brown", label=comps[3])

    # plt.plot(time, PSTH[0], "-", label=str(dose))
    plt.title("{2}: {0} ng, {1} ms".format(dose, duration*1000, cell_gid))
    plt.xlabel("time")
    plt.ylabel("PSTH")
    plt.legend()
    # plt.xlim(0,2)
    plt.xlim(0, round(time[-1]))
    plt.ylim(0,50)
    plt.rcParams["font.size"] = 15


    target_file = "{0}_PSTH.png".format(cell_gid)
    print input_dir+target_file
    plt.savefig(input_dir+target_file)
    plt.close()




if __name__ == "__main__":
    input_dir = sys.argv[1]
    files = glob.glob("{0}*Spike.dat".format(input_dir))
    print "{0} files was imported.".format(len(files))

    duration = 1. #temporary
    bin = 0.1
    dose = 3000

    for file in files:
        cell_gid = file.split("/")[-1][:6]
        if cell_gid[0] == "3":
            tstop, comps, data = readdata_ln(file)
            draw_PSTH_ln()
            # print "a"
        else:
            tstop, data = readdata_rn_pn(file)
            draw_PSTH_rn_pn()
