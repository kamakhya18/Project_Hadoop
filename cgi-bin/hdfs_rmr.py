#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

file_name = data.getvalue("file_name")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop fs -rm "+file_name)

if "Deleted" in output:
 print "Successfully deleted file"
else:
 print output
print "</pre>"
