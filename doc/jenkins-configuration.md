Introduction
============

This documents describes the procedure on configuring a Jenkins CI server
for build automation of selected projects.

The following are the target projects for build automation:
*   python-int-overflow-check
    https://github.com/palominodb/python-int-overflow-check
*   mysql-params parameter tracker
    https://github.com/palominodb/mysql-params
*   couchbase query tool
    https://github.com/palominodb/palominodb-priv/tree/master/tools/couchbase/python-query

The following outlines the whole process:
1)  Create packages for dependencies that either do not exist on the standard
    repositories, or do exist but do not meet the required version.
2)  Collect built packages into custom repository that can be used for
    dependency resolution during installation.
3)  Create Amazon EC2 images which will be used by Jenkins CI server when
    building packages.
4)  Configure Jenkins CI server to use Amazon EC2 images for building packages.
5)  Configure jobs.


Building RPM/Debian packages for dependencies
=============================================

PalominoDB python projects have dependencies that are either non-existent
or does not have the required version on the standard repository.  We need
to build the individual RPM/Debian packages for these dependencies.

The RPM SPEC files needed for building RPM packages can be found here:
https://github.com/palominodb/palominodb-priv/tree/master/tools/packaging/SPECS

Refer to the following document for instruction on how to build RPM packages
using the RPM SPEC files:
https://github.com/palominodb/palominodb-priv/blob/master/tools/packaging/doc/configuring-a-dedicated-rpm-development-box.md

To build Debian packages, use the stdeb configuration files found here:
https://github.com/palominodb/palominodb-priv/tree/master/tools/packaging/stdeb

Refer to the following document for instruction on how to build Debian
packages using the stdeb configuration files:
https://github.com/palominodb/palominodb-priv/blob/master/tools/packaging/doc/building-debian-packages-using-stdeb.md


Setup Repositories for RPM/Debian packages
==========================================

Refer to the following documents for instructions on creating repositories
for RPM and Debian packages respectively:
https://github.com/palominodb/palominodb-priv/blob/master/tools/packaging/doc/creating-offline-rpm-repo-over-lan.md
https://github.com/palominodb/palominodb-priv/blob/master/tools/packaging/doc/creating-offline-deb-repo-over-lan.md


Prepare Amazon EC2 Images for Package Building
==============================================

1. Launch EC2 instances (CentOS for RPM package building, Ubuntu for Debian
package building)

2. Use the following ansible playbook to configure EC2 instances (see
included README):
https://github.com/palominodb/palominodb-priv/tree/master/tools/packaging/ansible-playbooks/jenkins_ci_slave

3. Using AWS console, create images based on the configured instances and
take note of the AMI IDs.


Configure Jenkins CI Server to Use Amazon EC2 Images
====================================================

Manage Jenkins > Configure System

in Cloud section, add new Amazon EC2 cloud and enter values for the following
fields (these values will be used for accessing an EC2 image and dynamically
launching an instance):

* Access Key ID =
* Secret Access Key =
* Region = ap-southeast-1
* EC2 Key Pair's Private Key =

Click add to add new AMI image and enter values for the following fields:

* Description = Jenkins slave for building RPM package using mock utility
* AMI ID = ami-2a612b78
* Instance Type = T1Micro
* Security group names = tools
* Remove FS root = /var/jenkins
* Remote user = jenkins
* Root command prefix = sudo
* Labels = centos
* Usage = Leave this machine for tied jobs only
* Idle termination time = 60
* Number of Executors = 1
* Remote ssh port = 22
* Stop/Disconnect on Idle Timeout = checked

in Tags, click add to add new tag and set the following values:
* Name = Name
* Value = Jenkins Node - CentOS 6.4 (Final) x86_64

Click add to add new AMI image and enter values for the following fields:

* Description = Jenkins slave for building DEB package using pbuilder
* AMI ID = ami-449cc916
* Instance Type = T1Micro
* Security group names = tools
* Remove FS root = /var/jenkins
* Remote user = jenkins
* Root command prefix = sudo
* Labels = ubuntu
* Usage = Leave this machine for tied jobs only
* Idle termination time = 60
* Number of Executors = 1
* Remote ssh port = 22
* Stop/Disconnect on Idle Timeout = checked

in Tags, click add to add new tag and set the following values:
* Name = Name
* Value = Jenkins Node - Ubuntu 12.04 x86_64


Setting up of Jenkins CI jobs to build RPM and Debian packages
==============================================================

Refer to the following document on how to configure Jenkins CI job
for python-int-overflow-check:
https://github.com/palominodb/python-int-overflow-check/blob/dev/docs/jenkins-configuration.txt

Refer to the following document on how to configure Jenkins CI job
for mysql-params parameter tracker:
https://github.com/palominodb/mysql-params/blob/master/docs/jenkins-configuration.txt

Refer to the following document on how to configure Jenkins CI job
for couchbase query tool:
https://github.com/palominodb/palominodb-priv/blob/master/tools/couchbase/python-query/docs/jenkins-configuration.txt


