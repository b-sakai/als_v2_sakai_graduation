import numpy as np

def write_swc(filename, swc, header):
    swcFile = open(filename, 'w')
    swcFile.writelines(header)
    for i in range(len(swc)):
        print swc[i].n
        swcdata_ = "%d %d %f %f %f %f %d\n" % (swc[i].n, swc[i].T, swc[i].x, swc[i].y, swc[i].z, swc[i].R, swc[i].P)
        #print "%d %d %f %f %f %f %d\n" % (swc[i].n, swc[i].T, swc[i].x, swc[i].y, swc[i].z, swc[i].R, swc[i].P)
        swcFile.writelines(swcdata_)
    swcFile.close()

class swc(object):
    n = 0    #Sample Number
    T = 0    #Structure Identifier
    x = 0.0  #x position
    y = 0.0  #y position
    z = 0.0  #z position
    R = 0.0  #Radius
    P = 0    #Parent Sample Number

Header = "#ORIGINAL_SOURCE IOSIM\n#CREATURE\n#REGION\n#FIELD/LAYER\n#TYPE\n#CONTRIBUTOR\n#REFERENCE\n#RAW\n#EXTRAS\n#SOMA_AREA\n#SHINKAGE_CORRECTION 1.000000 1.000000 1.000000\n#VERSION_NUMBER\n#VERSION_DATE 2012-01-28\n#SCALE 1.0 1.0 1.0\n"



num_comp = 100
seclist = []
for i in range(num_comp):
    sec = swc()
    sec.n = i+1
    sec.T = 0
    sec.x = np.float64(i)
    sec.y = np.float64(0)
    sec.z = np.float64(0)
    sec.R = np.float64(1.0)
    sec.P = i
    seclist.append(sec)

write_swc("KC.swc", seclist, Header)
