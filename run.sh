#!/bin/bash

python train2vw.py train.csv train.vw
python test2vw.py test.csv test.vw

# validation
# vw train.vw --oaa 10 -c --passes 100 --cubic xxx -P 1e4 --l1 6e-7 -b 25 

# number of examples per pass = 22523
# passes used = 42
# weighted example sum = 945987
# weighted label sum = 0
# average loss = 0.069972 h
# best constant = 0
# total feature number = 123924297

# train
vw train.vw --oaa 10 -c --passes 42 --cubic xxx -P 1e4 --l1 6e-7 -b 25 --holdout_off -f model

# predict
vw test.vw -t -i model -p p.txt

python p2kaggle.py p.txt p.csv
gzip -k p.csv
