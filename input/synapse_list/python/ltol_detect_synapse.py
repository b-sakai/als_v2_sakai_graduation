# -*- coding: utf-8 -*-

"""
シナプスを求めるプログラム
synapse 間距離 < sys.argv[1] を満たす組を抽出し，synapses_between_300_301.dat などとして保存するプログラム
ALのLNの間のシナプスの組を抽出するのに使用
全てのLNの種類に対して、使用

Usage:
$ python detect_synapses.py

by Buntaro Sakai 20190112
"""

import sys
import numpy as np


def read_swc(path):
    print "a"
    with open(path, "r") as f:
        while len(f.readline()) >= 3 :
            continue
        lines = f.readlines()



    n = len(lines)
    comps = np.ndarray([n, 7]) #id, type, x, y, z, d, parent

    for i, line in enumerate(lines):
        comps[i] = np.array(map(float, line.split()))

    return comps


def calc_distance():
    for i, pre in enumerate(comps1):
        if i%100 == 0:
            print i
        for j, post in enumerate(comps2):
            distance = np.linalg.norm(pre[2:5]-post[2:5])
            if distance < max_distance:
                synlist.append((i, j, distance))
                #print (i, j)
        # if i > 30:
        #     break


if __name__ == "__main__":
    max_distance = float(sys.argv[1])
    print max_distance

    # paths of ln
    LNpattern = 4
    swc_path_300 = "../../swc/040823_5_sn_bestrigid0106_mkRegion.swc"
    swc_path_301 = "../../swc/050205_7_sn_bestrigid0106_mkRegion.swc"
    swc_path_302 = "../../swc/mirror040823_5_sn_bestrigid0106_mkRegion.swc"
    swc_path_303 = "../../swc/mirror050205_7_sn_bestrigid0106_mkRegion.swc"
    swc_path = [swc_path_300, swc_path_301, swc_path_302, swc_path_303]
    print "load completed"

    
    for i in range(4):
        for j in range(4):
            if i != j:
                output_filename = "../syn_Sakai.d/synapses_between_30" + str(i) + "_30" + str(j) + ".dat"
                print output_filename
                line1 = "# %s_syn %s_syn\n" % ("30"+str(i),  "30"+str(j))
                print line1
                print "start reading swc"

                comps1 = read_swc(swc_path[i])
                print comps1
                print "comps1 completed"
                comps2 = read_swc(swc_path[j])
                print "comps2 completed"

                synlist = []
                calc_distance()
                print "set completed"

                with open(output_filename, "w") as f:
                    f.write(line1)
                    f.write("# num of data: %d\n" % len(synlist))
                    print len(synlist)
                    for syn in synlist:
                        f.write("%d %d %f\n"%syn)
