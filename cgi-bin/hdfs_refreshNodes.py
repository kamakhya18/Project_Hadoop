#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop dfsadmin -refreshNodes ")

if not output:
 print commands.getoutput("sudo hadoop dfsadmin -report")
else:
 print output
print "</pre>"
