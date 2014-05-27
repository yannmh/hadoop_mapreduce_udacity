#!/usr/bin/python

import sys
import csv

userInfo = []
currentKey = None

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store
reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
    if len(line)==6:
        user_ptr_id,aString,reputation,gold,silver,bronze = line
        currentKey=int(user_ptr_id)
        userInfo=[reputation,gold,silver,bronze]

    if len(line)==10:
        author_id,bString,id_m,title,tagnames,node_type,parent_id,abs_parent_id,added_at,score = line
        thisKey=int(author_id)
        if thisKey==currentKey:
            postInfo=[id_m,title,tagnames,author_id,node_type,parent_id,abs_parent_id,added_at,score]
            entry=postInfo+userInfo
            writer.writerow(entry)