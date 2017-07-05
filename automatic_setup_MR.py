#!/usr/bin/python

import os,time,string,sys,commands,getpass

print "Content-type:text/html"
print ""

data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')
#img_tag = '<img src="data:image/jpg;base64,%s">' % data_uri

data_uri1 = open('background1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri2 = open('refresh.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')

print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:50px; width:2000px; background-image:url(data:image/jpg;base64,%s);background-size:170px;background-repeat: no-repeat; postion:fixed; padding:40px 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px;  postion:fixed; background-color:royalblue;'>Automatic Setup of Map Reduce Cluster</li>"
print "</ul>"

ip_details=[]
commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | awk '{print $1}' > /tmp/ip_list")

commands.getoutput("sudo echo '192.168.122.1\n'>> /tmp/ip_list")

commands.getoutput("sudo cp /tmp/ip_list /tmp/inventory")

commands.getoutput("sudo chmod 777 /tmp/inventory")

print "<br>"

ip_list_file=open('/tmp/ip_list','r')
ip_list=ip_list_file.read()
ip_list=ip_list.split();

if len(ip_list)>0:
 print "<br>"
 print "<br>"
 print "<font size='6' style='margin:0px; display: block; color: white;margin-left:700px;padding: 14px 16px;text-decoration: none; width:1500px;'><i>Scanned IPs</i></font>"
 
 print "<form action='automatic_setup_start_MR.py' method='POST'>"
 
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
  print "\t"+i[0] + "\t\t\t" + i[1] + "\t\t\t"+ i[2]
 print "</i>"
 print "</font>"
 print "</pre>"

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
print "<br>"
print "<br>"
print "<a href='automatic_setup_MR.py'>"
print "<img src='data:image/jpg;base64,%s' style='width:100px; height:100px; margin-left: 1000px;'>" % data_uri2
print "</a>"
print "<br>"
print "</div>"

