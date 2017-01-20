import os
import glob
import random
import numpy as np


files = glob.glob("./before_reduction/*.dat")
print files

for file in files:
    index = file.split("_")[2]
    # src_prefix = file.split("/")[2].split("_")[:1]
    # print src_prefix

    if index == "5":
#        num_synapses = 800
        num_synapses = 100
        target_prefix = "3000"
        ncells = 17
    elif index == "7":
#        num_synapses = 600
        num_synapses = 100
        target_prefix = "3010"
        ncells = 16
    else:
        print "wrong .dat file in ./before_reduction/"
        break

    with open(file, "r") as f:
        lines = f.readlines()
        synlist = [None] * len(lines)
        for i, line in enumerate(lines):
            synlist[i] = line.split("[")[2].split("]")[0]

    for i in xrange(ncells+1):
        reduced_synlist = np.random.choice(synlist, num_synapses, replace=False)
        # print len(reduced_synlist)
        target_suffix = "%02d"%i
        print target_suffix
        with open(target_prefix + target_suffix + ".dat", "w") as f:
            f.write(str(num_synapses)+"\n")
            for syn in reduced_synlist:
                # index = random.randint(0,len(not_toroid)-1)
                f.write(str(syn)+"\n")
                # print syn
