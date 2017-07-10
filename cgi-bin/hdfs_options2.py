#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
ip_namenode= data.getvalue('ip_namenode')
option = data.getvalue('hdfs_option')


if option == "mkdir":
 print "<form action='../cgi-bin/hdfs_mkdir.py'>"
 
 print "<input type='text' placeholder='Enter directory name' name='directory_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<input type='submit' value='Done'>"
 print "</form>"

elif option == "put":
 print "<form action='../cgi-bin/hdfs_upload.py'>"
 
 print "<input type='text' placeholder='Enter file name' name='file_src' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Enter destination' name='file_dest' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Enter replication factor' name='block_rep' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Enter block size' name='block_size' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"


elif option == "mv":
 print "<form action='../cgi-bin/hdfs_cut.py'>"
 
 print "<input type='text' placeholder='Enter file name' name='file_src' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Enter destination' name='file_dest' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "ls":
 print "<form action='../cgi-bin/hdfs_ls.py'>"
 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "text":
 print "<form action='../cgi-bin/hdfs_cat.py'>"
 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"


elif option == "touchz":
 print "<form action='../cgi-bin/hdfs_touch.py'>"
 
 print "<input type='text' placeholder='Enter file name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"


elif option == "rm":
 print "<form action='../cgi-bin/hdfs_rmr.py'>"
 
 print "<input type='text' placeholder='Enter file name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"


elif option == "rmr":
 print "<form action='../cgi-bin/hdfs_rmdir.py'>"
 
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"


elif option == "count":
 print "<form action='../cgi-bin/hdfs_count.py'>"
 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "lsr":
 print "<form action='../cgi-bin/hdfs_lsr.py'>"
 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"


elif option == "setrep":
 print "<form action='../cgi-bin/hdfs_setrep.py'>"
 
 print "<input type='text' placeholder='Enter file name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Replication factor' name='rep_factor' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "chown":
 print "<form action='../cgi-bin/hdfs_chown.py'>"
 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Owner name' name='owner_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "chmod":
 print "<form action='../cgi-bin/hdfs_chmod.py'>"
 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Enter permissions' name='permissions' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "chgrp":
 print "<form action='../cgi-bin/hdfs_chgrp.py'>"
 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Group name' name='grp_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "cmd":
 print "<form action='../cgi-bin/hdfs_cmd.py'>"
 
 print "<input type='text' placeholder='Enter command' name='command' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "safemode":
 print "<form action='../cgi-bin/hdfs_safemode.py'>"
 
 print "Choose safemode state"
 print "<br>"
 
 print "<input type='radio' name='state' value='Enter'>Enter"
 print "<br>"
 
 print "<input type='radio' name='state' value='Leave'>Leave"
 print "<br>"
 
 print "<input type='radio' name='state' value='Get'>Get"
 print "<br>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "set_space_quota":
 print "<form action='../cgi-bin/hdfs_spaceQuota.py'>"
 
 print "<input type='text' placeholder='Enter quota' name='quota' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Enter directory name' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "clr_space_quota":
 print "<form action='../cgi-bin/hdfs_clrSpaceQuota.py'>"
 
 print "<input type='text' placeholder='Enter directory name' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "set_name_quota":
 print "<form action='../cgi-bin/hdfs_nameQuota.py'>"
 
 print "<input type='text' placeholder='Enter quota' name='quota' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='text' placeholder='Enter directory name' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "clr_name_quota":
 print "<form action='../cgi-bin/hdfs_clrNameQuota.py'>"
 
 print "<input type='text' placeholder='Enter directory name' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "du":
 print "<form action='../cgi-bin/hdfs_du.py'>"
 
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "dus":
 print "<form action='../cgi-bin/hdfs_dus.py'>"
 
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "decommission_nodes":
 print "<form action='../cgi-bin/hdfs_decommission.py'>"
 
 print "<input type='text' placeholder='Enter directory name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "commission_nodes":
 print "<form action='../cgi-bin/hdfs_commission.py'>"
 
 print "<input type='text' placeholder='Enter file name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "fsck":
 print "<form action='../cgi-bin/hdfs_fsck.py'>"
 
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "permissions":
 print "<form action='../cgi-bin/hdfs_permissions.py'>"
 
 print "<input type='radio' name='state' value='Enable'>Enable"
 
 print "<input type='radio' name='state' value='Disable'>Disable"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='submit'>"
 print "</form>"

elif option == "report":
 print "<form action='../cgi-bin/hdfs_report.py'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue'>"
 print "</form>"

elif option == "refresh_nodes":
 print "<form action='../cgi-bin/hdfs_refreshNodes.py'>"
 
 print "<input type='submit' value='Continue'>"
 print "</form>"

elif option=="mr":
 print "<form action='../cgi-bin/manual_setup_MR.py'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue'>"
 print "</form>"

elif option=="hive":
 print "<form action='../cgi-bin/hive_cluster.py'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue'>"
 print "</form>"

else:
 print option


