#!/bin/bash

# usage

# sh download_spike.sh [jobID] [local path after $HOME]
# ex. sh download_spike.sh 5475341 lab/result/compare_compartments/

source ~/.bashrc

target="$2/$1"
echo $target
echo $HOME
mkdir $HOME/$target
scpfromk result/spike/$1/* $HOME/$target

#python spike_analyze.py $HOME/$target

