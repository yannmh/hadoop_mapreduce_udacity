#!/usr/bin/python

import sys

listIndex = []
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

    thisKey, thisIndex = data_mapped

    if thisIndex=="id":
        continue

    thisIndex = int(thisIndex)

    if oldKey and oldKey != thisKey:
        print oldKey, "\t", listIndex, "\t", len(listIndex)
        oldKey = thisKey;
        listIndex = []

    oldKey = thisKey
    listIndex.append(thisIndex)

if oldKey != None:
    print oldKey, "\t", listIndex,  "\t", len(listIndex)

