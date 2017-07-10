#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

file_src=data.getvalue("file_src")

file_dest=data.getvalue("file_dest")

ip_namenode=data.getvalue('ip_namenode')

block_rep = data.getvalue('block_rep')

block_size = data.getvalue('block_size')

if not block_size:
 block_size = '64'

if not block_rep:
 block_rep = 3


block_size = int(block_size) * 1024 * 1024

print "<pre>"
output = commands.getoutput("sudo hadoop fs -Ddfs.replication="+(str)(block_rep)+" -Ddfs.block.size="+str(block_size)+" -put "+file_src+" "+file_dest)

if not output:
 print "Successfully uploaded file"
else:
 print output
print "</pre>"
