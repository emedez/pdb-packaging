%define pname couchbase
%define version 1.8.0
%define unmangled_version 1.8.0
%define release 1.pdb%{?dist}

Summary: Couchbase Python SDK
Name: python-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: LICENSE.txt
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Couchbase Inc <info@couchbase.com>
Url: http://couchbase.org/
Requires: python >= 2.6

%description
This library provides methods to connect to both the couchbase
memcached interface and the couchbase rest api interface.


%prep
%setup -n %{pname}-%{unmangled_version}

%build
python setup.py build

%install
python setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
