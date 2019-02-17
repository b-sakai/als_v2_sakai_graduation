#!/bin/bash -x
#PJM --rsc-list "node=6"
#PJM --rsc-list "elapse=10:00:00"
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
#PJM --stgin "rank=* ./input/spiketiming/* %r:../input/spiketiming/"
#PJM --stgin "rank=* ./input/spiketiming/1000dose_30stims_filtering/* %r:../input/spiketiming/1000dose_30stims_filtering/"
#PJM --stgin "rank=* ./input/spiketiming/1000dose_1stims_filtering/* %r:../input/spiketiming/1000dose_1stims_filtering/"


#PJM --stgin "rank=* ./input/swc/* %r:../input/swc/"
#PJM --stgin "rank=* ./input/swc/rn0514/* %r:../input/swc/rn0514/"
#PJM --stgin "rank=* ./input/synapse_info/* %r:../input/synapse_info/"
#PJM --stgin "rank=* ./input/synapse_info/40cells/* %r:../input/synapse_info/40cells/"
#PJM --stgin "rank=* ./input/synapse_info/syn/* %r:../input/synapse_info/syn/"
#PJM --stgin "rank=* ./input/synapse_list/* %r:../input/synapse_list/"
#PJM --stgin "rank=* ./input/synapse_list/40cells/* %r:../input/synapse_list/40cells/"
#PJM --stgin "rank=* ./input/synapse_list/fromRN/* %r:../input/synapse_list/fromRN/"

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
" -c STOPTIME=100"\
" -c IS_SUPERCOMPUTER=1"\
" -c INTERVAL=300"\
" -c GABAA_ON=0"\
" -c GABAB_ON=0"


#LPG="lpgparm -t 4MB -s 4MB -d 4MB -h 4MB -p 4MB"

MPIEXEC="mpiexec -mca mpi_print_stats 1"
#MPIEXEC="mpiexec -mca mpi_print_stats 2 -mca mpi_print_stats_ranks 0"

#PROF="fapp -C -d ./prof -L1 -Hevent=Statistics"
#PROF="fipp -C -Ihwm,call -d ./prof"
PROF=""

echo "${PROF} ${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}"
time ${PROF} ${MPIEXEC} ${NRNIV} ${NRNOPT} ${HOC_NAME}

sync

