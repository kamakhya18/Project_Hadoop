#!/usr/bin/python

import os,time,string,sys,commands,getpass

print "Content-type:text/html"
print ""

print "<head>"
print "<title>Hadoop</title>"
print "<link rel='stylesheet' type='text/css' href='./css/login.css'>"
print "</head>"
print "<body>"

data_uri5 = open('../html/css/person.jpg', 'rb').read().encode('base64').replace('\n', '')
data_uri6 = open('../html/css/contact.png', 'rb').read().encode('base64').replace('\n', '')

print "<ul>"
print "<li style='float:left;'><font size='6'><b style='color:white;'><i>Hadoop</i></b></font></li>"
print "<li><a href='contact.html'><img src='data:image/png;base64,%s' width='25px' style='background-color:white;'></a></li>" %data_uri6
print "<div class='dropdown' >"
print "<button class='dropbtn'><img src='data:image/jpg;base64,%s' width='30px'></button>" %data_uri5
print "<div class='dropdown-content'>"
print "<a href='login.html'>Log In</a>"
print "<a href='#'>Register</a>"
print "</div>"
print "</div>"
print "<li><a href='../index.html'>About</a></li>"
print "<li><a href='../index.html'>Home</a></li>"
print "<li><a href='../cgi-bin/hive_cluster.py'>Hive</a></li>"
print "<li><a href='../cgi-bin/mr_options1.py'>MR</a></li>"
print "<li><a href='../cgi-bin/hdfs_options1.py'>HDFS</a></li>"
print "<div class='dropdown' >"
print "<button class='dropbtn'>Cluster</button>"
print "<div class='dropdown-content'>"
print "<a href='../hdfs.html'>HDFS</a>"
print "<a href='../mr.html'>MR</a>"
print "<a href='../hive.html'>Hive</a>"
print "</div>"
print "</div>"
print "</ul>"

data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')
#img_tag = '<img src="data:image/jpg;base64,%s">' % data_uri

data_uri1 = open('background1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri2 = open('refresh.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri3 = open('directory.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')


print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1

print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px;  postion:fixed; background-color:royalblue;'>Manual Setup of HDFS Cluster</li>"
print "</ul>"

ip_details=[]
commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | grep -Ev '192.168.122.93' | awk '{print $1}' > /tmp/ip_list")

#commands.getoutput("sudo echo '192.168.122.1\n'>> /tmp/ip_list")

#commands.getoutput("sudo arp-scan -I docker0 172.17.0.0/24 | grep 172 | grep -Ev '172.17.0.5' | awk '{print $1}' > /tmp/ip_list")

commands.getoutput("sudo cp /tmp/ip_list /tmp/inventory")

commands.getoutput("sudo chmod 777 /tmp/inventory")

print "<br>"

ip_list_file=open('/tmp/ip_list','r')
ip_list=ip_list_file.read()
ip_list=ip_list.split();

if len(ip_list)>0:
 print "<br>"
 print "<br>"
 print "<font size='6' style='margin:0px; display: block; color: white;margin-left:700px;padding: 14px 16px;text-decoration: none; width:1500px;'><i>Select namenode</i></font>"
 
 print "<form action='manual_setup_start.py' method='POST'>"
 
 for temp in ip_list:
  
  cpu_core=commands.getstatusoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+temp+" lscpu| grep -i 'CPU(s):'|head -1 | cut -d: -f2")
  
  os_ram=commands.getoutput("sudo sshpass -p 'redhat' ssh root@"+temp+" cat /proc/meminfo| grep -i 'MemTotal:'| cut -d: -f2")
  
  os_ram=os_ram.strip()
  os_ram=os_ram[:-3]
  os_ram=int(os_ram) / 1024 / 1024 
  os_ram = os_ram + 1
  os_ram = str(os_ram)
  
  ip_details.append((temp,cpu_core[1].strip(),os_ram))
 
 print "<pre>"
 print "<font style='color:white;' size='5'>"
 print "<i>"
 print "\t\tIP\t\t\tCPU\t\t\tRAM"
 print "<br>"
 for i in ip_details:
  print "\t<input type='radio' name='namenode' checked='checked' value="+i[0]+">"+i[0] + "\t\t\t" + i[1] + "\t\t\t"+ i[2]
 print "</i>"
 print "</font>"
 print "</pre>"

 print "<br>"
 
 print "<input type='text' placeholder='Enter directory name' name='namenode_directory' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px;background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 20px;'>" %data_uri3
 
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
print "<a href='manual_setup.py'>"
print "<img src='data:image/jpg;base64,%s' style='width:100px; height:100px; margin-left: 1000px;'>" % data_uri2
print "</a>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "</div>"
print "</body>"

