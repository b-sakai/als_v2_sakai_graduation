#! /usr/bin/python
# coding: utf-8

#--------------------------
# mkSynapseList.py
# 2015/01/08
#--------------------------

#--------------------------
# About this program
#  SWCファイルのTypeに記載されている情報（T==7、であればSynapseRegion）
#　をもとにしてSynapseRegionのコンパートメントを長さ定数で正規化し、ランダムで
#　シナプスを生成する。またその情報をSynapseList_swcファイル名.txtで保存する。
#-------------------------

from neuron import h
import neuron as nrn
import numpy as np
from itertools import chain

import swc #import swc.py

h.load_file("CellSwc_Ver2.hoc")

#calculate section axial resistance(internal resistance)
def Calc_SRi(cell, num_sec):
    sri = cell.Dend[num_sec].Ra /(np.pi*(cell.Dend[num_sec].diam/2)**2 * (10**8))
    #print cell.Dend[num_sec].Ra, cell.Dend[num_sec].diam
    return sri

#calcuate section membrane resistance
def Calc_SRm(cell, num_sec):
    #print num_sec
    srm = 10**4/(cell.Dend[num_sec].gl_hh * cell.Dend[num_sec].L)
    return srm

def Calc_LengthConstant(cell, num_sec):
    Ri = Calc_SRi(cell, num_sec)
    Rm = Calc_SRm(cell, num_sec)
    lc  = np.sqrt(Rm/Ri)
    return lc

def Calc_SumOfNormalizedLength(cell, dendlist, sum_list):
    sum_ = 0;
    for i in range(len(dendlist)):
        normalized_length = cell.Dend[dendlist[i]].L / Calc_LengthConstant(cell, dendlist[i])
        sum_ = sum_ + normalized_length
        sum_list.append(sum_)
    return sum_

#重複するコンパートメント番号が生成されることを考慮してない
def matching_RandomNumbers_and_NormalizedLengthSum(cell, dendlist, sum_list, sumofnl, numberofsynapse):
    synapse_list = []
    rnd = sumofnl * np.random.random(numberofsynapse)
    print "len(rnd):%d"%(len(rnd))
    print "len(sum_list):%d"%(len(sum_list))
    #    print sum_list
    k=0
    for i in range(len(rnd)):
        #print "i %d, rnd[%d] %d"%(i,i,rnd[i])
        for j in range(len(sum_list)):
            if j==0:
                if(sum_list[j]>=rnd[i]):
                    synapse_list.append(dendlist[j])
                    k+=1
            if j>0:
                if(sum_list[j-1]<rnd[i])&(sum_list[j]>=rnd[i]):
                    synapse_list.append(dendlist[j])
                    if(k!=i):
                        print "ERROR %d, %d"%((k-i),rnd[k])
                    #print dendlist[j], sum_list[j], rnd[i],i,k,j
                    k+=1

    return synapse_list


def write_Synlist(filename, synlist):
    #filename = 'SynapseList.dat'
    f = open(filename,'w')
    f.write(repr(len(synlist))+'\n')
    for i in range(len(synlist)):
        data = "%d\n"%synlist[i]
        f.write(data)
    f.close()

# Find Synase Region from swc file
# append dendrite number which is Synapse Region type in SynapseRegionList
def findSynapseRegion(cell, dendlist):
    counter = 0
    for i in range(int(cell.SectionNum)):
        parentID = int(cell.pID.x[i])
	parentType = int(cell.Type.x[parentID])
        cellType = int(cell.Type.x[i])
        if((cellType == 7) and (parentType == 7)):
            #print parentID, parentType, cellType
            dendlist.append(i)
            counter +=1
    print "SYNAPSE COMPARTMENT NUMBER : %d\n"%(counter)

if __name__ == "__main__":
    files = ["200000.swc", "300000.swc", "301000.swc"]
    for file in files:

        CELL = h.CellSwc(file)
        for sec in h.allsec():
            sec.insert('hh')
        swcData = swc.read(file)

        SynapseRegionList = []
        #-----------------------------------
        # Find Synapse Region
        #-----------------------------------
        findSynapseRegion(CELL, SynapseRegionList)
        print SynapseRegionList
        
        #-----------------------------------
        # Normalizing Length
        #-----------------------------------
        normalized_length_sum = []
        sum_nl = Calc_SumOfNormalizedLength(CELL, SynapseRegionList, normalized_length_sum)
        print "sum_nl:%d"%(sum_nl)
        
        #-----------------------------------
        # make synapse
        #-----------------------------------
        if file[0] == "2":
            N = 5
            NUMBEROFSYNAPSE = 300
        elif file[0] == "3":
            N = 18
            NUMBEROFSYNAPSE = 200
        else: 
            print "error %s\n" % file

        for i in xrange(N):
            SYNLIST = matching_RandomNumbers_and_NormalizedLengthSum(CELL, SynapseRegionList, normalized_length_sum, sum_nl, NUMBEROFSYNAPSE)

            syn_filename = file.split(".")[0][:4] + ("%02d"%i) +'_synlist.dat' 
            write_Synlist(syn_filename,SYNLIST)
            print syn_filename
