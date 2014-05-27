#!/usr/bin/python

import sys

saleMax = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped
    thisSale=float(thisSale)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", saleMax
        oldKey = thisKey;
        saleMax = 0

    oldKey = thisKey
    saleMax = thisSale if thisSale>saleMax else saleMax 

if oldKey != None:
    print oldKey, "\t", saleMax

