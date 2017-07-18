import os
import glob
import random
import numpy as np


files = glob.glob("./before_reduction/*_toroid.txt")
print files

for file in files:
    index = file.split("/")[2][:3]
    print(index)
    if index == "300":
#        num_synapses = 800
        num_synapses = 200
        target_prefix = "3000"
        ncells = 17
    elif index == "301":
#        num_synapses = 600
        num_synapses = 200
        target_prefix = "3010"
        ncells = 16
    elif index == "200":
#        num_synapses = 600
        num_synapses = 300
        target_prefix = "2000"
        ncells = 4
    else:
        print "wrong .dat file in ./before_reduction/"
        break

    with open(file, "r") as f:
        lines = f.readlines()
        synlist = [None] * len(lines)
        for i, line in enumerate(lines):
            synlist[i] = line.strip()

    for i in xrange(ncells+1):
        reduced_synlist = np.random.choice(synlist, num_synapses, replace=False)
        # print len(reduced_synlist)
        target_suffix = "%02d"%i
        print target_suffix
        with open(target_prefix + target_suffix + "_synlist.dat", "w") as f:
            f.write(str(num_synapses)+"\n")
            for syn in reduced_synlist:
                # index = random.randint(0,len(not_toroid)-1)
                f.write(str(syn)+"\n")
                # print syn
