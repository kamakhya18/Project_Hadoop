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
print "<input type='radio'  name='hdfs_option' checked='checked' value='mkdir'> Create Directory"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='put'> Upload File"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='mv'> Move File"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='ls'> List of files"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='text'> View a file"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='touchz'> Create File"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='rmr'> Remove Directory"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='rm'> Remove File"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='count'> Count"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='lsr'> List Recursively"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='setrep'> Set Replication Factor"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chown'> Change owner"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chmod'> Change permissions"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chgrp'> Change group"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='safemode'> Safemode"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='set_space_quota'> Set Space Quota"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='clr_space_quota'> Clear Space Quota"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='set_name_quota'> Set Name Quota"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='clr_name_quota'> Clear Name Quota"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='report'> Datanodes List"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='refresh_nodes'> Refresh Nodes"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='commission_nodes'> Commission Nodes"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='decommission_nodes'> Decommission Nodes"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='du'> Size of file"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='dus'> Total size of all files"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='fsck'> Check FileSystem"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='permissions'> Permission Checking"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='cmd'> Run other commands"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='mr'> Perform MR Operations"
print "<br>"
print "<br>"
print "<br>"
print "<input name='ip_namenode' type='hidden' value="+ip_namenode+">"
print "<input type='submit' value='submit'>"
print "</form>"


