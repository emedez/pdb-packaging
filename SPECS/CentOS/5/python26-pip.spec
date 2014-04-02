%define pname pip
%define version 1.4.1
%define unmangled_version 1.4.1
%define unmangled_version 1.4.1
%define release 1.pdb%{?dist}

Summary: A tool for installing and managing Python packages.
Name: python26-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: The pip developers <python-virtualenv@groups.google.com>
Url: http://www.pip-installer.org
BuildRequires: python26, python26-libs, python26-setuptools, git

%description

Project Info
============

* Project Page: https://github.com/pypa/pip
* Install howto: http://www.pip-installer.org/en/latest/installing.html
* Changelog: http://www.pip-installer.org/en/latest/news.html
* Bug Tracking: https://github.com/pypa/pip/issues
* Mailing list: http://groups.google.com/group/python-virtualenv
* Docs: http://www.pip-installer.org/
* IRC: #pip on Freenode.

Quickstart
==========

Install a package:

::

  $ pip install SomePackage==1.0
    [...]
    Successfully installed SomePackage

Show what files were installed:

::

  $ pip show --files SomePackage
    Name: SomePackage
    Version: 1.0
    Location: /my/env/lib/pythonx.x/site-packages
    Files:
     ../somepackage/__init__.py
     [...]

List what packages are outdated:

::

  $ pip list --outdated
    SomePackage (Current: 1.0 Latest: 2.0)

Upgrade a package:

::

  $ pip install --upgrade SomePackage
    [...]
    Found existing installation: SomePackage 1.0
    Uninstalling SomePackage:
      Successfully uninstalled SomePackage
    Running setup.py install --single-version-externally-managed for SomePackage
    Successfully installed SomePackage

Uninstall a package:

::

  $ pip uninstall SomePackage
    Uninstalling SomePackage:
      /my/env/lib/pythonx.x/site-packages/somepackage
    Proceed (y/n)? y
    Successfully uninstalled SomePackage



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
