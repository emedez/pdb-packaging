%define pname Django
%define version 1.5.4
%define unmangled_version 1.5.4
%define release 1.pdb%{?dist}

Summary: A high-level Python Web framework that encourages rapid development and clean, pragmatic design.
Name: python26-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: BSD
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Django Software Foundation <foundation@djangoproject.com>
Url: http://www.djangoproject.com/
BuildRequires: python26, python26-libs, python26-setuptools

%description
UNKNOWN

%prep
%setup -n %{pname}-%{unmangled_version}

%build
python2.6 setup.py build

%install
#! /bin/sh
#
# This file becomes the install section of the generated spec file.
#

# This is what dist.py normally does.
#%{__python} setup.py install --root=${RPM_BUILD_ROOT} --record="INSTALLED_FILES"
python2.6 setup.py install --root=${RPM_BUILD_ROOT} --record="INSTALLED_FILES"


# Sort the filelist so that directories appear before files. This avoids
# duplicate filename problems on some systems.
touch DIRS
for i in `cat INSTALLED_FILES`; do
  if [ -f ${RPM_BUILD_ROOT}/$i ]; then
    echo $i >>FILES
  fi
  if [ -d ${RPM_BUILD_ROOT}/$i ]; then
    echo %dir $i >>DIRS
  fi
done

# Make sure we match foo.pyo and foo.pyc along with foo.py (but only once each)
sed -e "/\.py[co]$/d" -e "s/\.py$/.py*/" DIRS FILES >INSTALLED_FILES

mkdir -p ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cp docs/man/* ${RPM_BUILD_ROOT}/%{_mandir}/man1/
cat << EOF >> INSTALLED_FILES
%doc %{_mandir}/man1/*"
EOF


%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc docs extras AUTHORS INSTALL LICENSE README.rst
