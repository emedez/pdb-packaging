%define pname mysql-params
%define version 0.1b.dev
%define unmangled_version 0.1b.dev
%define release 1.pdb%{?dist}

Summary: Utility for tracking MySQL patterns
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: GPLv2
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: PalominoDB <oss@palominodb.com>
Packager: PalominoDB <oss@palominodb.com>
BuildRequires: python27, python27-libs, python27-setuptools
Requires: gcc, python27, python27-libs, mysql-devel >= 5.0, python27-MySQL-python >= 1.2, python27-Django >= 1.5.1, python27-South >= 0.7.6, python27-boto >= 2.9.5, python27-jsonfield >= 0.9.18, python27-texttable >= 0.8.1, python27-colorama >= 0.2.5, python27-pycrypto >= 2.6, python27-paramiko >= 1.7.5, python27-hurry.filesize >= 0.9
Url: http://pypi.python.org/pypi/mysql-params

%description
UNKNOWN

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
