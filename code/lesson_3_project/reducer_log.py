#!/usr/bin/python

import sys

maxHits = 0
maxFile = None


nbHits = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip()

    thisKey = data_mapped

    if oldKey and oldKey != thisKey:
        # print oldKey, "\t", nbHits
        if nbHits>maxHits:
            maxHits=nbHits
            maxFile=oldKey
        oldKey = thisKey;
        nbHits = 0

    oldKey = thisKey
    nbHits += 1

if oldKey != None:
    # print oldKey, "\t", nbHits
    if nbHits>maxHits:
        maxHits=nbHits
        maxFile=oldKey

print maxFile, "\t", maxHits

