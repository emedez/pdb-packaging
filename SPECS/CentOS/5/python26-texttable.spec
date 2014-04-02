%define pname texttable
%define version 0.8.1
%define unmangled_version 0.8.1
%define release 1.pdb%{?dist}

Summary: module for creating simple ASCII tables
Name: python26-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: LGPL
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Gerome Fournier <jef(at)foutaise.org>
Url: http://foutaise.org/code/
BuildRequires: python26, python26-libs, python26-setuptools

%description
texttable is a module to generate a formatted text table, using ASCII
characters.

%prep
%setup -n %{pname}-%{unmangled_version}

%build
python2.6 setup.py build

%install
python2.6 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
