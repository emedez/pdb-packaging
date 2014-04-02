Introduction
============

This document explains how to create a debian package from a git repository 
using git-buildpackage on Ubuntu.


Requirements
============

$ sudo apt-get install devscripts pbuilder git-buildpackage dh-make apt-utils


Steps
=====

## 1. Create a directory to contain your sources and other files, and clone 
your target repository inside this directory (we will use the mysql-params 
project as example).

$ mkdir mysql-params
$ cd mysql-params
$ git clone https://github.com/palominodb/mysql-params.git


## 2. Build a source distribution and put the result on the parent directory 
of your source directory.

$ cd mysql-params
$ python setup.py sdist -d ../


## 3. Renamed the resulting tarball from the format <package>_<version>.tar.gz 
to <package>_<version>.orig.tar.gz

$ cd ../
$ mv mysql-params-0.1b.dev.tar.gz mysql-params_0.1b.dev.orig.tar.gz


## 4. Create our debian branches on the git repository: debian-upstream, 
where we will store the upstream source, and debian-debian, which will hold 
the debian package data.  This separation provides a cleaner revision history 
by separating the changes that affect the software from the changes in the 
packaging.

$ cd mysql-params
$ git symbolic-ref HEAD refs/heads/debian-upstream
$ git rm --cached -r .
$ git clean -xfd
$ git commit --allow-empty -m ‘Start of debian branches.’
$ git checkout -b debian-debian

That will make both branches point to a root-commit with no files.


## 5. Create the initial debian directory in the debian-debian branch.

$ DEBFULLNAME="Elmer Medez" DEBEMAIL="emedez@palominodb.com" \
    dh_make -s -p mysql-params_0.1b.dev
$ rm debian/*.{ex,EX}

We had set a couple of environment variables to tell the script what to fill 
in for the maintainer field.

We can now customize the standard debian directory created.  The only required 
files that must be fixed are changelog, compat, control, copyright, and rules.

Fix debian/changelog:

The original content was:
mysql-params (0.1b.dev-1) unstable; urgency=low

  * Initial release (Closes: #nnnn)  <nnnn is the bug number of your ITP>

 -- Elmer Medez <emedez@palominodb.com>  Wed, 30 Oct 2013 05:56:03 +0000

My updated version is:
mysql-params (0.1b.dev-1pdb.ubuntu12.4) unstable; urgency=low

  * Initial release

 -- Elmer Medez <emedez@palominodb.com>  Wed, 30 Oct 2013 05:56:03 +0000

Take a closer look at the version number:
(0.1b.dev-1pdb.ubuntu12.4)

The first part 0.1b.dev is the upstream package version. The second part 
1pdb.ubuntu12.4 is the Debian version.

Fix debian/control:

The original content was:
Source: mysql-params
Section: unknown
Priority: extra
Maintainer: Elmer Medez <emedez@palominodb.com>
Build-Depends: debhelper (>= 8.0.0)
Standards-Version: 3.9.2
Homepage: <insert the upstream URL, if relevant>
#Vcs-Git: git://git.debian.org/collab-maint/mysql-params.git
#Vcs-Browser: http://git.debian.org/?p=collab-maint/mysql-params.git;a=summary

Package: mysql-params
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}
Description: <insert up to 60 chars description>
 <insert long description, indented with spaces>

My updated version is:
Source: mysql-params
Section: python
Priority: extra
Maintainer: Elmer Medez <emedez@palominodb.com>
Build-Depends: debhelper (>= 8.0.0), python-all, python-setuptools
Standards-Version: 3.9.2

Package: python-mysql-params
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, ${python:Depends}
Description: Utility for tracking MySQL patterns

Fix debian/rules:

Replaced line:
    dh $@

with:
    dh $@ --with python2


Create a debian/gbp.conf with the following contents:

[DEFAULT]
upstream-branch=debian-upstream
debian-branch=debian-debian

We can now commit the debian directory in the debian-debian branch.


## 6. Import the original sources.

In the debian-debian branch:

$ git-import-orig ../mysql-params_0.1b.dev.orig.tar.gz

That will import the original sources to the debian-upstream branch, and 
merge it with the debian-debian branch.


## 7. Create the package.

$ git-buildpackage --git-builder="DIST=precise ARCH=amd64 pdebuild" \
    2>&1 | tee ../build.log

For new versions:

Create the new ../<package>_<version>/.orig.tar.gz and then:

$ git-import-orig ../<package>_<version>.orig.tar.gz

Edit the debian/changelog file (we can use dch for that), and create a new 
package:

$ DEBFULLNAME="Elmer Medez" DEBEMAIL="emedez@palominodb.com" dch
$ git-buildpackage --git-builder="DIST=precise ARCH=amd64 pdebuild" \
    2>&1 | tee ../build.log


