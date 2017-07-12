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

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../login.html'>LOG IN</a></li>"

print "<li style='float:right'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../about.html'>ABOUT</a></li>"

print "</ul>"

print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1


data=cgi.FieldStorage()

ip_namenode=data.getvalue("ip_namenode")

ip_jobtracker = data.getvalue("ip_jobtracker")

if not ip_namenode:
 ip_list = commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | awk '{print $1}'")
 ip_list = ip_list.split()
 for i in ip_list:
  jps = commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i+" jps ")
  if "NameNode" in jps:
   ip_namenode = i
   break

#print ip_namenode

if not ip_jobtracker:
 ip_list = commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | awk '{print $1}'")
 ip_list = ip_list.split()
 for i in ip_list:
  jps = commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i+" jps ")
  if "JobTracker" in jps:
   ip_jobtracker = i
   break

f=open("/etc/hadoop/core-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip_namenode+":10002</value>\n</property>\n</configuration>\n")

f.close()

f=open("/etc/hadoop/mapred-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>"+ip_jobtracker+":9001</value>\n</property>\n</configuration>\n")

f.close()

print "<form action='../cgi-bin/mr_options2.py' method='POST'>"
print "<font size='4' style='color:white'>"
print "<i>"
print "<br>"
print "<br>"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='list'> Running Jobs"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='all'> All Jobs"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='tasktrackers'> Tasktrackers"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='status'> Status of a job"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='kill'> Kill a job"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='submit'> Submit A Job"
print "<br>"
print "<br>"
print "<br>"
print "<input name='ip_namenode' type='hidden' value="+ip_namenode+">"
print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
print "<br>"
print "<br>"
print "<br>"
print "</i>"
print "</font>"
print "</form>"
print "</div>"
