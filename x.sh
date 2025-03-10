#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file_to_run> <contest_name>"
    exit 1
fi

file_to_run=$1
contest_name=$2

/usr/local/bin/python3 /Users/tedvtorov/Desktop/MISIS/dma/run_tests.py ${file_to_run} ${contest_name}