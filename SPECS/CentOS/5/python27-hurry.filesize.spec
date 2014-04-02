%define pname hurry.filesize
%define version 0.9
%define unmangled_version 0.9
%define release 1.pdb%{?dist}

Summary: A simple Python library for human readable file sizes (or anything sized in bytes).
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: ZPL 2.1
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Martijn Faassen, Startifact <faassen@startifact.com>
BuildRequires: python27, python27-libs, python27-setuptools

%description
hurry.filesize
==============

hurry.filesize a simple Python library that can take a number of bytes and
returns a human-readable string with the size in it, in kilobytes (K),
megabytes (M), etc.

The default system it uses is "traditional", where multipliers of 1024
increase the unit size::

  >>> from hurry.filesize import size
  >>> size(1024)
  '1K'

An alternative, slightly more verbose system::

  >>> from hurry.filesize import alternative
  >>> size(1, system=alternative)
  '1 byte'
  >>> size(10, system=alternative)
  '10 bytes'
  >>> size(1024, system=alternative)
  '1 KB'

A verbose system::

  >>> from hurry.filesize import verbose
  >>> size(10, system=verbose)
  '10 bytes'
  >>> size(1024, system=verbose)
  '1 kilobyte'
  >>> size(2000, system=verbose)
  '1 kilobyte'
  >>> size(3000, system=verbose)
  '2 kilobytes'
  >>> size(1024 * 1024, system=verbose)
  '1 megabyte'
  >>> size(1024 * 1024 * 3, system=verbose)
  '3 megabytes'

You can also use the SI system, where multipliers of 1000 increase the unit
size::

  >>> from hurry.filesize import si
  >>> size(1000, system=si)
  '1K'


Changes
=======

0.9 (2009-03-11)
----------------

* Initial public release.

Download
========


%prep
%setup -n %{pname}-%{unmangled_version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
