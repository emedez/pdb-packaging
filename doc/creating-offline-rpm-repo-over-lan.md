Introduction
============

This document describes the steps for creating an offline RPM repository
over LAN.


Steps
=====


## 1. Install a local apache webserver.

[root@server1 ~]# yum install httpd

By default, package will set up a website uder /var/www/html on your
system.  For our purposes, that's fine, so there's no reason to do 
anything more.  You can easily test it by pointing your favorite browser 
at http://server1.  


## 2. First create directory structure on the server:

[root@server1 ~]# mkdir -p /www/var/html/CentOS/6/i386/RPMS


## 3. If createrepo is not already installed, as it will not be by default,
install it.

[root@server1 ~]# yum install createrepo


## 4. Build a new set of packages from foo-1.2.3.4-1.el4.src.rpm (or alternately
get packages from another trusted source).

[builduser@server1 ~]$ rpmbuild --rebuild /path/to/srpm/foo-1.2.3.4-1.el4.src.rpm

This creates (for example):

/home/builduser/rpmbuild/RPMS/foo-1.2.3.4-1.el4.i386.rpm
/home/builduser/rpmbuild/RPMS/foo-devel-1.2.3.4-1.el4.i386.rpm
/home/builduser/rpmbuild/RPMS/foo-docs-1.2.3.4-1.el4.i386.rpm


## 5. Move the files to the repo and create metadata:

[root@server1 ~]# mv /home/builduser/rpmbuild/RPMS/foo* \
    /var/www/html/CentOS/6/i386/RPMS
[root@server1 ~]# createrepo --database /var/www/html/CentOS/6/i386/RPMS

Note: Steps 3 and 4 are repeated as new packages are added to the repo.


## 6. Create /etc/yum.repos.d/local.repo

[local]
name=CentOS-$releasever - local packages for $basearch
baseurl=http://server1/CentOS/6/i386/RPMS/
enabled=1
gpgcheck=0


## 7. Install packages on the server to test the repo. Can be removed later
if not required on server.

[root@server1 ~]# yum install foo foo-devel foo-docs



