#!/bin/bash -x
#PJM --rsc-list "node=6"
#PJM --rsc-list "elapse=3:30:00"
#PJM --rsc-list "rscgrp=small"
#PJM --mpi "proc=48"
#PJM -s

# staging
#PJM --stg-transfiles all
#PJM --mpi "use-rankdir"

# CHANGE TO YOUR OWN DIR
#PJM --stgin-basedir /home/hp160269/k03367/als_v2/
#PJM --stgin "rank=* ./result/* %r:./result/"
#PJM --stgin "rank=* ./result/record/* %r:./result/record/"
#PJM --stgin "rank=* ./result/spike/* %r:./result/spike/"

#PJM --stgin "rank=* ./input/* %r:../input/"
#PJM --stgin "rank=* ./input/network_info/* %r:../input/network_info/"
#PJM --stgin "rank=* ./input/spiketiming_arase/* %r:../input/spiketiming_arase/"
#PJM --stgin "rank=* ./input/spiketiming_arase/ORN/* %r:../input/spiketiming_arase/ORN/"
#PJM --stgin "rank=* ./input/spiketiming_arase/ORN/3000ng_1stim/* %r:../input/spiketiming_arase/ORN/3000ng_1stim/"
#PJM --stgin "rank=* ./input/spiketiming_arase/MRN/* %r:../input/spiketiming_arase/MRN/"
#PJM --stgin "rank=* ./input/spiketiming_arase/MRN/10Hz_1stim/* %r:../input/spiketiming_arase/MRN/10Hz_1stim/"
#PJM --stgin "rank=* ./input/spiketiming_arase/MRN/10Hz_constant/* %r:../input/spiketiming_arase/MRN/10Hz_constant/"
#PJM --stgin "rank=* ./input/spiketiming_arase/general_odor/* %r:../input/spiketiming_arase/general_odor/"


#PJM --stgin "rank=* ./input/swc/* %r:../input/swc/"
#PJM --stgin "rank=* ./input/swc/rn0514/* %r:../input/swc/rn0514/"
#PJM --stgin "rank=* ./input/synapse_info/* %r:../input/synapse_info/"
#PJM --stgin "rank=* ./input/synapse_info/40cells_arase/* %r:../input/synapse_info/40cells_arase/"
#PJM --stgin "rank=* ./input/synapse_list/* %r:../input/synapse_list/"
#PJM --stgin "rank=* ./input/synapse_list/40cells_arase/* %r:../input/synapse_list/40cells_arase/"
#PJM --stgin "rank=* ./input/synapse_list/fromRN/* %r:../input/synapse_list/fromRN/"
#PJM --stgin "rank=* ./input/synapse_list/fromMRN/* %r:../input/synapse_list/fromMRN/"
#PJM --stgin "rank=* ./input/synapse_list/general_odor/* %r:../input/synapse_list/general_odor/"

#PJM --stgin "rank=* ./src/* %r:./"
#PJM --stgin "rank=* ../neuron_kplus/stgin/* %r:./"
#PJM --stgin "rank=* ../neuron_kplus/specials/sparc64/special %r:./"

#PJM --stgout "rank=* %r:./*.txt /data/hp160269/arase/al_V2/%j/record/"
#PJM --stgout "rank=* %r:./*.hoc /data/hp160269/arase/al_V2/%j/src/"

#PJM --stgout "rank=* %r:./result/record/* /data/hp160269/arase/result/record/%j/"
#PJM --stgout "rank=* %r:./result/spike/* /data/hp160269/arase/result/spike/%j/"

# SET UP ENVIRONMENT OF LANGUAGE 
. /work/system/Env_base

#--#export OMP_NUM_THREADS=8

NRNIV="./special -mpi"
HOC_NAME="./main.hoc"
#NRNOPT=""
NRNOPT=\
" -c STOPTIME=2000"\
" -c IS_SUPERCOMPUTER=1"\
" -c INTERVAL=5000"\
" -c SAVE_ALL=1"\
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


#LPG="lpgparm -t 4MB -s 4MB -d 4MB -h 4MB -p 4MB"

MPIEXEC="mpiexec -mca mpi_print_stats 1"
#MPIEXEC="mpiexec -mca mpi_print_stats 2 -mca mpi_print_stats_ranks 0"

#PROF="fapp -C -d ./prof -L1 -Hevent=Statistics"
#PROF="fipp -C -Ihwm,call -d ./prof"
PROF=""

echo "${PROF} ${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"
time ${PROF} ${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}

sync

