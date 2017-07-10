#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

query = data.getvalue('query')

# query  = "create table xyz (id int, name string) row format delimited fields terminated by ':' location '/hello1'"

print commands.getoutput("sudo /hive/bin/hive -S -e \"use adhoc; "+query+";\"")



