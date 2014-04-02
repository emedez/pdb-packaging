%define pname logutils
%define version 0.3.3
%define unmangled_version 0.3.3
%define release 1.pdb%{?dist}

Summary: Logging utilities
Name: python26-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: Copyright (C) 2010-2013 by Vinay Sajip. All Rights Reserved. See LICENSE.txt for license.
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Vinay Sajip <vinay_sajip@red-dove.com>
Url: http://code.google.com/p/logutils/
BuildRequires: python26, python26-libs

%description
The logutils package provides a set of handlers for the Python standard
library's logging package.

Some of these handlers are out-of-scope for the standard library, and
so they are packaged here. Others are updated versions which have
appeared in recent Python releases, but are usable with older versions
of Python and so are packaged here.

The latest version of logutils can be found at:

  http://code.google.com/p/logutils/



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
