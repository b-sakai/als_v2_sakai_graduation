# -*- coding: utf-8 -*-

"""
LN,PN間のシナプスを求めるプログラム
./fromRN/glomerulars/300のコンパートメントとPN軸索初節部のコンパートメント../comp_pnAxon/717.datとのシナプスをsynapses_between_300_201.dat などとして保存するプログラム
swc ファイルの指定と出力ファイルの指定は随時書き換えてください．

Usage:
$ python ltop_detect_synapses.py

by Buntaro Sakai 20181224
"""

import sys
import os
import numpy as np
import random


def read_comp(path):
    comps = []
    for line in open(path, 'r'):
        line = line.replace('\n', '')
        line = line.replace('\r', '')
        comps.append(int(line))
    return comps


def make_random_pair_of_ln_and_pn(ln_path, pn_path, ouput_filename):
#    print "load completed"

    output_dir = "../syn_Sakai.d/ltop/"
#    print "start reading comp"
#    print pn_comps
#    print "pn_comps read"
    ln_comps = read_comp(ln_path)
    pn_comps = read_comp(pn_path)

    random.shuffle(ln_comps)
    print "ln_comps read"
    print len(ln_comps)

    synlist = []
    for i in range(min(len(ln_comps), len(pn_comps))):
        synlist.append((ln_comps[i], pn_comps[i]))
        
#    print "set completed"
#    print synlist

    with open(output_dir + output_filename, "w") as f:
        f.write("# %s_syn %s_syn\n" % (output_filename.split(".")[0].split("_")[2], output_filename.split(".")[0].split("_")[3]))
        f.write("# num of data: %d\n" % len(synlist))
        for syn in synlist:
            f.write("%d %d\n"%syn)


if __name__ == "__main__":

    pn_glomerular =[["0","6"],
                    ["1","5"],
                    ["2","19"],
                    ["3","18"],
                    ["4","17"],
                    ["5","16"],
                    ["6","15"],
                    ["7","35"],
                    ["8","34"],
                    ["9","33"],
                    ["10","32"]]
    for j in range(len(pn_glomerular)):
        for i in range(4):
            pn_path = "../comp_pnAxon/717axon.dat"
            ln_path = "../fromRN/syn_glomerulars/30" + str(i) + "/30" + str(i) + "_" +  str(pn_glomerular[j][1].zfill(2)) + "_glomerulars.dat"
            output_filename = "synapses_between_2" + str(pn_glomerular[j][0].zfill(2)) + "_30" + str(i) + ".dat"
            print output_filename
            make_random_pair_of_ln_and_pn(ln_path, pn_path, output_filename)
