%define pname paramiko
%define version 1.10.1
%define unmangled_version 1.10.1
%define release 1.pdb%{?dist}

Summary: SSH2 protocol library
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Jeff Forcier <jeff@bitprophet.org>
Url: https://github.com/paramiko/paramiko/
BuildRequires: python27, python27-libs, python27-setuptools

%description

This is a library for making SSH2 connections (client or server).
Emphasis is on using SSH2 as an alternative to SSL for making secure
connections between python scripts.  All major ciphers and hash methods
are supported.  SFTP client and server mode are both supported too.

Required packages:
    pyCrypto

To install the `in-development version
<https://github.com/paramiko/paramiko/tarball/master#egg=paramiko-dev>`_, use
`pip install paramiko==dev`.


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
