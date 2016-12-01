# -*- coding: utf-8 -*-

"""
USAGE
$ python make_synapse.py [target_directory]
"""

import os
import sys
import random

"""
comps_to_ln[300_301 or 301_300][pre or post] by Park
comps_to_pn[300_200 or 301_200][pre or post] by Park
"""

comps_to_ln = \
[[[21015,14644, 8240,15191, 8804,21375, 8239,15706,15171,21088],\
[11079,10877,11534,11093,11257,10351,11580,11879,11949,11038]],\
[[10351,10877,11083,10380,11422,11681,10351,11083,11219,11093],\
[21374,15191, 8242,21309, 8239, 9486,21436, 8804,21088,15070]]]

comps_to_pn = \
[[[2739, 2730, 2366, 2363, 2055, 2050, 1809, 1801, 1590, 1579],\
[110,  107,  104,  101,  98,   97,   94,   114,  109,  102]],\
[[3572, 4958, 5487, 1846, 6691, 7140, 3610, 3524, 2733, 4517],\
[101,  102,  94,   98,   125,  119,  114,  108,  103,  93]]]


def make_synapse_Park():
    gid_to_ln = 3000000
    gid_to_pn = 2000000

    n = 10

    for file in files:
        pre_cell, post_cell, _ = file.split("_")
        if post_cell[0] == "3":
            with open(target + file, "w") as f:
                f.write("$ PRE_CELL %s\n" % pre_cell)
                f.write("$ POST_CELL %s\n" % post_cell)
                f.write("$ NCONNECTIONS %d\n" % n)
                index = int(pre_cell[2])
                for i in xrange(n):
                    f.write("%d %d %d\n" % (comps_to_ln[index][0][i], comps_to_ln[index][1][i], gid_to_ln+i))
                gid_to_ln += n
        elif post_cell[0] == "2":
            with open(target + file, "w") as f:
                f.write("$ PRE_CELL %s\n" % pre_cell)
                f.write("$ POST_CELL %s\n" % post_cell)
                f.write("$ NCONNECTIONS %d\n" % n)
                index = int(pre_cell[2])
                for i in xrange(10):
                    f.write("%d %d %d\n" % (comps_to_pn[index][0][i], comps_to_pn[index][1][i], gid_to_pn+i))
                gid_to_pn += n


def make_synapse_Arase(n):
    gid_to_ln = 3000000
    gid_to_pn = 2000000

    for file in files:
        pre_cell, post_cell, _ = file.split("_")
        if post_cell[0] == "3":
            with open(target + file, "w") as f:
                f.write("$ PRE_CELL %s\n" % pre_cell)
                f.write("$ POST_CELL %s\n" % post_cell)
                f.write("$ NCONNECTIONS %d\n" % nconnections)
                pre_index = int(pre_cell[2])
                post_index = int(post_cell[2])
                for i in xrange(n):
                    f.write("%d %d %d\n" % (random.randint(1, n_comps[pre_index]), random.randint(1, n_comps[post_index]), gid_to_ln+i))
                gid_to_ln += n
        elif post_cell[0] == "2":
            with open(target + file, "w") as f:
                f.write("$ PRE_CELL %s\n" % pre_cell)
                f.write("$ POST_CELL %s\n" % post_cell)
                f.write("$ NCONNECTIONS %d\n" % n)
                index = int(pre_cell[2])
                for i in xrange(10):
                    f.write("%d %d %d\n" % (comps_to_pn[index][0][i], comps_to_pn[index][1][i], gid_to_pn+i))
                gid_to_pn += n


if __name__ == "__main__":
    target = os.path.abspath(sys.argv[1]) + "/"
    files = os.listdir(target)

    nconnections = 40
    n_comps = [22928-5, 12525-5] #[300, 301]

    #make_synapse_Park()
    make_synapse_Arase(nconnections)
