#!/bin/sh

# usage
# sh run_spike_analyze.sh ~/lab/result/1201spike_analyze

_LISPDIRS=`find $1 -maxdepth 1 -mindepth 1 -type d`

for _DIRS in ${_LISPDIRS}; do
    echo ${_DIRS}
    python spike_analyze.py ${_DIRS}
done