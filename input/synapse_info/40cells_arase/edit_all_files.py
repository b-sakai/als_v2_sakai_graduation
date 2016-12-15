import os
import glob

files = glob.glob("*syn.dat")

for file in files:
    with open(file, "r") as f:
        lines = f.readlines()
    with open(file, "w") as f:
        for i, line in enumerate(lines):
            if line == "$ fromRN\n":
                f.write(line)
                f.write(lines[i+1])
                f.write("$ fromMRN\n")
            else:
                f.write(line)
