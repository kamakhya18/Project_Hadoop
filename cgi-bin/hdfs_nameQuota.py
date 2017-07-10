#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

path=data.getvalue("path")

quota = data.getvalue("quota")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop dfsadmin -setQuota "+quota+" "+path)

if not output:
 print "Quota Set"
else:
 print output
print "</pre>"
