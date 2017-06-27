#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""


data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')

ip_details=[]

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:90px; width:1500px; background-image:url(data:image/jpg;base64,%s);background-size:120px;background-repeat: no-repeat;padding-left: 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px; background-color:black'>HDFS Cluster Status</li>"
print "</ul>"

ip_list=commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | awk '{print $1}'")

#ip_list=ip_list+"\n192.168.122.1\n"

while "\n" in ip_list:
  temp=ip_list[0:ip_list.index("\n")]
  
  ip_list=ip_list[ip_list.index("\n")+1:]
  
  #print "sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+temp+" lscpu| grep -i 'CPU(s):'|head -1 | cut -d: -f2"
  
  cpu_core=commands.getstatusoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+temp+" lscpu| grep -i 'CPU(s):'|head -1 | cut -d: -f2")
  
  os_ram=commands.getstatusoutput("sudo sshpass -p 'redhat' ssh root@"+temp+" cat /proc/meminfo| grep -i 'MemTotal:'| cut -d: -f2")
  
  ip_details.append((temp,cpu_core[1].strip(),os_ram[1].strip()))


print "<br>"

#IP of namenode--> Highest RAM

max_ram=sorted(ip_details,key=lambda x:x[2],reverse=True)[0]

ip_namenode=max_ram[0]
namenode_directory = "hadoopnamenode"


#core-site.xml
f=open("/tmp/core-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip_namenode+":10002</value>\n</property>\n</configuration>\n")

f.close()


#hdfs-site.xml
f=open("/tmp/hdfs-site.xml","w")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>dfs.data.dir</name>\n<value>/hadoopdatanode</value>\n</property>\n</configuration>\n")

f.close()


f=open("/tmp/.bashrc","w+")

f.write("# .bashrc\n\n# User specific aliases and functions\n\nalias rm='rm -i'\nalias cp='cp -i'\nalias mv='mv -i'\n\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n\t. /etc/bashrc\nfi\n\nJAVA_HOME=/usr/java/jdk1.7.0_79\nPATH=$JAVA_HOME/bin:$PATH\nexport PATH\n\n")

f.close()

for i in ip_details:
  
  #Install JDK, Hadoop
  os.system("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" yum install jdk -y")
  
  os.system("sudo sshpass -p 'redhat' scp /tmp/.bashrc root@"+i[0]+":/root/")
  
  #os.system("sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" rpm -ivh http://192.168.50.50/repo/rhel7rpm/hadoop-1.2.1-1.x86_64.rpm --replacefiles")
  
  os.system("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" rpm -ivh http://192.168.122.1/repo/rhel7rpm/hadoop-1.2.1-1.x86_64.rpm --replacefiles")
  
  
  #JAVA path set
  commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" JAVA_HOME=/usr/java/jdk1.7.0_79")
  
  #Core-site.xml of all nodes
  commands.getoutput("sudo sshpass -p 'redhat' scp /tmp/core-site.xml root@"+i[0]+":/etc/hadoop ")
  
  #Hdfs-site.xml of all nodes
  commands.getoutput("sudo sshpass -p 'redhat' scp /tmp/hdfs-site.xml root@"+i[0]+":/etc/hadoop ")
  
  commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" hadoop-daemon.sh stop datanode")
  
  commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" hadoop-daemon.sh stop namenode")


#Namenode hdfs-site.xml
f=open("/tmp/hdfs-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>dfs.name.dir</name>\n<value>/"+namenode_directory+"</value>\n</property>\n</configuration>\n")

f.close()

commands.getoutput("sudo sshpass -p 'redhat' scp /tmp/hdfs-site.xml root@"+ip_namenode+":/etc/hadoop ")

#Namenode format, start
commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" rm -rf /"+namenode_directory)

commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" hadoop namenode -format")

commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" hadoop-daemon.sh start namenode")


#Datanodes start 
print "<br>"

for i in ip_details:
 
 if i[0] != ip_namenode:
  commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" rm -rf /hadoopdatanode")
  
  commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" hadoop-daemon.sh start datanode")

print "HDFS Cluster setup successful"

print "<META HTTP-EQUIV='refresh' content='0; url=dfsadmin_report'/>"


