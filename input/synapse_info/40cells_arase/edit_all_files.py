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
                f.write(line)
                if "fromRN" in line:
                    if prefix[2] == "0":
                        f.write("../input/synapse_list/fromRN/040823_5_sn_SynapseList.dat\n")
                    elif prefix[2] == "1":
                        f.write("../input/synapse_list/fromRN/050205_7_sn_SynapseList.dat\n")
                    else:
                        print "wrong prefix %s."%prefix

