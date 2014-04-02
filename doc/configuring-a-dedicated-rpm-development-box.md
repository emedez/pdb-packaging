Configuring a Dedicated RPM Development Box
===========================================

This article uses CentOS 6 as an example.


Conventions and Vocabulary
--------------------------

All commands are prefixed with a generi shell, and appear in a code block 
such as:

[user@mockbuild]$ echo "This is a regular user shell"
[root@mockbuild]# echo "This is a root shell"

Take note of the user [user@, root@] and shell prompt [#, $] for each command.
Some pieces of the article require root access, some are expectd to be run 
as a regular user account.

The hostname we use is 'mockbuild' to signify this machine we are working 
on. If the present working directory is important, we will first prefix any 
commands with a 'cd' statement to signify that you should change to a
specific directory.


Configure 3rd Party Yum Repositories
------------------------------------

You may wish to have 3rd party yum repos setup as well, though keep in mind
that this is for the host system only.  You have to add 3rd party repo 
configs to your mock configuration files as well if you wish to build against 
packages in the 3rd party repo (more on that later). Because we want to use 
the Fedora Mock utility, we want to install the EPEL repository:

[root@mockbuild]# rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/`uname -i`/epel-release-6-8.noarch.rpm 


Install Fedora Mock and Other Packages
--------------------------------------

[root@mockbuild]# yum install mock rpm-build


Configure Global Environment Settings
-------------------------------------

There are a number of global settings we can make that will optimize the use 
of this system for RPM Development with Mock.

/etc/profile.d/mock.sh:

We prefer to add an alias for the mock command that adds a unique extension 
to the end of each build. This is critical on a shared system where you might 
have multiple developers building against the same target. Add the following 
to /etc/profile.d/mock.sh as well as any other global mock environment changes 
you need:

alias mock="mock --uniqueext=$USER"

And make the file executable:

[root@mockbuild]# chmod +x /etc/profile.d/mock.sh

/etc/skel:

Setting up a default /etc/skel can help provide a decent ‘starting point’ 
for users, and help encourage a common practice on working with files. The 
following sets up /etc/skel.

Create the buildroot for packaging:

[root@rpmbuild]# mkdir /etc/skel/packages

[root@rpmbuild]# cd /etc/skel/packages

[root@rpmbuild]# mkdir buildroot.clean/{RPMS,SRPMS,SPECS,BUILD,SOURCES} -p

Create the RPM Macros file to set rpmbuild defaults by adding the following 
to /etc/skel/.rpmmacros:

%_topdir %(pwd)

Note, these settings are for CentOS 6 and would be different for others.

We set each user’s _topdir (default: /usr/src/redhat) to ‘pwd’ [present 
working directory] as it makes working out of multiple build roots easier. 
Remember, this system is dedicated to RPM Development! We will explain this 
a bit more in detailed later in the article. Setting _topdir to ‘pwd’ is a 
preference and can be modified based on each individuals needs.


Add / Modify Users
------------------

At this point you should have everything in place to setup users properly.

New Users:

[root@mockbuild]# useradd <username>

[root@mockbuild]# passwd <username>

[root@mockbuild]# usermod -aG mock <username>

Existing Users:

[root@mockbuild]# usermod -aG mock <username>

[root@mockbuild]# sudo -u <username> cp -a /etc/skel/packages /home/<username>

[root@mockbuild]# sudo -u <username> cp -a /etc/skel/.rpmmacros /home/<username>


Mock Configurations
-------------------

Mock comes with a number of default configurations for building against and 
CentOS with EPEL. All target configuration files are in /etc/mock.

### Setting Global Defaults

Global defaults are in /etc/mock/site-defaults.cfg, of which each individual 
target config can override. For the majority of Mock users, the defaults are 
preferred and shouldn’t really need to be modified.

### Stock Build Targets

As mentioned, mock comes with a number of stock build targets. 
Essentially, the config simply sets a number of unique configuration options 
including the Yum config to use for the build. It is recommended to keep the 
stock config files as-is so that you have a basis for ‘building against a 
stock distro’ as apposed to custom targets that might include additional 3rd 
party repositories.

### Custom Build Targets

Custom build targets can be created by simply copying a stock config and 
adding the changes and additional 3rd party repositories that you might 
want to build against. As an example, I will create a custom build target 
that builds against CentOS 5 x86_64 + Fedora EPEL 5 + IUS 5 repositories.

/etc/mock/centos-6-x86_64-epel-ius-pdb:

config_opts['root'] = 'centos-6-x86_64-epel-ius-pdb'
config_opts['target_arch'] = 'x86_64'
config_opts['legal_host_arches'] = ('x86_64',)
config_opts['chroot_setup_cmd'] = 'groupinstall buildsys-build'
config_opts['dist'] = 'el6'  # only useful for --resultdir variable subst

config_opts['yum.conf'] = """
[main]
cachedir=/var/cache/yum
debuglevel=1
reposdir=/dev/null
logfile=/var/log/yum.log
retries=20
obsoletes=1
gpgcheck=0
assumeyes=1
syslog_ident=mock
syslog_device=

# repos
[base]
name=CentOS-$releasever - Base
mirrorlist=http://mirrorlist.centos.org/?release=6&arch=x86_64&repo=os

#released updates
[updates]
name=CentOS-$releasever - Updates
mirrorlist=http://mirrorlist.centos.org/?release=6&arch=x86_64&repo=updates

[extras]
name=CentOS-$releasever - Extras
mirrorlist=http://mirrorlist.centos.org/?release=6&arch=x86_64&repo=extras

[centosplus]
name=CentOS-$releasever - Plus
mirrorlist=http://mirrorlist.centos.org/?release=6&arch=x86_64&repo=centosplus

[epel]
name=Extra Packages for Enterprise Linux 6 - x86_64
mirrorlist=https://mirrors.fedoraproject.org/metalink?repo=epel-6&arch=x86_64

[ius]
name=IUS Community Packages for Enterprise Linux 6 - x86_64
mirrorlist=http://dmirr.iuscommunity.org/mirrorlist/?repo=ius-centos6&arch=x86_64

[PalominoDB]
name=PalominoDB Packages for Enterprise Linux 6 - x86_64
baseurl=http://yum.palominodb.com/centos/6/x86_64
"""

### A Sample Build with Mock

We will use couchbase-python-client python source code from github repository
as an example.


Setup the unique, dedicated build root for this package:

[user@mockbuild]$ cd ~/packages

[user@mockbuild]$ cp -a buildroot.clean python-couchbase


Create source distribution and copy it to the SOURCES directory of the target
buildroot: 

[user@mockbuild]$ cd ~

[user@mockbuild]$ git clone https://github.com/couchbase/couchbase-python-client.git

[user@mockbuild]$ cd couchbase-python-client

[user@mockbuild]$ git checkout couchbase-181

[user@mockbuild]$ python setup.py sdist -d ~/packages/python-couchbase/SOURCES/


Create ~/packages/python-couchbase/SPECS/python-couchbase.spec with the 
following contents:

%define pname couchbase
%define version 1.8.0
%define unmangled_version 1.8.0
%define release 1.pdb%{?dist}

Summary: Couchbase Python SDK
Name: python-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: LICENSE.txt
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Couchbase Inc <info@couchbase.com>
Url: http://couchbase.org/
Requires: python >= 2.6

%description
This library provides methods to connect to both the couchbase
memcached interface and the couchbase rest api interface.

%prep
%setup -n %{pname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)


Build source package:

[user@mockbuild]$ cd ~/package/python-couchbase

[user@mockbuild]$ rpmbuild -bs --nodeps --define "dist %{nil}" \
    --define "_source_filedigest_algorithm md5" \
    SPECS/python-couchbase.spec

This will create a source package under the SRPMS directory.


Build binary package:

[user@mockbuild]$ mkdir -p ~/results

[user@mockbuild]$ mock --uniqueext=$USER -r centos-6-x86_64-epel-ius-pdb \
    rebuild --resultdir=~/results \
    SRPMS/python-couchbase-1.8.0-1.pdb-src.rpm

The binary package should now be available at $/results.

Should the build fail, you can view the 'build.log' in the result dir for the
output of the rpmbuild command that mock ran.  Modify your spec, rebuild the
source rpm again, and then rebuild with mock once again.

