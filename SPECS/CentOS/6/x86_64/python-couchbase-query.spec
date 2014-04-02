%define pname couchbase-query
%define version 0.1b.dev
%define unmangled_version 0.1b.dev
%define unmangled_version 0.1b.dev
%define release 1.pdb%{?dist}

Summary:  Connects to a couchbase instance and returns the contents of bucket given a key
Name: python-%{pname}
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
Requires: gcc python >= 2.6 python-setuptools >= 0.6 PyYAML >= 3.10 python-argparse >= 1.2 python-logutils >= 0.3 python-requests >= 1.1 python-unittest2 >= 0.5 python-couchbase >= 0.8
Url: http://pypi.python.org/pypi/python-couchbase-query

%description
UNKNOWN

%prep
%setup -n %{pname}-%{unmangled_version} -n %{pname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
