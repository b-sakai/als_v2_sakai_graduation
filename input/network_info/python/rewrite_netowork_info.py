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



filename = "network_info_46cells.dat"

wlines = []
with open(filename, "r") as f:
     f.readline()
     lines = f.readlines()
     for i, line in enumerate(lines):
     	 if line[0] != "#" and line[0] != "$":
	    elem = line.split()

	    splsynpath = elem[6].split("/")
	    splsynpath[3] = "46cells_sakai"
	    synpath = "/".join(splsynpath)
	    
	    wline = " ".join([elem[0], elem[1], elem[2], elem[3], elem[4], elem[5], synpath])
	    print wline
	    wlines.append(wline)
	 else:
	    wlines.append(line)

wfilename = "new_network_info_46cells.dat"
with open(wfilename, "w") as f:
    for line in wlines:
        f.write(line + "\n")
	
	
	    
	    
