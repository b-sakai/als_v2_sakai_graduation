class CELL:
      def __init__(self):
      	  self.gid     = -1
	  self.cellid  = -1
	  self.swcid   = -1
	  self.cloneid = -1
	  self.swcpath = "none"
	  self.ppath   = "none"
	  self.synpath = "none"

      def set(self, gid, cellid, swcid, swcpath, synpath):
      	  self.gid = gid
	  self.cellid = cellid
	  self.swcid = swcid
	  self.swcpath = swcpath
	  self.synpath = synpath



filename = "../network_info_1200rns.dat"

wlines = []
with open(filename, "r") as f:
     f.readline()
     lines = f.readlines()
     for i, line in enumerate(lines):
         print i  
         print line  
     	 if line[0] != "#" and line[0] != "$":
	    elem = line.split()
	    wline = " ".join([elem[0], elem[1], str(int((i-1)/100.0)), str(int((i-1)/20.0)), elem[4], elem[5], elem[6]])
	    wlines.append(wline)
	 else:
	    wlines.append(line)

wfilename = "../new_network_info_1200rns.dat"
with open(wfilename, "w") as f:
    f.write("# gid, cellid, swcid, cloneid, gloid, SWC file path, position&rotation file, Synapse information file\n")
    for line in wlines:
        f.write(line + "\n")
	
	
	    
	    
