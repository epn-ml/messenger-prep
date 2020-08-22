#!/usr/bin/env python
import requests

BASE_URL='https://pds-ppi.igpp.ucla.edu/search/view'
PDS_ID='pds://PPI/MESS-E_V_H_SW-MAG-4-SUMM-CALIBRATED-V1.0/DATA/MSO'
years = list(range(2011, 2016))

for y in years:
    y_url = f'{BASE_URL}/?f=yes&id={PDS_ID}/{y}'

