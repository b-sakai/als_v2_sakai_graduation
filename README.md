About this simulator
als : Antenal Lobe Simulator
this simulator is based on github.com/arase/als_v2 
this simulator could run on the cluster
this program simulate  "the response of AL to two alternate general odor stimulation"
the result is saved /result directory


How to use this simulator in cluster
0. load module of mpi (module load torque compiler/gcc-4.8.2 openmpi/1.10.2/gcc-4.8.2.lp)
1. git clone neuron_kplus
2. git clone als_v2_sakai_graduation (this simulator)
3. copy mod files (cp als_v2_sakai_graduation/mod/* to neuron_kplus/mod)
4. compile neuron in the neuron_kplus (refer to the documentation of neuron_kplus)
5. change the path of src1/run.sh
6. execute the program (sh run.sh)


Directory structure
/analyze        python program for generating graph of PSTH, ISF, membrance potential from result
/input          input stimulus file and swc file for multicompartment and connect file
/mod            mod file necessary for simulator
/old            directories of old simulator
/result         simulation result of spike and membrance potential
/src            source code for simulation
/visualize      python programs for generating vtk file from saved 
/vtk            place of vtk file and movie file generated from vtk file

message_slack.py  program of sending message to slack (need to configulate slack application)
upload_slack.py   program of uploading to slack (need to configulate slack application)


*** this simulator is graduation research theme by b-sakai
