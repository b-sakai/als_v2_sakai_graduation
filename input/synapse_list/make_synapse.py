# -*- coding: utf-8 -*-

"""
synapses_between_*.dat からシナプス結合のリストを取得し，指定されたディレクトリ以下のシナプス結合ファイルをランダムに生成する
numpy 使ってないから京上でも動く

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
            print map(int, line.split()[:2])
            var[0][i], var[1][i] = map(int, line.split()[:2])
    return var


def make_synapse_Arase():
    gid = [2000000, 3000000]

    for file in files:
        #print file
        pre_cell, post_cell, _ = file.split("/")[-1].split("_")
        
        #print post_cell[0]
        if post_cell[0] == "2":
            if pre_cell[2] == "0":
                if post_cell[5] == "0":
                    synlist = syn_200_300
                elif post_cell[5] == "1":
                    synlist = syn_201_300
                elif post_cell[5] == "2":
                    synlist = syn_202_300
                elif post_cell[5] == "3":
                    synlist = syn_203_300
                elif post_cell[5] == "4":
                    synlist = syn_204_300
            elif pre_cell[2] == "1":
                if post_cell[5] == "0":
                    synlist = syn_200_301
                elif post_cell[5] == "1":
                    synlist = syn_201_301
                elif post_cell[5] == "2":
                    synlist = syn_202_301
                elif post_cell[5] == "3":
                    synlist = syn_203_301
                elif post_cell[5] == "4":
                    synlist = syn_204_301
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
            if gid_index == 0: # LN to PN
                n = 10
                n_toroid = 0
            else: # LN to LN in og
                n = 10
                n_toroid = 0


            f.write("$ PRE_CELL %s\n" % pre_cell)
            f.write("$ POST_CELL %s\n" % post_cell)
            f.write("$ NCONNECTIONS %d\n" % (n + n_toroid))

            index = random.sample(xrange(len(synlist[0])), n)

            """ ln - pn in toroid or ln - ln in OG """
            for i in index:
                gid[gid_index] += 1
                f.write("%d %d %d\n" % (synlist[1][i], synlist[0][i], gid[gid_index]))


            """ ln - ln in toroid """
            if post_cell[0] == "3":
                if pre_cell[2] == "0":
                    synlist = [syn_300_301_toroid[1], syn_300_301_toroid[0]]
                elif pre_cell[2] == "1":
                    synlist = syn_300_301_toroid
                else:
                    print "something wrong with %s" % file
                index = random.sample(xrange(len(synlist[0])), n_toroid)
                for i in index:
                    gid[gid_index] += 1
                    f.write("%d %d %d\n" % (synlist[1][i], synlist[0][i], gid[gid_index]))



if __name__ == "__main__":
    target = os.path.abspath(sys.argv[1]) + "/"
    # target = "30temp/"
    files = glob.glob("{0}*.txt".format(target))

    syn_200_300 = read_data("synapses_between_717_300_selected.dat")
    syn_200_301 = read_data("synapses_between_717_301_selected.dat")

    syn_201_300 = read_data("synapses_between_7171_300_selected.dat")
    syn_201_301 = read_data("synapses_between_7171_301_selected.dat")

    syn_202_300 = read_data("synapses_between_7172_300_selected.dat")
    syn_202_301 = read_data("synapses_between_7172_301_selected.dat")

    syn_203_300 = read_data("synapses_between_7173_300_selected.dat")
    syn_203_301 = read_data("synapses_between_7173_301_selected.dat")

    syn_204_300 = read_data("synapses_between_7174_300_selected.dat")
    syn_204_301 = read_data("synapses_between_7174_301_selected.dat")

    syn_300_301 = read_data("synapses_between_LN_OG.dat")
    syn_300_301_toroid = read_data("synapses_between_LN_toroid.dat")

    # nconnections = 10
    
    #print files
    #print target
    make_synapse_Arase()
