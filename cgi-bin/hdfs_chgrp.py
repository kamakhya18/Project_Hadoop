#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

path=data.getvalue("path")

grp_name=data.getvalue("grp_name")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop fs -chgrp "+grp_name+" "+path)

if not output:
 print "Successfully changed group"
else:
 print output
print "</pre>"
