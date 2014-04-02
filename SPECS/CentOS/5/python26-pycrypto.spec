%define pname pycrypto
%define version 2.6
%define unmangled_version 2.6
%define release 1.pdb%{?dist}

Summary: Cryptographic modules for Python.
Name: python26-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: UNKNOWN
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Dwayne C. Litzenberger <dlitz@dlitz.net>
Url: http://www.pycrypto.org/
BuildRequires: python26, python26-libs, python26-setuptools, python26-devel

%description
UNKNOWN

%prep
%setup -n %{pname}-%{unmangled_version}

%build
env CFLAGS="$RPM_OPT_FLAGS" python2.6 setup.py build

%install
python2.6 setup.py install -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
