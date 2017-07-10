#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
ip_namenode= data.getvalue('ip_namenode')
option = data.getvalue('hdfs_option')




