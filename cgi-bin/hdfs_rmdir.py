#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

dir_name=data.getvalue("dir_name")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop fs -rmr "+dir_name)

if "Deleted" in output:
 print "Successfully deleted directory"
else:
 print output
print "</pre>"
