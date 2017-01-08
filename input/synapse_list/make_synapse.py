# -*- coding: utf-8 -*-

"""
synapses_between_*.dat からシナプス結合のリストを取得し，指定されたディレクトリ以下のシナプス結合ファイルをランダムに生成する
京上でも動く

USAGE
$ python make_synapse.py [target_directory]
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
            var[0][i], var[1][i] = map(int, line.split())
    return var


def make_synapse_Arase(n):
    gid = [2000000, 3000000]

    for file in files:
        print file
        pre_cell, post_cell, _ = file.split("/")[-1].split("_")

        if post_cell[0] == "2":
            if pre_cell[2] == "0":
                synlist = syn_200_300
            elif pre_cell[2] == "1":
                synlist = syn_200_301
            else:
                print "something wrong with %s" % file
        elif post_cell[0] == "3":
            if pre_cell[2] == "0":
                synlist = [syn_300_301[1], syn_300_301[0]]
            elif pre_cell[2] == "1":
                synlist = syn_300_301
            else:
                print "something wrong with %s" % file
        else:
            print "something wrong with %s" % file

        with open(file, "w") as f:
            gid_index = int(post_cell[0])-2
            #k = 4 if gid_index == 0 else 1
            k = 1

            f.write("$ PRE_CELL %s\n" % pre_cell)
            f.write("$ POST_CELL %s\n" % post_cell)
            f.write("$ NCONNECTIONS %d\n" % (k*n))

            index = random.sample(xrange(len(synlist[0])), k*n)
            

            for i in index:
                gid[gid_index] += 1
                f.write("%d %d %d\n" % (synlist[1][i], synlist[0][i], gid[gid_index]))


if __name__ == "__main__":
    target = os.path.abspath(sys.argv[1]) + "/"
    # target = "30temp/"
    files = glob.glob("{0}*.txt".format(target))

    syn_200_300 = read_data("synapses_between_200_300.dat")
    syn_200_301 = read_data("synapses_between_200_301.dat")
    syn_300_301 = read_data("synapses_between_300_301.dat")

    nconnections = 10

    make_synapse_Arase(nconnections)
