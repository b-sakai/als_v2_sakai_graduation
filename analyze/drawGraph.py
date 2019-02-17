#! /usr/bin/python
#-------------------------------------------------
#This Program is for drawing graph with voltage record
#
# How to use this program
# $ipython drawGraph.py filenames
# $ipython drawGraph.py directory
# comment added 2015.03.30
#-------------------------------------------------


import sys
import os.path
import numpy as np

import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pylab as plt

def drawGraph(filename):
    datafile = open(filename,'r')
    data = datafile.readlines()
    nDatas, nColumns = data[0].split(' ')
    nDatas = int(nDatas)
    nColumns = int(nColumns)
    print filename
    print nDatas, nColumns
    vec = [[0 for i in range(nDatas)] for j in range(nColumns)]
    svec = [0 for i in range(nDatas)]

    dummy = []
    for i in range(0,nDatas):
        #print i
        #print data[i].split('\t')
        dummy = data[i+1].split('\t')
        for j in range(nColumns):
            #print j, dummy[j]
            try:
                vec[j][i]=float(dummy[j])
            except ValueError:
                print dummy[j]
            except IndexError:
                print j,"  ", i

    tmp = filename.rsplit('.',1)
    imgFilename = "%s.png"%tmp[0]

    flg = plt.figure()
    if 'Synaptic' in filename:
        for i in range(nDatas):
            for j in range(1,nColumns):
                svec[i] += vec[j][i]
        plt.plot(vec[0], svec)
        plt.ylabel("Current[nA]")        
        _SAVETXT_NAME_ = "%s_Sum.dat"%(tmp[0])
        np.savetxt(_SAVETXT_NAME_, svec, fmt="%.5f")
    elif 'GABA' in filename:
        for i in range(nDatas):
            for j in range(1,nColumns):
                svec[i] += vec[j][i]
        plt.plot(vec[0], svec)
        plt.ylabel("Current[nA]")        
        _SAVETXT_NAME_ = "%s_Sum.dat"%(tmp[0])
        np.savetxt(_SAVETXT_NAME_, svec, fmt="%.5f")
    else:
        plt.ylabel("membrain potential[mV]")

    for j in range(1,nColumns):
        plt.plot(vec[0], vec[j])
    #pylab.ylim(-100, 80)
    #pylab.xlim(0,500)
    plt.xlabel("time[ms]")
    #pylab.ylabel("current[nA]")
    
    #print imgFilename, tmp
    plt.title(imgFilename)
    plt.savefig(imgFilename)

    plt.close()
    """
    #### Graph for Thesis big
    fig = plt.figure(figsize=(8,3),dpi=400)
    fig.subplots_adjust(bottom=0.2)
    ax = fig.add_subplot(111)
    #plt.rcParams['font.family'] = 'Times New Roman'
    plt.rcParams['font.size'] = 20
    #plt.rcParams['axes.linewidth'] = 1.5
    #plt.rcParams['xtics.major.size'] = 10
    #plt.rcParams['xtics.major.width'] = 1.5
    plt.axis('off')
    plt.plot(vec[0],vec[1],'b')
    #plt.plot([0,1000],[-80,-80],'k',linewidth=4.0)
    plt.plot([0,200],[-80,-80],'k',linewidth=4.0)
    
    plt.plot([-100,-100],[-100,-50],'k',linewidth=4.0)
    plt.text(-100,-75, '50mV', ha = 'right', va = 'center')
    plt.plot([-100,0],[-100,-100],'k',linewidth=4.0)
    plt.text(-50,-100, '100ms', ha = 'center', va = 'top')
    #plt.legend(frameon=False)
    plt.xlim(-100,3000)
    plt.ylim(-100,60)
    plt.xlabel("Time[ms]")
    plt.ylabel("membrain potential[mV]")
    plt.savefig("%s_forThesis.png"%(imgFilename))
    plt.close()
    """

if len(sys.argv) is 1:
    print "NO FILENAME"
elif len(sys.argv) is 2:
    if(os.path.isfile(sys.argv[1])):
        drawGraph(sys.argv[1])
    elif(os.path.isdir(sys.argv[1])):
        print "%s is directory"%sys.argv[1]
        target_dir = os.path.normpath(sys.argv[1])
        for fname in os.listdir(target_dir):
            full_dir = os.path.join(target_dir,fname)
            if(os.path.isfile(full_dir)):
                ext = os.path.splitext(full_dir)
                if(ext[1] == '.txt'):
                    print full_dir                    
                    drawGraph(full_dir)
    else:
        print "Wrong directory or filename"
else:
    print "Wrong input"

"""
elif len(sys.argv) is 2:
    Filename = sys.argv[1]
    drawGraph(Filename)
elif len(sys.argv) is 3:
    target_dir = os.path.normpath(sys.argv[2])
    if((sys.argv[1] = '-r')&os.path.exists(target_dir):
"""    
       
        
