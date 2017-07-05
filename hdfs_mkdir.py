#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

directory_name=data.getvalue("directory_name")

print "<pre>"
x = commands.getoutput("sudo hadoop fs -mkdir "+directory_name)

if not x:
 print "Successfully created directory"
else:
 print x
print "</pre>"
