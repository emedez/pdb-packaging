Introduction
============

This document describes the steps for creating an offline Debian repository
over LAN.


Steps
=====

## Install a Local Apache Webserver

# apt-get install apache2

By default, Debian's Apache package will set up a website under /var/www on
your system. For our purposes, that's fine, so there's no reason to do anything
more. You can easily test it by pointing your favorite browser at
http://localhost.  You should see the default post-installation web page which
is actually stored in /var/www/index.html


## Create a Debian Package Repository Directory

I chose to create a directory /var/www/debs for this. Under it, you should
create "architecture" directories, one for each architecture you need to
support. If you're using just one computer (or type of computer), then you'll
only need one -- typically "i386" for 32-bit systems or "amd64" for 64 bit.
Now just copy the package files for a given architecture into the appropriate
directories. If you now point your favorite web browser at
http://localhost/debs/amd64 (for example) you'll see a listing of the packages
for 64 bit systems.


## Create a Packages.gz file

Now we need to create a catalog file for APT to use. This is done with a
utility called "dpkg-scanpackages". Here's the commands I use to update the
AMD64 packages on my LAN:

# cd /var/www/debs/

# dpkg-scanpackages amd64 | gzip -9c > amd64/Packages.gz


## Create Sources.gz file (optional)

# dpkg-scansources amd64 | gzip -9c > amd64/Sources.gz


## Make the repository known to APT

Now the only thing left to do is to let APT know about your repository. You do
this by updating your /etc/apt/sources.list file. You'll need an entry like
this one:

deb http://localhost/debs/ amd64/
deb-src http://localhost/debs/ amd64/


I used the actual hostname of my system instead of localhost -- this way the
code is the same for all of the computers on my LAN, but localhost will do just
fine if you are running just one computer.


## Now, update APT:

# apt-get update

