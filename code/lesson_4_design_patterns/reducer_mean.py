#!/usr/bin/python

import sys

salesTotal = 0
countSales = 0
oldKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # print "smthg went wrong"
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale, weight = data_mapped
    thisKey= int(thisKey)
    weight= int(weight)

    if oldKey and oldKey != thisKey:
        print "{0}\t{1}\t{2}".format(oldKey,salesTotal/countSales,countSales)
        # print oldKey, "\t", salesTotal/countSales, "\t", countSales
        oldKey = thisKey;
        salesTotal = 0
        countSales = 0

    oldKey = thisKey
    salesTotal += weight*float(thisSale)
    countSales += weight

if oldKey != None:
    print "{0}\t{1}\t{2}".format(oldKey,salesTotal/countSales,countSales)
    # print oldKey, "\t", salesTotal/countSales, "\t", countSales

