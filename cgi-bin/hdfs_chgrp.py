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
print "<font size='5'>"
if not output:
 print "Successfully changed group"
else:
 print output
print "</pre>"
print "</form>"
print "</div>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
