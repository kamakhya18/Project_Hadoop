#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

file_name = data.getvalue("file_name")

rep_factor = data.getvalue("rep_factor")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"
output = commands.getoutput("sudo hadoop fs -setrep "+rep_factor+" "+file_name)

print output
print "</pre>"
