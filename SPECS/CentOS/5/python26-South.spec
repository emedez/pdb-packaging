%define pname South
%define version 0.7.6
%define unmangled_version 0.7.6
%define unmangled_version 0.7.6
%define release 1.pdb%{?dist}

Summary: South: Migrations for Django
Name: python26-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Andrew Godwin & Andy McCurdy <south@aeracode.org>
Url: http://south.aeracode.org/
BuildRequires: python26, python26-libs, python26-setuptools

%description
South is an intelligent database migrations library for the Django web framework. It is database-independent and DVCS-friendly, as well as a whole host of other features.

%prep
%setup -n %{pname}-%{unmangled_version} -n %{pname}-%{unmangled_version}

%build
python2.6 setup.py build

%install
python2.6 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
