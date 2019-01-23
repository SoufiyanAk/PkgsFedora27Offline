#!/bin/bash

#////////////////////////
#
#Title : Packages fedora 27
#Created by : EBF LEARN | SOAK
#Date : 30/12/2018
#Contact :  securcomix@gmail.com
#For More information ,read INFO file
#
#////////////////////////

#Note : Conflis packages do not delete --force

rpm -ivhe samba/libsmbclient-4.7.10-1.fc27.x86_64.rpm samba/libwbclient-4.7.10-1.fc27.x86_64.rpm samba/samba-4.7.10-1.fc27.x86_64.rpm samba/samba-client-4.7.10-1.fc27.x86_64.rpm samba/samba-client-libs-4.7.10-1.fc27.x86_64.rpm samba/samba-common-4.7.10-1.fc27.noarch.rpm samba/samba-common-libs-4.7.10-1.fc27.x86_64.rpm samba/samba-common-tools-4.7.10-1.fc27.x86_64.rpm samba/samba-dc-libs-4.7.10-1.fc27.x86_64.rpm samba/samba-libs-4.7.10-1.fc27.x86_64.rpm --force
