%define pname MySQL-python
%define version 1.2.4
%define unmangled_version 1.2.4
%define unmangled_version 1.2.4
%define release 1.pdb%{?dist}

Summary: Python interface to MySQL
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: GPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: MySQL-python SourceForge Project
Packager: Andy Dustman <adustman@users.sourceforge.net>
Requires: python27 python27-setuptools
Url: https://github.com/farcepest/MySQLdb1
Distribution: Red Stains Linux
BuildRequires: python27-devel mysql-devel zlib-devel openssl-devel

%description

=========================
Python interface to MySQL
=========================

MySQLdb is an interface to the popular MySQL_ database server for
Python.  The design goals are:

- Compliance with Python database API version 2.0 [PEP-0249]_
- Thread-safety
- Thread-friendliness (threads will not block each other)

MySQL-3.23 through 5.5 and Python-2.4 through 2.7 are currently
supported. Python-3.0 will be supported in a future release.
PyPy is supported.

MySQLdb is `Free Software`_.

.. _MySQL: http://www.mysql.com/
.. _`Free Software`: http://www.gnu.org/
.. [PEP-0249] http://www.python.org/peps/pep-0249.html

%prep
%setup -n %{pname}-%{unmangled_version} -n %{pname}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.7 setup.py build

%install
python2.7 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
