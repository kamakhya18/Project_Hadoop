#!/usr/bin/python

import os,time,string,sys,commands,getpass

print "Content-type:text/html"
print ""

data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')
#img_tag = '<img src="data:image/jpg;base64,%s">' % data_uri

data_uri1 = open('bigdata1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri2 = open('refresh.jpg', 'rb').read().encode('base64').replace('\n', '')

print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:4100px;background-repeat: no-repeat; width:2000px; height:2500px;">' % data_uri1

#back_img='<div style="background-image:url(data:image/jpg;base64,%s);">' % data_uri

#data_uri1 = open('background_man2.jpg', 'rb').read().encode('base64').replace('\n', '')

#print img_tag

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:90px; width:1500px; background-image:url(data:image/jpg;base64,%s);background-size:120px;background-repeat: no-repeat;padding-left: 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

#print '<div style="background-image:url(data:image/jpg;base64,%s);background-size:1550px;background-repeat: no-repeat; width:2000px; height:800px;">' % data_uri1


print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px; background-color:#6495ED;'>Manual Setup of Map Reduce Cluster</li>"
print "</ul>"

ip_details=[]
ip_list=commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | awk '{print $1}'")
#for i in range(255)[1:]:

print "<br>"

if len(ip_list)>3:
 #ip_list=ip_list+"\n192.168.122.1\n"
 
 print "<form action='manual_setup_start_MR.py'>"
 
 while "\n" in ip_list:
  temp=ip_list[0:ip_list.index("\n")]
  
  ip_list=ip_list[ip_list.index("\n")+1:]
  
  #print "sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+temp+" lscpu| grep -i 'CPU(s):'|head -1 | cut -d: -f2"
  
  cpu_core=commands.getstatusoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+temp+" lscpu| grep -i 'CPU(s):'|head -1 | cut -d: -f2")
  
  os_ram=commands.getstatusoutput("sudo sshpass -p 'redhat' ssh root@"+temp+" cat /proc/meminfo| grep -i 'MemTotal:'| cut -d: -f2")
  
  ip_details.append((temp,cpu_core[1].strip(),os_ram[1].strip()))
   
 print "<font size='5' style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1500px;'>Select Namenode</font>"
 
 print "<pre>"
 print "<font style='color:white;' size='6'>"
 print "<i>"
 print "<br>"
 print "\tIP\t\t\t\tCPU\t\t\t\tRAM"
 print "<br>"
 for i in ip_details:
  print "<input type='radio' name='namenode' checked='checked' value="+i[0]+">"+i[0] + "\t\t\t\t" + i[1] + "\t\t\t\t"+ i[2]
  print "<br>"
  print "<br>"
 print "</i>"
 print "</font>"
 print "</pre>"
 
 print "<font size='5' style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1500px;'>Select Jobtracker</font>"
 print "<pre>"
 print "<font style='color:white;' size='6'>"
 print "<i>"
 print "<br>"
 print "\tIP\t\t\t\tCPU\t\t\t\tRAM"
 print "<br>"
 for i in ip_details:
  print "<input type='radio' name='jobtracker' checked='checked' value="+i[0]+">"+i[0] + "\t\t\t\t" + i[1] + "\t\t\t\t"+ i[2]
  print "<br>"
  print "<br>"
 print "</i>"
 print "</font>"
 print "</pre>"

 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='text' placeholder='Enter directory name' name='namenode_directory' style='border: none; border-bottom: 2px solid white; background-color: black;color: white; text-align:center; margin-left:450px;'>"

 for i in ip_details:
  
  commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" iptables -F")
  
  commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i[0]+" setenforce 0")

 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='submit' value='Continue' style='background-color:black; color:white; margin-left:530px;'>"
 
 print "</form>" 

else:
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<font size='8' style='border: none;color: white; margin-left:500px;'>"
 print "No IP scanned"
 print "</font>" 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<a href='manual_setup_MR.py'>"
print "<img src='data:image/jpg;base64,%s' style='width:100px; height:100px; margin-left:560px;'>" % data_uri2
print "</a>"
print "</div>"

