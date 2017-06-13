#!/bin/bash

#PBS -l nodes=2:ppn=28
#PBS -q cluster

module load torque compiler/gcc-4.8.2 openmpi/1.10.2/gcc-4.8.2.lp
#cd $PBS_O_WORKDIR
cd /home/arase/kanzaki_lab/als_v2/src/
sh run.sh