#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

quota = data.getvalue('quota')

path = data.getvalue('path')

ip_namenode = data.getvalue("ip_namenode")

output = commands.getoutput("sudo hadoop dfsadmin -setSpaceQuota "+quota+" "+path)

print "<pre>"
if not output:
 print "Quota set successfull"
else:
 print output
print "</pre>"
