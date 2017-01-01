import os
import glob

files = glob.glob("*syn.dat")

for file in files:
    prefix = file.split("syn")[0]
    if prefix[0] == "2":
        continue
    else:
        with open(file, "r") as f:
            lines = f.readlines()
        with open(file, "w") as f:
            for line in lines:
                if "400cells" in line:
                    var = line.split("400cells")
                    unko = var[0] + "400cells_arase" + var[1]
                    # print unko
                    f.write(var[0] + "400cells_arase" + var[1])
                elif "SynapseList.dat" in line:
                    f.write(line)
                    f.write("$ fromMRN\n")
                    if prefix[2] == "0":
                        f.write("../input/synapse_list/fromMRN/300%03d.dat\n" % (int(prefix[3:])%18))
                    elif prefix[2] == "1":
                        f.write("../input/synapse_list/fromMRN/301%03d.dat\n" % (int(prefix[3:])%17))
                    else:
                        print "wrong prefix %s."%prefix
                else:
                    f.write(line)


