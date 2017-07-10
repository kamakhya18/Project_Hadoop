#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""


data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:90px; width:1500px; background-image:url(data:image/jpg;base64,%s);background-size:120px;background-repeat: no-repeat;padding-left: 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px; background-color:black'>HDFS Cluster Status</li>"
print "</ul>"

data=cgi.FieldStorage()

ip_namenode = data.getvalue('namenode')
namenode_directory = data.getvalue('namenode_directory')
ip_jobtracker=data.getvalue('jobtracker')

if not namenode_directory:
 namenode_directory="hadoopnamenode"

#Inventory file
inventory=open('/tmp/inventory','r+')

temp_in = inventory.read()

inventory.close()

temp = temp_in

temp_in = temp_in.replace(ip_namenode+"\n","\n")

inventory=open('/tmp/inventory','w+')

inventory.write("[namenode]\n"+ip_namenode+"\n\n[datanode]\n")

inventory.write(temp_in)

inventory.write("\n[jobtracker]\n"+ip_jobtracker+"\n\n[tasktracker]\n")

temp = temp.replace(ip_jobtracker+"\n","\n")

inventory.write(temp)

inventory.close()

commands.getoutput("sudo ansible-playbook -i /tmp/inventory all_mr.yml")


#mapred-site.xml
f=open("/etc/hadoop/mapred-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>"+ip_jobtracker+":9001</value>\n</property>\n</configuration>\n")

f.close()

commands.getoutput("sudo ansible-playbook -i /tmp/inventory jobtracker_mr.yml")

commands.getoutput("sudo ansible-playbook -i /tmp/inventory tasktracker_mr.yml")

print "Map Reduce Cluster setup successful"

#print "<META HTTP-EQUIV='refresh' content='1; url=mr_options1.py'/>"

print "<form action='../cgi-bin/mr_options1.py' method='POST'>"
print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
print "<input type='submit' value='Continue'>"
print "</form>"
#print "<META HTTP-EQUIV='refresh' content='0; url=dfsadmin_report'/>"
