# -*- coding: utf-8 -*-

"""
LN - LN 結合を求めるプログラム
synapse 間距離 < sys.argv[1] を満たす組を抽出し，synapses_between_LN.dat として保存するプログラム

Usage:
$ python detect_synapses_between_LN.py

by Kosuke Arase 20170113
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

    swc_path1 = "../swc/040823_5_sn_bestrigid0106_mkRegion.swc"
    swc_path2 = "../swc/050205_7_sn_bestrigid0106_mkRegion.swc"
    output_filename = "synapses_between_LN.dat"

    comps1 = read_swc(swc_path1)
    comps2 = read_swc(swc_path2)

    synlist = []
    calc_distance()

    with open(output_filename, "w") as f:
        f.write("# 300_syn 301_syn\n")
        f.write("# num of data: %d\n" % len(synlist))
        for syn in synlist:
            f.write("%d %d %f\n"%syn)
