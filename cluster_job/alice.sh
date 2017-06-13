#!/bin/sh

#PBS -l nodes=1:ppn=68:xeonphi
#--PBS -q xeonphi

#module load torque compiler/gcc-4.8.2 openmpi/1.8.4/gcc-4.8.2.lp
#/usr/bin/mpi-selector --set openmpi-1.10.4-gnu64-4.8.5 -y

cd $PBS_O_WORKDIR
mpirun /bin/hostname
# mpirun ./a.out