import sys
import os.path

def calculate_diff(filename):
    weight_data = open(filename, "r")

    diff = 0
    predata = 0.0
    i = 0
    for data in weight_data:
        if i == 1:
            predata = float(data.split()[1])
        elif i != 0:
            diff += abs(float(data.split()[1]) - predata)
            predata = float(data.split()[1])
        i += 1
    print diff

if len(sys.argv) is 1:
    print "NO FILENAME"
elif len(sys.argv) is 2:
    if(os.path.isfile(sys.argv[1])):
        drawGraph(sys.argv[1])
    elif(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if(ext[1] == '.dat'):
                    print full_dir                    
                    calculate_diff(full_dir)
    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"
