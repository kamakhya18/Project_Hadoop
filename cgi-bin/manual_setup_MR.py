#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()

data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')
#img_tag = '<img src="data:image/jpg;base64,%s">' % data_uri

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

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../cgi-bin/hive_cluster.py'>HIVE</a></li>"

print "<li style='float:right'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../about.html'>ABOUT</a></li>"

print "</ul>"

print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1

print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px;  postion:fixed; background-color:royalblue;'>Manual Setup of MR Cluster</li>"
print "</ul>"

ip_details=[]
commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | awk '{print $1}' > /tmp/ip_list")

#commands.getoutput("sudo echo '192.168.122.1\n'>> /tmp/ip_list")

commands.getoutput("sudo cp /tmp/ip_list /tmp/inventory")

commands.getoutput("sudo chmod 777 /tmp/inventory")

print "<br>"

ip_list_file=open('/tmp/ip_list','r')
ip_list=ip_list_file.read()
ip_list=ip_list.split();

if len(ip_list)>0:
 print "<br>"
 print "<br>"
 
 print "<form action='manual_setup_start_MR.py' method='POST'>"
 
 for temp in ip_list:
  
  cpu_core=commands.getstatusoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+temp+" lscpu| grep -i 'CPU(s):'|head -1 | cut -d: -f2")
  
  os_ram=commands.getoutput("sudo sshpass -p 'redhat' ssh root@"+temp+" cat /proc/meminfo| grep -i 'MemTotal:'| cut -d: -f2")
  
  os_ram=os_ram.strip()
  os_ram=os_ram[:-3]
  os_ram=int(os_ram) / 1024 / 1024 
  os_ram = os_ram + 1
  os_ram = str(os_ram)
  
  ip_details.append((temp,cpu_core[1].strip(),os_ram))
  
  jps = commands.getoutput("sudo sshpass -p 'redhat' ssh root@"+temp+" jps")
  
  if "NameNode" in jps:
   ip_namenode = temp
 
 #print ip_namenode
 
 print "<font size='6' style='margin:0px; display: block; color: white;margin-left:700px;padding: 14px 16px;text-decoration: none; width:1500px;'><i>Select jobtracker</i></font>"
 
 print "<pre>"
 print "<font style='color:white;' size='5'>"
 print "<i>"
 print "\t\tIP\t\t\tCPU\t\t\tRAM"
 print "<br>"
 for i in ip_details:
  print "\t<input type='radio' name='jobtracker' checked='checked' value="+i[0]+">"+i[0] + "\t\t\t" + i[1] + "\t\t\t"+ i[2]
 print "</i>"
 print "</font>"
 print "</pre>"
 
 print "<input type='hidden' name='namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 
 print "</form>" 

else:
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<font size='8' style='border: none;color: white; position:fixed; margin-left: 800px;'>"
 print "No IP scanned"
 print "</font>" 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
print "<a href='manual_setup_MR.py'>"
print "<img src='data:image/jpg;base64,%s' style='width:100px; height:100px; margin-left: 1000px;'>" % data_uri2
print "</a>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "</div>"

