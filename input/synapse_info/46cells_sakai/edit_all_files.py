import os
import glob



NLN = 35
files = []
for i in range(NLN):
    if i <= 7:
        files.append("30000" + str(i) + "syn.dat")
    elif i <= 16:
        files.append("30100" + str(i - 8) + "syn.dat")
    elif i <= 25:
        files.append("30200" + str(i - 17) + "syn.dat")
    else:
        files.append("30300" + str(i - 26) + "syn.dat")
print files

NPN = 11
for i in range(NPN):
    files.append("2000" + str(i).zfill(2) + "syn.dat")
print files


for file in files:
    prefix = file.split("syn")[0]
    if prefix[0] == "2":
        with open(file, "w") as f:
            f.write("# This file shows the file path of synapse\n")
            f.write("$ fromRN\n")
            f.write("../input/synapse_list/fromRN/%s_synlist.dat\n"%prefix)
    else:
        flag = 0
        with open(file, "w") as f:
            f.write("# This file shows the file path of synapse\n")
            # write fromRN files
            f.write("$ fromRN\n")
            f.write("../input/synapse_list/fromRN/syn_glomerulars/%s\n"%prefix[:3])
            # write fromMRN files
            f.write("$ fromMRN\n")
            f.write("../input/synapse_list/fromMRN/%s.dat\n"%prefix)
            # write CtoC files
            f.write("$ CtoC\n")
            print prefix[2]
            if prefix[2] == "0":
                f.write("38\n") # num of CtoC files
            else:
                f.write("37\n") # num of CtoC files
            for i in range(NPN):
                pnName = "2000" + str(i).zfill(2)
                f.write(prefix + " " + pnName + " ../input/synapse_list/46cells/" + prefix + "_" + pnName + "_manual.txt\n")
            for i in range(NLN):
                lnName = files[i].split("syn")[0]
                if prefix[2] != lnName[2]:
                    f.write(prefix + " " + lnName + " ../input/synapse_list/46cells/" +prefix + "_" + lnName + "_randomize.txt\n")


















