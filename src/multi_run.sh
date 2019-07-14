
#! /bin/bash

# argument
Arg1=$1

# Make directory to save data file
Time=`date '+%m%d%H%M%S'`
echo "TIME : ${Time}"
RESULT_DIR="../result/"
RECORD_DIR="${RESULT_DIR}${Time}/record"
SPIKE_DIR="${RESULT_DIR}${Time}/spike"
OUT="${RESULT_DIR}${Time}/out"
echo "DATA DIRECTORY : ${RECORD_DIR}"
mkdir -p ${RECORD_DIR}
mkdir -p ${SPIKE_DIR}

NRNIV='/home/sakai/neuron_kplus_temp/specials/x86_64/special -mpi'
HOC_NAME="./wmain.hoc"

NRNOPT=\
" -c STOPTIME=10"\
" -c IS_SUPERCOMPUTER=2"\
" -c INTERVAL=1000"\
" -c START_TIME=${Time}"\
" -c SAVE_ALL=0"\
" -c NCELL=46"\
" -c WEIGHT_200=0.02"\
" -c WEIGHT_300=0.06"\
" -c WEIGHT_301=0.06"\
" -c WEIGHT_M=0.0"\
" -c WEIGHT_GO_300=0.0"\
" -c WEIGHT_GO_301=0.0"\
" -c COMP_0=65"\
" -c COMP_1=5737"\
" -c COMP_2=5025"\
" -c COMP_3=9743"\
" -c GABAA_ON=1"\
" -c GABAB_ON=1"\
" -c DOSE=3000"\
" -c NSTIM=1"\
" -c MECHANO_SPONTANEOUS=10"\
" -c MECHANO_ON=0"\
" -c GENERAL_ODOR_ON=0"\
" -c GABAA_GMAX_LTOP=0.75"\
" -c GABAA_GMAX_LTOL=0.001"\
" -c GABAB_GMAX_LTOP=0.001"\
" -c GABAB_GMAX_LTOL=0.0"\
" -c GBAR_TIMES_LN=1.0"\
" -c GBAR_TIMES_PN=1.0"\
" -c LEARNING=${Arg1}"

MPIEXEC="mpiexec -n 56"
EXEC="${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"

echo $EXEC
time $EXEC |tee $OUT

wait

python ../analyze/drawPSTH.py $SPIKE_DIR
python ../analyze/drawGraph.py $RECORD_DIR
python ../analyze/drawISF.py $SPIKE_DIR
python ../analyze/calculate_synaptic_change_ltop.py $RECORD_DIR
