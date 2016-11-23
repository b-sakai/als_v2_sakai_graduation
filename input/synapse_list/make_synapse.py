# -*- coding: utf-8 -*-

"""
USAGE
$ python make_synapse.py [target_directory]
"""

import os
import sys
import random

target = os.path.abspath(sys.argv[1]) + "/"
files = os.listdir(target)
# nconnections = 100
# n_comps_300 = 22928
# n_comps_301 = 12525

nconnections = 10

"""
comps[300_301 or 301_300][pre or post]
"""

comps = [[[21015,14644, 8240,15191, 8804,21375, 8239,15706,15171,21088],\
          [11079,10877,11534,11093,11257,10351,11580,11879,11949,11038]],\
         [[10351,10877,11083,10380,11422,11681,10351,11083,11219,11093],\
          [21374,15191, 8242,21309, 8239, 9486,21436, 8804,21088,15070]]]

gid = 3000000

for file in files:
    pre_cell, post_cell, _ = file.split("_")
    if pre_cell[0] == "3" and post_cell[0] == "3":
        with open(target + file, "w") as f:
            f.write("$ PRE_CELL %s\n" % pre_cell)
            f.write("$ POST_CELL %s\n" % post_cell)
            f.write("$ NCONNECTIONS %d\n" % nconnections)
            index = int(pre_cell[2])
            for i in xrange(nconnections):
                f.write("%d %d %d\n" % (comps[index][0][i], comps[index][1][i], gid+i))
            gid += 10