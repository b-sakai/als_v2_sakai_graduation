# -*- coding: utf-8 -*-

"""
swcファイルから特定のエリアのコンパートメント番号を抽出して、300_glomerular.txtなどとして保存するプログラム

Usage:
$ python glomerular_extraction.py

by Buntaro Sakai 20181031
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

def extract_compartment(x_min, x_max, y_min, y_max, z_min, z_max):
    for i, pre in enumerate(comps):
        if x_min < pre[2] and pre[2] < x_max:
            if y_min < pre[3] and pre[3] < y_max:
                if z_min < pre[4] and pre[4] < z_max:
                    synlist.append(i)
                    print i




if __name__ == "__main__":


    #swc_path = "../../../swc/040823_5_sn_bestrigid0106_mkRegion.swc"
    swc_path = "../../../swc/050205_7_sn_bestrigid0106_mkRegion.swc"
    print "load completed"

  
    output_filename = "301_glomerular.dat"
    print "start reading swc"

    comps = read_swc(swc_path)
    print comps
    print "comps completed"


    x_min = 176
    x_max = 241
    y_min = 14
    y_max = 192
    z_min = 33
    z_max = 88

    synlist = []
    extract_compartment(x_min, x_max, y_min, y_max, z_min, z_max)
    print "set completed"

    with open(output_filename, "w") as f:
        for syn in synlist:
            f.write("%d\n"%syn)
