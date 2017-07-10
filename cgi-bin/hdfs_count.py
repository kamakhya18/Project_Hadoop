#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

path=data.getvalue("path")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"

no_of_dirs = commands.getoutput("sudo hadoop fs -count "+path+" | awk '{print $1}'")

no_of_files = commands.getoutput("sudo hadoop fs -count "+path+" | awk '{print $2}'")

"""
print file_or_dir

if file_or_dir == "directory" and no_of_dirs != 0:
 no_of_dirs = (int)(no_of_dirs) - 1

else:
 if no_of_files != 0:
  no_of_files = (int)(no_of_files) - 1

"""

print "No of files "+(str)(no_of_files)
print "No of directories "+str(no_of_dirs)

print "</pre>"
