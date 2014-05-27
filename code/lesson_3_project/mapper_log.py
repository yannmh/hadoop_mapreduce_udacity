#!/usr/bin/python
import re
import sys

for line in sys.stdin:
    data = map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))
    if len(data) == 7:
        ip, identity, username, time, request, status, size = data
        detailled_request = request.split(" ")
        if len(detailled_request) !=3:
        	continue
        method, filename, http = detailled_request
        if filename.startswith("http://"):
        	filename=filename[31:]
        print "{0}".format(filename)
