import os
import glob

files = glob.glob("*syn.dat")

for file in files:
    prefix = file.split("syn")[0]
    if prefix[0] == "2":
        with open(file, "w") as f:
            f.write("# This file shows the file path of synapse\n")
            f.write("$ fromRN\n")
            f.write("../input/synapse_list/fromRN/050622_4_sn_SynapseList.dat\n")
    else:
        flag = 0
        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            for line in lines:
                if "/general_odor/" in line:
                    f.write("../input/synapse_list/general_odor/%s%02d.dat\n"%(prefix[:4],int(prefix[4:])%17))
                else:
                    f.write(line)


