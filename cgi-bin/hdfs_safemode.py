#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

state=data.getvalue("state")

ip_namenode=data.getvalue('ip_namenode')

print "<pre>"
output = commands.getoutput("sudo hadoop dfsadmin -safemode "+state)


print output
print "</pre>"
