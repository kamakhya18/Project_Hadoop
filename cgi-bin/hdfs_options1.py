#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri1 = open('background1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri2 = open('refresh.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri3 = open('directory.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:50px; width:2000px; background-image:url(data:image/jpg;base64,%s);background-size:170px;background-repeat: no-repeat; postion:fixed; padding:40px 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print "<ul style='list-style-type: none; margin: 0; padding: 0; overflow: hidden; background-color: #333;'>"
print "<li style='float: left;'><a href='../index.html' style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;'>HOME</a></li>"

print "<li style='float: left;'><a  style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../hdfs_cluster.html'>HDFS</a></li>"

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../mr_cluster.html'>Map Reduce</a></li>"

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../hive_cluster.py'>HIVE</a></li>"

print "<li style='float:right'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../about.html'>ABOUT</a></li>"

print "</ul>"

print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1

data=cgi.FieldStorage()

ip_namenode=data.getvalue("ip_namenode")

if not ip_namenode:
 ip_list = commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | awk '{print $1}'")
 ip_list = ip_list.split()
 for i in ip_list:
  jps = commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i+" jps ")
  if "NameNode" in jps:
   ip_namenode = i
   break

#print ip_namenode

f=open("/etc/hadoop/core-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip_namenode+":10002</value>\n</property>\n</configuration>\n")

f.close()

print "<form action='../cgi-bin/hdfs_options2.py' method='POST'>"
print "<font size='4' style='color:white'>"
print "<i>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='mkdir'> Create Directory"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='put'> Upload File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='mv'> Move File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='ls'> List of files"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='text'> View a file"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='touchz'> Create File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='rmr'> Remove Directory"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='rm'> Remove File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='count'> Count"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='lsr'> List Recursively"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='setrep'> Set Replication Factor"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chown'> Change owner"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chmod'> Change permissions"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chgrp'> Change group"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='safemode'> Safemode"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='set_space_quota'> Set Space Quota"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='clr_space_quota'> Clear Space Quota"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='set_name_quota'> Set Name Quota"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='clr_name_quota'> Clear Name Quota"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='report'> Datanodes List"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='refresh_nodes'> Refresh Nodes"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='commission_nodes'> Commission Nodes"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='decommission_nodes'> Decommission Nodes"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='du'> Size of file"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='dus'> Total size of all files"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='fsck'> Check FileSystem"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='permissions'> Permission Checking"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='cmd'> Run other commands"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<input name='ip_namenode' type='hidden' value="+ip_namenode+">"
print "</i>"
print "</font>"
print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
print "<br>"
print "<br>"
print "<br>"
print "</form>"


