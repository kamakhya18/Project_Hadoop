#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

dir_name=data.getvalue("dir_name")

ip_namenode=data.getvalue('ip_namenode')


print "<pre>"
output = commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" hadoop fsck "+dir_name+" -files")

if not output:
 print "Successfully uploaded file"
else:
 print output
print "</pre>"
