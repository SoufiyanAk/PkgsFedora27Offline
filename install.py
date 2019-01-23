import subprocess
import var
import sys
sys.path.insert(0, 'Cop')
import cp
sys.path.insert(0, 'samba')
import er
import os
choice = 0
class bcolors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    ENDC = '\033[0m'
    FAIL = '\033[91m'
if cp.fn2ver == var.fn and cp.ln2ver == var.ln and er.fn2ver2 == var.fn:  
	

    print bcolors.OKBLUE + "\n \n Packages Fedora 27 \n" + bcolors.ENDC
    print('1 - Service BIND \n')
    print('2 - Service DHCP\n')
    print('3 - Service OPENLDAP\n')
    print('4 - Service vsftpd\n')
    print('5 - Service Postfix (MC + POSTFIX + DOVECOT + MAILX)\n')
    print('6 - Service LAMP (HTTPD + MYSQL + PHP + PHPMYADMIN)\n')
    print('7 - Service OPENSSH\n')
    print('8 - Service TELNET\n') 
    print('9 - Service SAMBA\n')
    print('10 - Service NFS\n')
    print('11 - Service Vertualisation KVM\n')
    print('12 - About\n')
    print('13 - Quit\n') 
    choice = int(input('Enter your choice (Only Service Number): '))
else : 
	print bcolors.FAIL + "\n ERROR : The property rights have been tampered with , this is a Open Source script there is no need to edit property right  \n" + bcolors.ENDC
if (choice == var.a):
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "bind.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** BIND SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output
    
elif (choice == var.l):
 print(var.pnt)
 var.ch = var.ck
 print (var.tl)
 print (var.cr + " " + var.fn + " " + var.ln)
 print (var.dt)
 print (var.em)
 print (var.inf)
 print(var.pnt)
 

elif (choice == var.d):
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "dhcp.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** DHCP SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output
 
elif (choice == var.b):
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["rpm", "-ivh", "openldap/openldap-2.4.45-4.fc27.x86_64.rpm" , "--force"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    p = subprocess.Popen(["rpm", "-ivh", "openldap/openldap-clients-2.4.45-4.fc27.x86_64.rpm" , "openldap/openldap-servers-2.4.45-4.fc27.x86_64.rpm"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** OPENLDAP SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output

elif (choice == var.c):
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["rpm", "-ivh", "vsftp/ftp-0.17-75.fc27.x86_64.rpm" , "vsftp/vsftpd-3.0.3-8.fc27.x86_64.rpm"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** VSFTPD SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output  
elif (choice == var.e):
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["rpm", "-ivh", "postfix/postfix-3.2.6-1.fc27.x86_64.rpm" , "postfix/mc/mc-4.8.19-7.fc27.x86_64.rpm" , "postfix/mc/gpm-libs-1.20.7-10.fc26.x86_64.rpm" , "postfix/mailx/mailx-12.5-25.fc27.x86_64.rpm" , "postfix/dovecot/dovecot-2.2.36-1.fc27.x86_64.rpm" , "postfix/dovecot/clucene-core-2.3.3.4-29.20130812.e8e3d20git.fc27.x86_64.rpm"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** POSTFIX SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output

elif (choice == var.f):
	
	
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "httpd.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** HTTPD SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "php.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    p = subprocess.Popen(["rpm", "-ivh", "lamp/php/nginx-filesystem-1.12.1-1.fc27.noarch.rpm" , "lamp/php/php-fpm-7.1.23-1.fc27.x86_64.rpm"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** PHP7 SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output 
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "mysql.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** MYSQL/MARIADB SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "phpmyadmin.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** PHPMYADMIN SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output
    
     

 
elif (choice == var.h):
	
	print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
	print "*** OPENSSH SERVICE INSTALLATION SUCCESSFUL***\n"

elif (choice == var.g):
	
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["rpm", "-ivh", "telnet/telnet-server-0.17-72.fc27.x86_64.rpm"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print bcolors.OKGREEN + "*** TELNET SERVICE INSTALLATION SUCCESSFUL ***\n" + bcolors.ENDC , output

elif (choice == var.i):
	
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "samba.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print "*** SAMBA SERVICE INSTALLATION SUCCESSFUL ***\n", output

elif (choice == var.m):
	print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
	print "*** NFS SERVICE INSTALLATION SUCCESSFUL***\n"

elif (choice == var.j):
	
    
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "libvirt.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print "*** LIBVIRT SERVICE INSTALLATION SUCCESSFUL ***\n", output
    print bcolors.WARNING + "\n Please wait for a while ...\n" + bcolors.ENDC
    p = subprocess.Popen(["bash", "qemu-kvm.sh"], stdout=subprocess.PIPE)
    output, err = p.communicate()
    print "*** QEMU-KVM SERVICE INSTALLATION SUCCESSFUL ***\n", output  


elif (choice == var.k):
 quit()
else:
    print bcolors.FAIL + "\n Invalid Choice\n" + bcolors.ENDC
    

