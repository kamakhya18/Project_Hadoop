#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

file_src=data.getvalue("file_src")

file_dest=data.getvalue("file_dest")

print "<pre>"
output = commands.getoutput("sudo hadoop fs -put "+file_src+" "+file_dest)

if not output:
 print "Successfully created directory"
else:
 print output
print "</pre>"
