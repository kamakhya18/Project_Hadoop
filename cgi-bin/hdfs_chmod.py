#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

path=data.getvalue("path")

permissions=data.getvalue("permissions")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop fs -chmod "+permissions+" "+path)

if not output:
 print "Successfully changed permissions"
else:
 print output
print "</pre>"
