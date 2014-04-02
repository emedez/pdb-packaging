Introduction
============

This document covers the procedure for building packages for Python 
applications using stdeb.


Requirements
============

To build packages, we need to install required packages

$ sudo apt-get install python-stdeb


Steps
=====

1. Download and extract the code that you want to package (we will use 
Django for this example):

$ wget https://pypi.python.org/packages/source/D/Django/Django-1.5.4.tar.gz
$ tar -zxf Django-1.5.4.tar.gz

Note: You can build the package directly without extracting the .tar.gz 
source using py2dsc but if you want to add customizations, extracting the 
source and adding your own settings in stdeb.cfg is the way.

2. Create stdeb.cfg with your package configuration (see stdeb documentation 
for this)

$ cd Django-1.5.4
$ cat <<EOF > stdeb.cfg
> [DEFAULT]
> Debian-Version: 1pdb.ubuntu12.4
> EOF

3. Build the package

$ python setup.py --command-packages=stdeb.command bdist_deb

4. If the process completed successfully, the package should not be available 
inside deb_dist directory.


