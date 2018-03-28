#! /usr/bin/python
# coding: UTF-8

"""
This program draws a graph of peak ISF and spike counts.
It can draw multi graph for multi compartment.

Usage:
$python spike_analyze.py filenames
    or
$python spike_analyze.py directory

行と列逆の方がわかりやすいけど dat の向き（縦方向）に揃えてる
"""

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import os.path
import csv
import matplotlib
from collections import deque
x = "$ cmpt: 30 50 60 80"

def readSpikeRecordFile(filename):
    global interval, delay, size, tstop, row, column, cmpt
    with open(filename,'r') as datafile:
        data = deque(datafile.readlines())
        interval = int(data.popleft().split(":")[1])
        delay = float(data.popleft().split(":")[1])
        size = int(data.popleft().split(":")[1])
        tstop = int(data.popleft().split(":")[1])
        if len(data[0].split()) > 0 and data[0].split()[0] == "$":
            cmpt = map(int, data.popleft().split(":")[1].split())
        else:
            cmpt = [""]
        row = size
        if len(data[0].split()) == 2:
            column = int(data.popleft().split()[1])
        else:
            column = 1
        spt = np.zeros([row, column]) #spike timing, spt[:, c]: c 番目の column の spike が入る

        print "Interval : %d, Delay : %f, number of data : %d, tstop : %d"%(interval, delay, size, tstop)

        for i in xrange(row):
            try :
                spt[i, :] = map(float, data[i].split())
            except ValueError:
                print "error!%s"%data[i]
                pass

        return spt


def reconstruct_data(spt): # devide by interval
    num = int(math.ceil(float(tstop)/float(interval)))
    pulses = [[[] for j in xrange(num)] for i in xrange(column)] # pulse[c][i]: c 番目の column の spike のうち i*interval <= t < (i+1)*interval を満たすもの

    for c in xrange(column):
        for t in spt[:,c]:
            if t != 0:
                pulses[c][int(t-delay)/interval].append(t)

    return pulses


def drawSpikeCounts(pulses, filename, show):
    fig = plt.figure()
    n_stim = len(pulses[0])
    stims = range(1, n_stim+1)
    counts = [[len(pulses[c][s]) for s in xrange(n_stim)] for c in xrange(column)]

    for c in xrange(column):
        plt.plot(stims,counts[c], label=str(cmpt[c]))


    plt.xlabel("stimulus pulse number", fontsize=15)
    plt.ylabel("Spike Counts[spikes]", fontsize=15)
    plt.legend()
    tmp = filename.rsplit('.',1)
    imgFilename = "%s_spikecounts.png"%tmp[0]
    plt.savefig(imgFilename)

    plt.close()

    # tmp = filename.rsplit('.',1)
    # csvfilename = "%s_spikecounts.csv"%tmp[0]
    # with open(csvfilename,'wb') as f:
    #     writer = csv.writer(f)
    #     for i in range(n_stim):
    #         writer.writerow([stims[i], counts[i]])


def drawPeakISF(pulses, filename, show):
    fig = plt.figure()
    n_stim = len(pulses[0])
    stims = range(1, n_stim+1)

    peakISF = np.zeros([n_stim, column])

    for c in xrange(column): # column
        for r in xrange(n_stim): # row
            var = pulses[c][r]
            if len(var) == 0: continue

            maximum = 0
            for j in xrange(len(var)-1):
                ISF = 1000/(var[j+1]-var[j])
                if maximum < ISF: maximum = ISF
            peakISF[r, c] = maximum

        plt.plot(stims, peakISF[:,c], label=str(cmpt[c]))

    plt.xlabel("stimulus pulse number", fontsize=15)
    plt.ylabel("peak ISF [Hz]", fontsize=15)
    plt.legend()
    tmp = filename.rsplit('.',1)
    imgFilename = "%s_peakISF.png"%tmp[0]
    plt.savefig(imgFilename)

    plt.close()

    # tmp = filename.rsplit('.',1)
    # csvfilename = "%s_spikecounts.csv"%tmp[0]
    # with open(csvfilename,'wb') as f:
    #     writer = csv.writer(f)
    #     for i in range(n_stim):
    #         writer.writerow([stims[i], counts[i]])


if __name__ == "__main__":
    print "::::: spike_analyze.py :::::"
    matplotlib.rc('xtick',labelsize = 15)
    matplotlib.rc('ytick',labelsize = 15)

    if len(sys.argv) is 1:
        print "NO FILENAME"
    elif len(sys.argv) is 2:
        if(os.path.isfile(sys.argv[1])):
            s = readSpikeRecordFile(sys.argv[1])
            Pulses = reconstruct_data(s)
            drawSpikeCounts(Pulses,sys.argv[1],1)
            drawPeakISF(Pulses,sys.argv[1],1)
        elif(os.path.isdir(sys.argv[1])):
            print "%s is directory"%sys.argv[1]
            target_dir = os.path.normpath(sys.argv[1])
            for fname in os.listdir(target_dir):
                full_dir = os.path.join(target_dir,fname)
                if(os.path.isfile(full_dir)):
                    ext = os.path.splitext(full_dir)
                    if(ext[1] == '.dat'):
                        print full_dir                    
                        spikes = readSpikeRecordFile(full_dir)
                        Pulses = reconstruct_data(spikes)
                        drawSpikeCounts(Pulses,full_dir,0)
                        drawPeakISF(Pulses,full_dir,0)
        else:
            print "Wrong directory or filename"
    else:
        print "Wrong input"


