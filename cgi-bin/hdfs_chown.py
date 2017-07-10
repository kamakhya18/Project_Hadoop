#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

path=data.getvalue("path")

owner_name=data.getvalue("owner_name")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop fs -chown "+owner_name+" "+path)

if not output:
 print "Successfully changed owner"
else:
 print output
print "</pre>"
