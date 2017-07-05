#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

option = data.getvalue('hdfs_option')


if option == "mkdir":
 print "<META HTTP-EQUIV='refresh' content='0; url=../hdfs_mkdir.html'/>"

elif option == "put":
 print "<META HTTP-EQUIV='refresh' content='0; url=../hdfs_upload.html'/>"

elif option == "mv"
 print "<META HTTP-EQUIV='refresh' content='0; url=../hdfs_cut.html'/>"

else:
 print option

