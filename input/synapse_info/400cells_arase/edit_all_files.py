import os
import glob

files = glob.glob("*syn.dat")

for file in files:
    prefix = file.split("syn")[0]
    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for line in lines:
            if "/general" in line:
#                if prefix[0] == "2":
#                    f.write("../input/synapse_list/fromRN/%d_synlist.dat\n"%( int(prefix[4:])%5+200000 ))
#                else:
                f.write("../input/synapse_list/general_odor/%d.dat\n"%( int(prefix[3:])%17+int(prefix[:3])*1000 ))
            else:
                f.write(line)

