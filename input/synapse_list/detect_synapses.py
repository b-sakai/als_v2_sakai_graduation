# -*- coding: utf-8 -*-

"""
シナプスを求めるプログラム
synapse 間距離 < sys.argv[1] を満たす組を抽出し，synapses_between_300_301.dat などとして保存するプログラム
swc ファイルの指定と出力ファイルの指定は随時書き換えてください．

Usage:
$ python detect_synapses.py

by Kosuke Arase 20170115
"""

import sys
import numpy as np


def read_swc(path):
    with open(path, "r") as f:
        while len(f.readline())!= 1:
            continue
        lines = f.readlines()

    n = len(lines)
    comps = np.ndarray([n, 7]) #id, type, x, y, z, d, parent

    for i, line in enumerate(lines):
        comps[i] = np.array(map(float, line.split()))

    return comps


def calc_distance():
    for i, pre in enumerate(comps1):
        for j, post in enumerate(comps2):
            distance = np.linalg.norm(pre[2:5]-post[2:5])
            if distance < max_distance:
                synlist.append((i, j, distance))
                print (i, j)
        # if i > 30:
        #     break


if __name__ == "__main__":
    max_distance = float(sys.argv[1])

    swc_path_200 = "../swc/050622_4_sn_bestrigid0106_mkRegion.swc"
    swc_path_300 = "../swc/040823_5_sn_bestrigid0106_mkRegion.swc"
    swc_path_301 = "../swc/050205_7_sn_bestrigid0106_mkRegion.swc"

    # output_filename = "synapses_between_200_300.dat"
    output_filename = "synapses_between_200_300.dat"
    # output_filename = "synapses_between_300_301.dat"

    comps1 = read_swc(swc_path_200)
    comps2 = read_swc(swc_path_300)

    synlist = []
    calc_distance()

    with open(output_filename, "w") as f:
        f.write("# %s_syn %s_syn\n" % (output_filename.split(".")[0].split("_")[2], output_filename.split(".")[0].split("_")[3]))
        f.write("# num of data: %d\n" % len(synlist))
        for syn in synlist:
            f.write("%d %d %f\n"%syn)
