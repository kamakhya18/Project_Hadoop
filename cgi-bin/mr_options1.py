#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

ip_namenode=data.getvalue("ip_namenode")

f=open("/etc/hadoop/core-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip_namenode+":10002</value>\n</property>\n</configuration>\n")

f.close()

print "<form action='../cgi-bin/hdfs_options2.py'>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='jobs'> Create Directory"
print "<br>"
print "<br>"
print "<br>"
print "<input name='ip_namenode' type='hidden' value="+ip_namenode+">"
print "<input type='submit' value='submit'>"
print "</form>"


