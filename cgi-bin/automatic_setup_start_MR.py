#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""


data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:90px; width:1500px; background-image:url(data:image/jpg;base64,%s);background-size:120px;background-repeat: no-repeat;padding-left: 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px; background-color:black'>Manual Cluster Status</li>"
print "</ul>"

data=cgi.FieldStorage()

ip_namenode = data.getvalue('ip_namenode')

#IP of jobtracker--> Highest CPU

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

max_cpu=sorted(ip_details,key=lambda x:x[1],reverse=True)[0]

ip_jobtracker=max_cpu[0]

print "Ip of jobtracker "+ip_jobtracker

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

inventory.seek(0)

inventory.close()

commands.getoutput("sudo ansible-playbook -i /tmp/inventory all_mr.yml")


#mapred-site.xml
#print "Ip of jobtracker1 "+ip_jobtracker
f=open("/tmp/mapred-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>"+ip_jobtracker+":9001</value>\n</property>\n</configuration>\n")

#print "Ip of jobtracker2 "+ip_jobtracker
f.seek(0)
print f.read()

f.close()

print commands.getoutput("cat /tmp/inventory")

commands.getoutput("sudo ansible-playbook -i /tmp/inventory jobtracker_mr.yml")

commands.getoutput("sudo ansible-playbook -i /tmp/inventory tasktracker_mr.yml")

print "Map Reduce Cluster setup successful"


print "<form action='../cgi-bin/mr_options1.py' method='POST'>"
print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
print "<input type='submit' value='Continue'>"
print "</form>"

print "<META HTTP-EQUIV='refresh' content='0; url=mr_options1.py'/>"
