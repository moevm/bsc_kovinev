#!/bin/bash

dir_ui_raw="../ui_raw"
dir_ui="../ui"


for filename in $dir_ui_raw/*.ui; do
    name=${filename##*/}
    base=${name%.ui}
    pyuic5 $filename -o "$dir_ui/$base.py"
done
