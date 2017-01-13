#!/bin/bash

# usage

# sh download_spike.sh [jobID] [destination]
# ex. sh download_spike.sh 5475341 ~/lab/result/compare_compartments/

source ~/.bashrc

target="$2/$1"
echo $target
echo $HOME
mkdir $target
scpfromk result/record/$1/*tar $target

#python spike_analyze.py $HOME/$target

