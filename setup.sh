#!/bin/bash

pip3 install --upgrade pip
python3 -m venv venv
source venv/bin/activate
pip3 install pipreqs
pip3 install -r requirements.txt

./01-mfield.sh
./02-heliocoord.py Mercury 2011-Mar-23Z00:00 2015-May-01Z00:00 1m > mercury-pos-min.txt
./03-checkout.sh > checkout.dat
