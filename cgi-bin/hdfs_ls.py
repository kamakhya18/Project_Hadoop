#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

path=data.getvalue("path")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop fs -ls "+path)

if not output:
 print "Empty"
else:
 print output
print "</pre>"
