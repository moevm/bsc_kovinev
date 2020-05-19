#!/bin/bash

file=../venv/lib/python3.8/site-packages/direct/showbase/ShowBase.py
sed -i "s/base')/base_')/g" $file