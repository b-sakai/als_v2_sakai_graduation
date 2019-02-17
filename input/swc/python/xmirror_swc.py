import swc
import sys

filename = sys.argv[1]
swcData = swc.read(filename)
header = swcData[0]
dswc = swcData[1]


for i in range(len(dswc)):
    dswc[i].x = 328.0 - dswc[i].x


swc.write("mirror" + filename, dswc, header)
print "mirror " + filename + " is written"

