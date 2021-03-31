#! /bin/bash
tfile=$(mktemp)
metex --prefix $tfile. 10 && test -f $tfile.0.png && rm $tfile.0.png
