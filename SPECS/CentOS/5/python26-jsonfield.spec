%define pname jsonfield
%define version 0.9.16
%define unmangled_version 0.9.16
%define release 1.pdb%{?dist}

Summary: A reusable Django field that allows you to store validated JSON in your model.
Name: python26-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: MIT
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Brad Jasper <bjasper@gmail.com>
Url: https://github.com/bradjasper/django-jsonfield/
BuildRequires: python26, python26-libs, python26-setuptools

%description
django-jsonfield
----------------

django-jsonfield is a reusable Django field that allows you to store validated JSON in your model.

It silently takes care of serialization. To use, simply add the field to one of your models.

**New: Python 3 support added!**

Install
-------

.. code-block:: python

    pip install jsonfield


Usage
-----

.. code-block:: python

    from django.db import models
    from jsonfield import JSONField

    class MyModel(models.Model):
      json = JSONField()

Advanced Usage
--------------

By default python deserializes json into dict objects. This behavior differs from the standard json behavior because python dicts do not have ordered keys.

To overcome this limitation and keep the sort order of OrderedDict keys the deserialisation can be adjusted on model initialisation:

.. code-block:: python

    import collections
    class MyModel(models.Model):
      json = JSONField(load_kwargs={'object_pairs_hook': collections.OrderedDict})


Other Fields
------------

**jsonfield.JSONCharField**

If you need to use your JSON field in an index or other constraint, you can use **JSONCharField** which subclasses **CharField** instead of **TextField**. You'll also need to specify a **max_length** parameter if you use this field.


Compatibility
--------------

django-jsonfield supports Python 2.7-Python 3.3 and Django 1.4+

**Why doesn't it support Python 2.6?**

You actually might be OK if you don't use an OrderedDict, but there are some issues with the simplejson API that make it cumbersome to support.

**Why doesn't it support Django 1.3?**

There was a bug that could only be fixed by a feature in Django 1.4. `Read More`_ if you're interested in the details.

.. _Read More: https://github.com/bradjasper/django-jsonfield/issues/33


Travis CI
---------

.. image:: https://travis-ci.org/bradjasper/django-jsonfield.png?branch=master


Contact
-------

http://bradjasper.com

Changes
-------

v0.9.19, 09/18/2013 -- Fixed changes to django.six.with_metaclass that broke django-jsonfield for Django 1.6

v0.9.18, 08/23/2013 -- Fixed bugs with South datamigration

v0.9.17, 06/07/2013 -- Fixed bugs in JSONCharField admin form

v0.9.14/15/16, 04/29/2013 -- Python 3 support added!

v0.9.11/12/13, 03/26/2013 -- PyPi changes

v0.9.9/10/11, 03/21/2013 -- PyPi changes

v0.9.8, 03/21/2013 -- Added support for native PostgreSQL JSON data type

v0.9.7, 03/21/2013 -- Fix bug #33 where JSONField didn't correctly store some values inside of
strings



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
