# -*- coding: utf-8 -*-

"""
swcファイルから各糸球体のエリア（６０分割）のコンパートメント番号を抽出して、300/300_i_glomerular.datなどとして保存するプログラム
/300, /301というディレクトリをつくってファイルを保存するので予め'rm 30*'などで消しておく必要があることに注意
Usage:
$ python ln_glomerular_extraction.py

by Buntaro Sakai 20181224
"""
import sys
import math
import numpy as np
import os
import random


# parameter for extraction
a = 80
b = 75
c = 70

xc = 164  # center of x
yc = 195  # center of y
zc = 90  # center of z

# parameter for read
numsynapse = 3

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

def shell(comp):
    return comp[2]**2 / (a/2)**2 + comp[3]**2 / (b/2)**2 + comp[4]**2 / (c/2)**2 > 1

def shell_outer(comp):
    return (comp[2] - xc)**2 / a**2 + (comp[3] - yc)**2 / b**2 + (comp[4] - zc)**2 / c**2 < 1.2

def abs_yx_degree(x, y):
    xr = x - xc
    yr = y - yc
    result = math.degrees(math.atan2(abs(xr), yr))
    if result < 0:
        result = 90 - result
    return result

def xz_degree(x, z):
    xr = x - xc
    zr = z - zc
    result = math.degrees(math.atan2(zr, xr))

    if zr < 0:
        result = 360 + result
    
    return result
        
    

def comb(num, i):
    return 360.0 / num * i






def read_extract_save(swc_path, output_id):    
    print "load completed"

    print "start reading swc"

    comps = read_swc(swc_path)
    print comps
    print "comps completed"

    print "the all compartment number is " + str(len(comps))
#    shell_comps = [i for i in comps if shell(i)]  # extract compartment in the AL shell
    shell_comps = [i for i in comps if shell_outer(i)]  # extract compartment in the AL shell    
    print "the all compartment number in the shell is " + str(len(shell_comps))

    comps_glomerulars = [[] for i in range(60)]
    print comps_glomerulars

    phais = []

    for i in range(len(shell_comps)):
        comp = shell_comps[i]
        theta = 180 - abs_yx_degree(comp[2], comp[3])
        phai = 360 - xz_degree(comp[2], comp[4])
        phais.append(phai)
        if theta < 20:
            if 0 <= phai and phai < 90:
                comps_glomerulars[0].append(int(comp[0]))
            elif 90 <= phai and phai < 180:
                comps_glomerulars[1].append(int(comp[0]))
            elif 180 <= phai and phai < 270:
                comps_glomerulars[2].append(int(comp[0]))
            elif 270 <= phai and phai < 360:
                comps_glomerulars[3].append(int(comp[0]))
        elif  theta < 60:
            if 0 <= phai and phai < 36:
                comps_glomerulars[4].append(int(comp[0]))
            elif 36 <= phai and phai < 72:
                comps_glomerulars[5].append(int(comp[0]))
            elif 72 <= phai and phai < 108:
                comps_glomerulars[6].append(int(comp[0]))
            elif 108 <= phai and phai < 144:
                comps_glomerulars[7].append(int(comp[0]))
            elif 144 <= phai and phai < 180:
                comps_glomerulars[8].append(int(comp[0]))
            elif 180 <= phai and phai < 216:
                comps_glomerulars[9].append(int(comp[0]))
            elif 216 <= phai and phai < 252:
                comps_glomerulars[10].append(int(comp[0]))
            elif 252 <= phai and phai < 288:
                comps_glomerulars[11].append(int(comp[0]))
            elif 288 <= phai and phai < 324:
                comps_glomerulars[12].append(int(comp[0]))
            elif 324 <= phai and phai < 360:
                comps_glomerulars[13].append(int(comp[0]))
        elif theta < 90:
            if phai < comb(16,1):
                comps_glomerulars[14].append(int(comp[0]))
            elif phai < comb(16,2):
                comps_glomerulars[15].append(int(comp[0]))
            elif phai < comb(16,3):
                comps_glomerulars[16].append(int(comp[0]))
            elif phai < comb(16,4):
                comps_glomerulars[17].append(int(comp[0]))
            elif phai < comb(16,5):
                comps_glomerulars[18].append(int(comp[0]))
            elif phai < comb(16,6):
                comps_glomerulars[19].append(int(comp[0]))
            elif phai < comb(16,7):
                comps_glomerulars[20].append(int(comp[0]))
            elif phai < comb(16,8):
                comps_glomerulars[21].append(int(comp[0]))
            elif phai < comb(16,9):
                comps_glomerulars[22].append(int(comp[0]))
            elif phai < comb(16,10):
                comps_glomerulars[23].append(int(comp[0]))
            elif phai < comb(16,11):
                comps_glomerulars[24].append(int(comp[0]))
            elif phai < comb(16,12):
                comps_glomerulars[25].append(int(comp[0]))
            elif phai < comb(16,13):
                comps_glomerulars[26].append(int(comp[0]))
            elif phai < comb(16,14):
                comps_glomerulars[27].append(int(comp[0]))
            elif phai < comb(16,15):
                comps_glomerulars[28].append(int(comp[0]))
            elif phai < comb(16,16):
                comps_glomerulars[29].append(int(comp[0]))
        elif theta < 125:
            if phai < comb(16,1):
                comps_glomerulars[30].append(int(comp[0]))
            elif phai < comb(16,2):
                comps_glomerulars[31].append(int(comp[0]))
            elif phai < comb(16,3):
                comps_glomerulars[32].append(int(comp[0]))
            elif phai < comb(16,4):
                comps_glomerulars[33].append(int(comp[0]))
            elif phai < comb(16,5):
                comps_glomerulars[34].append(int(comp[0]))
            elif phai < comb(16,6):
                comps_glomerulars[35].append(int(comp[0]))
            elif phai < comb(16,7):
                comps_glomerulars[36].append(int(comp[0]))
            elif phai < comb(16,8):
                comps_glomerulars[37].append(int(comp[0]))
            elif phai < comb(16,9):
                comps_glomerulars[38].append(int(comp[0]))
            elif phai < comb(16,10):
                comps_glomerulars[39].append(int(comp[0]))
            elif phai < comb(16,11):
                comps_glomerulars[40].append(int(comp[0]))
            elif phai < comb(16,12):
                comps_glomerulars[41].append(int(comp[0]))
            elif phai < comb(16,13):
                comps_glomerulars[42].append(int(comp[0]))
            elif phai < comb(16,14):
                comps_glomerulars[43].append(int(comp[0]))
            elif phai < comb(16,15):
                comps_glomerulars[44].append(int(comp[0]))
            elif phai < comb(16,16):
                comps_glomerulars[45].append(int(comp[0]))
        elif theta < 160:
            if 0 <= phai and phai < 36:
                comps_glomerulars[46].append(int(comp[0]))
            elif 36 <= phai and phai < 72:
                comps_glomerulars[47].append(int(comp[0]))
            elif 72 <= phai and phai < 108:
                comps_glomerulars[48].append(int(comp[0]))
            elif 108 <= phai and phai < 144:
                comps_glomerulars[49].append(int(comp[0]))
            elif 144 <= phai and phai < 180:
                comps_glomerulars[50].append(int(comp[0]))
            elif 180 <= phai and phai < 216:
                comps_glomerulars[51].append(int(comp[0]))
            elif 216 <= phai and phai < 252:
                comps_glomerulars[52].append(int(comp[0]))
            elif 252 <= phai and phai < 288:
                comps_glomerulars[53].append(int(comp[0]))
            elif 288 <= phai and phai < 324:
                comps_glomerulars[54].append(int(comp[0]))
            elif 324 <= phai and phai < 360:
                comps_glomerulars[55].append(int(comp[0]))
        else:
            if 0 <= phai and phai < 90:
                comps_glomerulars[56].append(int(comp[0]))
            elif 90 <= phai and phai < 180:
                comps_glomerulars[57].append(int(comp[0]))
            elif 180 <= phai and phai < 270:
                comps_glomerulars[58].append(int(comp[0]))
            elif 270 <= phai and phai < 360:
                comps_glomerulars[59].append(int(comp[0]))

    num_glomerulars = [len(comps_glomerulars[i]) for i in range(len(comps_glomerulars))]
    print num_glomerulars
    print sum(num_glomerulars)

    for comps in comps_glomerulars:
        random.shuffle(comps)

    output_dir = output_id
    os.mkdir(output_dir)
    for i in range(60):
        output_filename =  output_id + "/" + output_id + "_" + str(i).zfill(2) + "_glomerulars.dat"
        with open(output_filename, "w") as f:
            if len(comps_glomerulars[i]) < numsynapse:
                f.write("%d\n"%len(comps_glomerulars[i]))
            else:
                f.write("%d\n"%numsynapse)

            for syn in comps_glomerulars[i]:
                f.write("%d\n"%syn)


if __name__ == "__main__":
    swc_path = "../../../swc/040823_5_sn_bestrigid0106_mkRegion.swc"
    output_id = "300"
    read_extract_save(swc_path, output_id)

    swc_path = "../../../swc/050205_7_sn_bestrigid0106_mkRegion.swc"
    output_id = "301"
    read_extract_save(swc_path, output_id)

    swc_path = "../../../swc/mirror040823_5_sn_bestrigid0106_mkRegion.swc"
    output_id = "302"
    read_extract_save(swc_path, output_id)

    swc_path = "../../../swc/mirror050205_7_sn_bestrigid0106_mkRegion.swc"
    output_id = "303"
    read_extract_save(swc_path, output_id)
