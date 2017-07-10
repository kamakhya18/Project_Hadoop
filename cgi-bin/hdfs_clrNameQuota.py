#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

path = data.getvalue('path')

ip_namenode = data.getvalue("ip_namenode")

output = commands.getoutput("sudo hadoop dfsadmin -clrQuota "+path)

print "<pre>"
if not output:
 print "Quota Cleared"
else:
 print output
print "</pre>"
