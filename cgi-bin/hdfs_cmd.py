#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

command=data.getvalue("command")

ip_namenode=data.getvalue('ip_namenode')
 

print "<pre>"

output = commands.getoutput("sudo "+command)

if not output:
 print "Successfully executed command"
else:
 print output
print "</pre>"
