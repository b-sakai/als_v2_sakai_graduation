# -*- coding: utf-8 -*-

"""
toroid 領域での synapse 間距離を計算した結果：300_301_dist.csv 等
ここから synapse 間距離 < 10 を満たす組を抽出し，synapses_between_300_301.dat 等として保存するプログラム

Usage:
$ python peters_rule.py [filename] [max_distance]

ex:
$ python peters_rule.py 300_301_dist.csv 10

by Kosuke Arase 20170107 
"""

import sys
import numpy as np

def extract_comp(s):
    var = s.split("[")[2]
    return int(var[:-1])


input_filename = sys.argv[1] # "300_301_dist.csv"
cell0, cell1, _ = input_filename.split("_")
output_filename = "synapses_between_{0}_{1}.dat".format(cell0, cell1)

max_distance = float(sys.argv[2])

with open(input_filename, "r") as f:
    lines = f.readlines()

synapses = np.ndarray([3, len(lines)]) # distance, 300, 301
for i, line in enumerate(lines):
    comp0, comp1, dis = line.split(",")
    synapses[:, i] = [float(dis), extract_comp(comp0), extract_comp(comp1)]

candidates = synapses[:, np.where(synapses[0]<max_distance)[0]]

with open(output_filename, "w") as f:
    f.write("# {0}_syn {1}_syn\n".format(cell0, cell1))
    f.write("# num of data: %d\n" % len(candidates[0]))
    for (s0, s1) in zip(map(int, candidates[1]), map(int, candidates[2])):
        f.write("%d %d\n" % (s0+2, s1+2)) # 朴さんの距離計算プログラムにバグがあり，コンパートメント番号が2つずれているためその修正 
