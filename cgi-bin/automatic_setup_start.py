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

#IP of namenode--> Highest RAM

ip_list_file=open('/tmp/ip_list','r')
ip_list=ip_list_file.read()
ip_list=ip_list.split();

ip_details=[]

for temp in ip_list:
   
  cpu_core=commands.getstatusoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+temp+" lscpu| grep -i 'CPU(s):'|head -1 | cut -d: -f2")
  
  os_ram=commands.getoutput("sudo sshpass -p 'redhat' ssh root@"+temp+" cat /proc/meminfo| grep -i 'MemTotal:'| cut -d: -f2")
  
  os_ram=os_ram.strip()
  os_ram=os_ram[:-3]
  os_ram=int(os_ram) / 1024 / 1024 
  os_ram = os_ram + 1
  os_ram = str(os_ram)
  
  ip_details.append((temp,cpu_core[1].strip(),os_ram))

max_ram=sorted(ip_details,key=lambda x:x[2],reverse=True)[0]

ip_namenode=max_ram[0]
namenode_directory = "hadoopnamenode"

#Inventory file

inventory=open('/tmp/inventory','r+')

temp_in = inventory.read()

inventory.close()

temp_in = temp_in.replace(ip_namenode+"\n","\n")

inventory=open('/tmp/inventory','w+')

inventory.write("[namenode]\n"+ip_namenode+"\n\n[datanode]\n")

inventory.write(temp_in)

inventory.seek(0)

inventory.close()

#core-site.xml
f=open("/tmp/core-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip_namenode+":10002</value>\n</property>\n</configuration>\n")

f.close()


#Namenode hdfs-site.xml
f=open("/tmp/hdfs-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/"+namenode_directory+"</value>\n</property>\n</configuration>\n")

f.close()


#.bashrc
f=open("/tmp/.bashrc","w+")

f.write("# .bashrc\n\n# User specific aliases and functions\n\nalias rm='rm -i'\nalias cp='cp -i'\nalias mv='mv -i'\n\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n\t. /etc/bashrc\nfi\n\nJAVA_HOME=/usr/java/jdk1.7.0_79\nHIVE_PREFIX=/hive\nPATH=$JAVA_HOME/bin:$HIVE_PREFIX/bin:$PATH\nexport PATH\n\n")

f.close()

commands.getoutput("sudo ansible-playbook -i /tmp/inventory all.yml")

commands.getoutput("sudo ansible-playbook -i /tmp/inventory namenode.yml")

#hdfs-site.xml
f=open("/tmp/hdfs-site.xml","w")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/hadoopdatanode</value>\n</property>\n</configuration>\n")

f.close()

commands.getoutput("sudo ansible-playbook -i /tmp/inventory datanode.yml")

print "HDFS Cluster setup successful"

print "<form action='../cgi-bin/dfsadmin_report' method='POST'>"
print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
print "<input type='submit' value='Continue'>"
print "</form>"

print "<META HTTP-EQUIV='refresh' content='0; url=hdfs_options1.py'/>"
