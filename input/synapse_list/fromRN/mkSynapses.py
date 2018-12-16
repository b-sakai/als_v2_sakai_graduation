import os
import glob
import random
import numpy as np


files = glob.glob("./before_reduction/*_glomerular.txt")
print files

for file in files:
    index = file.split("/")[2][:3]
    print(index)
    if index == "300":
#        num_synapses = 800
        num_synapses = 200
        target_prefix = "3000"
        ncells = 18
    elif index == "301":
#        num_synapses = 600
        num_synapses = 200
        target_prefix = "3010"
        ncells = 17
    elif index == "200":
#        num_synapses = 600
        num_synapses = 100
        target_prefix = "2000"
        target_suffix = "00"
        ncells = 1
    elif index == "201":
#        num_synapses = 600
        num_synapses = 100
        target_prefix = "2000"
        target_suffix = "01"
        ncells = 1
    elif index == "202":
#        num_synapses = 600
        num_synapses = 100
        target_prefix = "2000"
        target_suffix = "02"
        ncells = 1
    elif index == "203":
#        num_synapses = 600
        num_synapses = 100
        target_prefix = "2000"
        target_suffix = "03"
        ncells = 1
    elif index == "204":
#        num_synapses = 600
        num_synapses = 100
        target_prefix = "2000"
        target_suffix = "04"
        ncells = 1
    else:
        print "wrong .dat file in ./before_reduction/"
        break

    with open(file, "r") as f:
        lines = f.readlines()
        synlist = [None] * len(lines)
        for i, line in enumerate(lines):
            synlist[i] = line.strip()


    for i in xrange(ncells):
        reduced_synlist = np.random.choice(synlist, num_synapses, replace=False)
        # print len(reduced_synlist)
        if target_prefix == "2000":
            print "making 2000"
        else:
            target_suffix = "%02d"%i
        print target_suffix
        with open(target_prefix + target_suffix + "_synlist.dat", "w") as f:
            f.write(str(num_synapses)+"\n")
            for syn in reduced_synlist:
                # index = random.randint(0,len(not_toroid)-1)
                f.write(str(syn)+"\n")
                # print syn




