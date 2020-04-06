#!/bin/bash

SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
PROJECT_PATH="$(dirname ${SCRIPT_PATH})"
START_PATH="$(dirname ${PROJECT_PATH})"
MAIN=${PROJECT_PATH}/main.py


echo "Benchmark for comparison 3D Models"
echo "PROJECT_PATH: ${PROJECT_PATH}"
echo "START_PATH: ${START_PATH}"
echo "MAIN: ${MAIN}"

export PYTHONPATH=${START_PATH}

python3 ${MAIN}