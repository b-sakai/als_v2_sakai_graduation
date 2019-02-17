import os
import glob
import random
import numpy as np


files = glob.glob("./MRNsyn_data/*_excluded.txt")
print files

for file in files:
    index = file.split("/")[2][2]
    print(index)
    if index == "0":
        num_synapses = 100
        target_prefix = "3000"
        ncells = 8
        print "index = 0"
    elif index == "1":
        num_synapses = 100
        target_prefix = "3010"
        ncells = 9
    if index == "2":
        num_synapses = 100
        target_prefix = "3020"
        ncells = 9
    elif index == "3":
        num_synapses = 100
        target_prefix = "3030"
        ncells = 9
#    else:
#        print "wrong .dat file in ./MRNsyn_data"
#        break

    print "reading"
    with open(file, "r") as f:
        lines = f.readlines()
        synlist = [None] * len(lines)
        for i, line in enumerate(lines):
            synlist[i] = line.strip()

    print "writing"
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
