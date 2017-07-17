#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""


print "<html>"
print "<head>"
print "<title>Hadoop</title>"
print "<link rel='stylesheet' type='text/css' href='login.css/>"
print "</head>"
print "<body>"


data_uri5 = open('../../html/css/css1/person.jpg', 'rb').read().encode('base64').replace('\n', '')
data_uri6 = open('../../html/css/css1/contact.png', 'rb').read().encode('base64').replace('\n', '')

print "<div style='background-color:black;'>"
print "<ul>"
print "<li style='float:left;'><font size='6'><b style='color:white;'><i>Hadoop</i></b></font></li>"
print "<li><a href='#'><img src='data:image/png;base64,%s' width='25px' style='background-color:white;'></a></li>" %data_uri6
print "<div class='dropdown' >"
print "<button class='dropbtn'><img src='data:image/jpg;base64,%s' width='30px'></button>" %data_uri5
print "<div class='dropdown-content'>"
print "<a href='../../html/Hadoop1/login.html'>Log In</a>"
print "<a href='#'>Register</a>"
print "</div>"
print "</div>"
print "<li><a href='../../html/Hadoop1/index.html'>About</a></li>"
print "<li><a href='../../html/Hadoop1/index.html'>Home</a></li>"
print "<li><a href='hive_cluster.py'>Hive</a></li>"
print "<li><a href='mr_options1.py'>MR</a></li>"
print "<li><a href='hdfs_options1.py'>HDFS</a></li>"
print "<div class='dropdown' >"
print "<button class='dropbtn'>Cluster</button>"
print "<div class='dropdown-content'>"
print "<a href='../../html/Hadoop1/hdfs.html'>HDFS</a>"
print "<a href='../../html/Hadoop1/mr.html'>MR</a>"
print "<a href='../../html/Hadoop1/hive.html'>Hive</a>"
print "</div>"
print "</div>"
print "</ul>"
print "</div>"



data_uri = open('../../html/hadooplogo.png', 'rb').read().encode('base64').replace('\n', '')
#print '<img src="data:image/jpg;base64,%s">' % data_uri

data_uri1 = open('background1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri2 = open('refresh.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri3 = open('directory.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')


print "<div>"
print '<img width="2150vw" src="data:image/jpg;base64,%s">' % data_uri
print "</div>"

print '<div style="background-color:skyblue;background-image:url(data:image/jpg;base64,%s);background-size:3000px;">' % data_uri1

data=cgi.FieldStorage()

ip_namenode=data.getvalue("ip_namenode")

if not ip_namenode:
 ip_list = commands.getoutput("sudo arp-scan -I docker0 172.17.0.0/24 | grep 172 | awk '{print $1}'")
 ip_list = ip_list.split()
 for i in ip_list:
  jps = commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i+" jps ")
  if "NameNode" in jps:
   ip_namenode = i
   break
if not ip_namenode:
 print "NO HDFS Cluster found"
 print "<META HTTP-EQUIV='refresh' content='0; url=../../html/Hadoop1/hdfs.html'/>"

#print ip_namenode
commands.getoutput("sudo chmod 777 /etc/hadoop/core-site.xml")

f=open("/etc/hadoop/core-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip_namenode+":10002</value>\n</property>\n</configuration>\n")

f.close()

print "<form action='hdfs_options2.py' method='POST'>"
print "<font size='4' style='color:white'>"
print "<i>"
print "<br>"
print "<br>"
print "<div style='float:left;padding-left:400px;'>"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chown'> Change owner"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chmod'> Change permissions"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chport'> Change View Port of namenode"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chgrp'> Change group"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='chhbt'> Change Heartbeat Interval"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='fsck'> Check FileSystem"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='clr_name_quota'> Clear Name Quota"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='clr_space_quota'> Clear Space Quota"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='commission_nodes'> Commission Nodes"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='count'> Count"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='mkdir'> Create Directory"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='touchz'> Create File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='report'> Datanodes List"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='decommission_nodes'> Decommission Nodes"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='empty_trash'> Empty Trash"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='get_quota'> Get Name and Space Quota"
print "<br>"
print "<br>"
"""
print "<input type='radio'  name='hdfs_option' checked='checked' value='ha'> High Availablity"
print "<br>"
print "<br>"
"""
print "<input type='radio'  name='hdfs_option' checked='checked' value='ls'> List files"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='lsr'> List Recursively"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='metasave'> Metadata of namenode"
print "<br>"
print "<br>"
print "</div>"

print "<br>"
print "<br>"
print "<div style='float:right;padding-right:400px;'>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='mv'> Move File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='putf'> Overwrite File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='permissions'> Permission Checking"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='refresh_nodes'> Refresh Nodes"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='rmr'> Remove Directory"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='rm'> Remove File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='cmd'> Run other commands"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='safemode'> Safemode"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='snn'> Secondary Namenode"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='set_name_quota'> Set Name Quota"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='setrep'> Change Replication Factor"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='defrep'> Set default Replication Factor"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='defsize'> Set Default Block Size"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='set_space_quota'> Set Space Quota"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='du'> Size of file"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='dus'> Total size of all files"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='trash'> Trash"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='put'> Upload File"
print "<br>"
print "<br>"
print "<input type='radio'  name='hdfs_option' checked='checked' value='text'> View a file"
print "<br>"
print "<br>"
print "</div>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<input name='ip_namenode' type='hidden' value="+ip_namenode+">"
print "</i>"
print "</font>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "</form>"


