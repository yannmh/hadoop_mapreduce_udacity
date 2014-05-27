#!/usr/bin/python
import sys
import csv

def my_split(s, seps):
    res = [s]
    for sep in seps:
        s, res = res, []
        for seq in s:
            res += seq.split(sep)
    return res

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
def mapper():
	for line in reader:
	    id_m = line[0]
	    body = line[4]


	    all_words = my_split(body, [' ',',','.','!','?',':',';','"','(',')','<','>','[',']','#','$','=','-','/'])
	    for word in all_words:
	    	if len(word)>1:
	    		print "{0}\t{1}".format(word.lower(), id_m)


def main():
    try:
        mapper()
    except:
        pass

main()