#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

state = data.getvalue("state")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"

if state == "Enable":
 value="true"

else:
 value="false"


print commands.getoutput("sudo sshpass -p 'redhat' scp root@"+ip_namenode+":/etc/hadoop/hdfs-site.xml /tmp/hdfs-site1.xml")

f = open("/tmp/hdfs-site1.xml","r+")
temp = f.read()
temp = temp.replace("</configuration>","\n<property>\n<name>dfs.permissions</name>\n<value>"+value+"</value>\n</property>\n</configuration>\n")
f.close()

f = open("/tmp/hdfs-site1.xml","w+")
f.write(temp)
f.close()

commands.getoutput("sudo sshpass -p 'redhat' scp /tmp/hdfs-site1.xml root@"+ip_namenode+":/etc/hadoop/hdfs-site.xml")

commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" hadoop dfsadmin -refreshNodes")

commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" hadoop-daemon.sh stop namenode")

status = commands.getstatusoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+"  hadoop-daemon.sh start namenode")

if status[0] == 0:
 if value == "true":
  print "Permission Checking Enabled"
 else:
  print "Permission Checking Disabled"

print "</pre>"
