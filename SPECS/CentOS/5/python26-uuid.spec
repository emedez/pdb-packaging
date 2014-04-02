%define pname uuid
%define version 1.30
%define unmangled_version 1.30
%define release 1.pdb%{?dist}

Summary: UUID object and generation functions
Name: python26-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Ka-Ping Yee <ping@zesty.ca>
Url: http://zesty.ca/python/
BuildRequires: python26, python26-libs, python26-setuptools

%description
UNKNOWN

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
