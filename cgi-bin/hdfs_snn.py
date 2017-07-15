#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
ip_namenode = data.getvalue("ip_namenode")
ip_snn = data.getvalue("ip_snn")


#core-site.xml
f=open("/tmp/core-site1.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip_namenode+":10002</value>\n</property>\n</configuration>\n")

f.close()



#core-site.xml
f=open("/tmp/hdfs-site1.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>dfs.http.address</name>\n<value>"+ip_namenode+":50070</value>\n</property>\n<property>\n<name>fs.checkpoint.edits.dir</name>\n<value>/data/edits</value>\n</property>\n<property>\n<name>dfs.secondary.http.address</name>\n<value>"+ip_snn+":50090</value>\n</property>\n<property>\n<name>fs.checkpoint.dir</name>\n<value>/data/check</value>\n</property>\n</configuration>\n")

f.close()



print commands.getoutput("sudo sshpass -p 'redhat' scp -o 'StrictHostKeyChecking no' /tmp/core-site1.xml root@"+ip_snn+":/etc/hadoop/core-site.xml")

print commands.getoutput("sudo sshpass -p 'redhat' scp -o 'StrictHostKeyChecking no' /tmp/hdfs-site1.xml root@"+ip_snn+":/etc/hadoop/hdfs-site.xml")

print commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_snn+" hadoop-daemon.sh start secondarynamenode ")

print commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_snn+" hadoop secondarynamenode -checkpoint force ")

