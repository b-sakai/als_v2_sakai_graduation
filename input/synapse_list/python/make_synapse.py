# -*- coding: utf-8 -*-

"""
./syn_Sakai.d/synapses_between_*.dat からシナプス結合のリストを取得し，指定されたディレクトリ以下のシナプス結合ファイルをランダムに生成する
numpy 使ってないから京上でも動く

USAGE
$ python make_synapse.py
"""

import os
import sys
import glob
import random


def read_data(filename):
    with open(filename, "r") as f:
        f.readline()
        num = int(f.readline().split()[-1])
        var = [[None for i in xrange(num)], [None for i in xrange(num)]]
        lines = f.readlines()
        for i, line in enumerate(lines):
#           print map(int, line.split()[:2])
            var[0][i], var[1][i] = map(int, line.split()[:2])
    return var


def make_synapse_Sakai():
    gid = [2000000, 3000000]


    for file in files:
        print file
        pre_cell, post_cell, _ = file.split("/")[-1].split("_")

        if post_cell[0] == "2":
            file_dir = "../syn_Sakai.d/ltop/"
            filename = "synapses_between_" + post_cell[0:3] + "_" +  pre_cell[0:3] + ".dat"
        else:
            file_dir = "../syn_Sakai.d/"
            filename = "synapses_between_" + pre_cell[0:3] + "_" +  post_cell[0:3] + ".dat"

        synlist = read_data(file_dir + filename)

        with open(file, "w") as f:

            gid_index = int(post_cell[0])-2
            n = 10

            f.write("$ PRE_CELL %s\n" % pre_cell)
            f.write("$ POST_CELL %s\n" % post_cell)
            f.write("$ NCONNECTIONS %d\n" % n)

            index = random.sample(xrange(len(synlist[0])), n)

         
            for i in index:
                gid[gid_index] += 1
                f.write("%d %d %d\n" % (synlist[0][i], synlist[1][i], gid[gid_index]))





if __name__ == "__main__":
#    target = os.path.abspath(sys.argv[1]) + "/"
#    files = glob.glob("{0}*.txt".format(target))

    output_dir = "../46cells/"

    NLN = 35
    lnName = []
    for i in range(NLN):
        if i <= 7:
            lnName.append("3000" + str(i).zfill(2))
        elif i <= 16:
            lnName.append("3010" + str(i - 8).zfill(2))
        elif i <= 25:
            lnName.append("3020" + str(i - 17).zfill(2))
        else:
            lnName.append("3030" + str(i - 26).zfill(2))
    print lnName

    NPN = 11
    files = []
    for i in range(NLN):
        for j in range(NPN):
            files.append(output_dir + lnName[i] + "_2000" + str(j).zfill(2) + "_manual.txt")
    for i in range(NLN):
        for j in range(NLN):
            pre = lnName[i][2]
            post = lnName[j][2] 
            if pre != post:
                files.append(output_dir + lnName[i] + "_" + lnName[j] + "_randomize.txt")
    

    make_synapse_Sakai()

   
