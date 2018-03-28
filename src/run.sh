#! /bin/bash

# Make directory to save data file
Time=`date '+%m%d%H%M%S'`
echo "TIME : ${Time}"
RESULT_DIR="../result/"
RECORD_DIR="${RESULT_DIR}${Time}/record"
SPIKE_DIR="${RESULT_DIR}${Time}/spike"
OUT="${RESULT_DIR}${Time}/out"
#SPIKERECORD_DIR="${BASE_DIR}${Time}/spike"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR}
mkdir -p ${SPIKE_DIR}

#NRNIV="/Users/arasekosuke/lab/neuron_kplus/specials/x86_64/special -mpi"
NRNIV='/home/arase/github/neuron_kplus/specials/x86_64/special -mpi'

#HOC_NAME="./main_antenna.hoc"
HOC_NAME="./main.hoc"
#HOC_NAME="./ln_test.hoc"
#HOC_NAME="./main_test.hoc"
#HOC_NAME="./loadbalance_test.hoc"

NRNOPT=\
" -c STOPTIME=2000"\
" -c IS_SUPERCOMPUTER=2"\
" -c INTERVAL=5000"\
" -c START_TIME=${Time}"\
" -c SAVE_ALL=0"\
" -c NCELL=40"\
" -c WEIGHT_200=0.02"\
" -c WEIGHT_300=0.006"\
" -c WEIGHT_301=0.006"\
" -c WEIGHT_M=0.03"\
" -c WEIGHT_GO_300=0.01"\
" -c WEIGHT_GO_301=0.1"\
" -c COMP_0=65"\
" -c COMP_1=5737"\
" -c COMP_2=5025"\
" -c COMP_3=9743"\
" -c GABAA_ON=1"\
" -c GABAB_ON=1"\
" -c DOSE=3000"\
" -c NSTIM=1"\
" -c MECHANO_SPONTANEOUS=10"\
" -c MECHANO_ON=1"\
" -c GENERAL_ODOR_ON=1"\
" -c GABAA_GMAX_LTOP=0.1"\
" -c GABAA_GMAX_LTOL=0.75"\
" -c GABAB_GMAX_LTOP=0.02"\
" -c GABAB_GMAX_LTOL=0.0"\
" -c GBAR_TIMES_LN=3.0"\
" -c GBAR_TIMES_PN=1.0"


#MPIEXEC="mpiexec  -n 2"
MPIEXEC="mpiexec -n 56"
#MPIEXEC="mpiexec -n 68"
#MPIEXEC="mpiexec -n 24"
#MPIEXEC="mpiexec -n 5"
#MPIEXEC="mpiexec -n 1"
#MPIEXEC=""

EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

#mpiexec -np 4 $NRNMPI/nrniv -mpi parallel_simulation1201.hoc
#mpiexec -np 8 ./mod/x86_64/special -mpi main.hoc
echo $EXEC
time $EXEC |tee $OUT

#python drawGraph.py $RECORD_DIR
#python drawISF.py $SPIKE_DIR
