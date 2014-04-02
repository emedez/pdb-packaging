%define pname requests
%define version 1.1.0
%define unmangled_version 1.1.0
%define release 1.pdb%{?dist}

Summary: Python HTTP for Humans.
Name: python27-%{pname}
Version: %{version}
Release: %{release}
Source0: %{pname}-%{unmangled_version}.tar.gz
License: ASL 2.0
Group: Development/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: noarch
Vendor: Kenneth Reitz <me@kennethreitz.com>
Url: http://python-requests.org
BuildRequires: python27, python27-libs, python27-setuptools

%description
Requests: HTTP for Humans
=========================


.. image:: https://travis-ci.org/kennethreitz/requests.png?branch=master
        :target: https://travis-ci.org/kennethreitz/requests

Requests is an Apache2 Licensed HTTP library, written in Python, for human
beings.

Most existing Python modules for sending HTTP requests are extremely
verbose and cumbersome. Python's builtin urllib2 module provides most of
the HTTP capabilities you should need, but the api is thoroughly broken.
It requires an enormous amount of work (even method overrides) to
perform the simplest of tasks.

Things shouldn't be this way. Not in Python.

.. code-block:: pycon

    >>> r = requests.get('https://api.github.com', auth=('user', 'pass'))
    >>> r.status_code
    204
    >>> r.headers['content-type']
    'application/json'
    >>> r.text
    ...

See `the same code, without Requests <https://gist.github.com/973705>`_.

Requests allow you to send HTTP/1.1 requests. You can add headers, form data,
multipart files, and parameters with simple Python dictionaries, and access the
response data in the same way. It's powered by httplib and `urllib3
<https://github.com/shazow/urllib3>`_, but it does all the hard work and crazy
hacks for you.


Features
--------

- International Domains and URLs
- Keep-Alive & Connection Pooling
- Sessions with Cookie Persistence
- Browser-style SSL Verification
- Basic/Digest Authentication
- Elegant Key/Value Cookies
- Automatic Decompression
- Unicode Response Bodies
- Multipart File Uploads
- Connection Timeouts
- Thread-safety


Installation
------------

To install requests, simply:

.. code-block:: bash

    $ pip install requests

Or, if you absolutely must:

.. code-block:: bash

    $ easy_install requests

But, you really shouldn't do that.



Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug. There is a Contributor Friendly tag for issues that should be ideal for people who are not very familiar with the codebase yet.
#. Fork `the repository`_ on Github to start making your changes to the **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as expected.
#. Send a pull request and bug the maintainer until it gets merged and published. :) Make sure to add yourself to AUTHORS_.

.. _`the repository`: http://github.com/kennethreitz/requests
.. _AUTHORS: https://github.com/kennethreitz/requests/blob/master/AUTHORS.rst


.. :changelog:

History
-------

1.1.0 (2013-01-10)
++++++++++++++++++

- CHUNKED REQUESTS
- Support for iterable response bodies
- Assume servers persist redirect params
- Allow explicit content types to be specified for file data
- Make merge_kwargs case-insensitive when looking up keys

1.0.3 (2012-12-18)
++++++++++++++++++

- Fix file upload encoding bug
- Fix cookie behavior

1.0.2 (2012-12-17)
++++++++++++++++++

- Proxy fix for HTTPAdapter.

1.0.1 (2012-12-17)
++++++++++++++++++

- Cert verification exception bug.
- Proxy fix for HTTPAdapter.

1.0.0 (2012-12-17)
++++++++++++++++++

- Massive Refactor and Simplification
- Switch to Apache 2.0 license
- Swappable Connection Adapters
- Mountable Connection Adapters
- Mutable ProcessedRequest chain
- /s/prefetch/stream
- Removal of all configuration
- Standard library logging
- Make Reponse.json() callable, not property.
- Usage of new charade project, which provides python 2 and 3 simultaneous chardet.
- Removal of all hooks except 'response'
- Removal of all authentication helpers (OAuth, Kerberos)

This is not a backwards compatible change.

0.14.2 (2012-10-27)
+++++++++++++++++++

- Improved mime-compatible JSON handling
- Proxy fixes
- Path hack fixes
- Case-Insensistive Content-Encoding headers
- Support for CJK parameters in form posts


0.14.1 (2012-10-01)
+++++++++++++++++++

- Python 3.3 Compatibility
- Simply default accept-encoding
- Bugfixes


0.14.0 (2012-09-02)
++++++++++++++++++++

- No more iter_content errors if already downloaded.

0.13.9 (2012-08-25)
+++++++++++++++++++

- Fix for OAuth + POSTs
- Remove exception eating from dispatch_hook
- General bugfixes

0.13.8 (2012-08-21)
+++++++++++++++++++

- Incredible Link header support :)

0.13.7 (2012-08-19)
+++++++++++++++++++

- Support for (key, value) lists everywhere.
- Digest Authentication improvements.
- Ensure proxy exclusions work properly.
- Clearer UnicodeError exceptions.
- Automatic casting of URLs to tsrings (fURL and such)
- Bugfixes.

0.13.6 (2012-08-06)
+++++++++++++++++++

- Long awaited fix for hanging connections!

0.13.5 (2012-07-27)
+++++++++++++++++++

- Packaging fix

0.13.4 (2012-07-27)
+++++++++++++++++++

- GSSAPI/Kerberos authentication!
- App Engine 2.7 Fixes!
- Fix leaking connections (from urllib3 update)
- OAuthlib path hack fix
- OAuthlib URL parameters fix.

0.13.3 (2012-07-12)
+++++++++++++++++++

- Use simplejson if available.
- Do not hide SSLErrors behind Timeouts.
- Fixed param handling with urls containing fragments.
- Significantly improved information in User Agent.
- client certificates are ignored when verify=False

0.13.2 (2012-06-28)
+++++++++++++++++++

- Zero dependencies (once again)!
- New: Response.reason
- Sign querystring parameters in OAuth 1.0
- Client certificates no longer ignored when verify=False
- Add openSUSE certificate support

0.13.1 (2012-06-07)
+++++++++++++++++++

- Allow passing a file or file-like object as data.
- Allow hooks to return responses that indicate errors.
- Fix Response.text and Response.json for body-less responses.

0.13.0 (2012-05-29)
+++++++++++++++++++

- Removal of Requests.async in favor of `grequests <https://github.com/kennethreitz/grequests>`_
- Allow disabling of cookie persistiance.
- New implimentation of safe_mode
- cookies.get now supports default argument
- Session cookies not saved when Session.request is called with return_response=False
- Env: no_proxy support.
- RequestsCookieJar improvements.
- Various bug fixes.

0.12.1 (2012-05-08)
+++++++++++++++++++

- New ``Response.json`` property.
- Ability to add string file uploads.
- Fix out-of-range issue with iter_lines.
- Fix iter_content default size.
- Fix POST redirects containing files.

0.12.0 (2012-05-02)
+++++++++++++++++++

- EXPERIMENTAL OAUTH SUPPORT!
- Proper CookieJar-backed cookies interface with awesome dict-like interface.
- Speed fix for non-iterated content chunks.
- Move ``pre_request`` to a more usable place.
- New ``pre_send`` hook.
- Lazily encode data, params, files.
- Load system Certificate Bundle if ``certify`` isn't available.
- Cleanups, fixes.

0.11.2 (2012-04-22)
+++++++++++++++++++

- Attempt to use the OS's certificate bundle if ``certifi`` isn't available.
- Infinite digest auth redirect fix.
- Multi-part file upload improvements.
- Fix decoding of invalid %encodings in URLs.
- If there is no content in a response don't throw an error the second time that content is attempted to be read.
- Upload data on redirects.

0.11.1 (2012-03-30)
+++++++++++++++++++

* POST redirects now break RFC to do what browsers do: Follow up with a GET.
* New ``strict_mode`` configuration to disable new redirect behavior.


0.11.0 (2012-03-14)
+++++++++++++++++++

* Private SSL Certificate support
* Remove select.poll from Gevent monkeypatching
* Remove redundant generator for chunked transfer encoding
* Fix: Response.ok raises Timeout Exception in safe_mode

0.10.8 (2012-03-09)
+++++++++++++++++++

* Generate chunked ValueError fix
* Proxy configuration by environment variables
* Simplification of iter_lines.
* New `trust_env` configuration for disabling system/environment hints.
* Suppress cookie errors.

0.10.7 (2012-03-07)
+++++++++++++++++++

* `encode_uri` = False

0.10.6 (2012-02-25)
+++++++++++++++++++

* Allow '=' in cookies.

0.10.5 (2012-02-25)
+++++++++++++++++++

* Response body with 0 content-length fix.
* New async.imap.
* Don't fail on netrc.


0.10.4 (2012-02-20)
+++++++++++++++++++

* Honor netrc.

0.10.3 (2012-02-20)
+++++++++++++++++++

* HEAD requests don't follow redirects anymore.
* raise_for_status() doesn't raise for 3xx anymore.
* Make Session objects picklable.
* ValueError for invalid schema URLs.

0.10.2 (2012-01-15)
+++++++++++++++++++

* Vastly improved URL quoting.
* Additional allowed cookie key values.
* Attempted fix for "Too many open files" Error
* Replace unicode errors on first pass, no need for second pass.
* Append '/' to bare-domain urls before query insertion.
* Exceptions now inherit from RuntimeError.
* Binary uploads + auth fix.
* Bugfixes.


0.10.1 (2012-01-23)
+++++++++++++++++++

* PYTHON 3 SUPPORT!
* Dropped 2.5 Support. (*Backwards Incompatible*)

0.10.0 (2012-01-21)
+++++++++++++++++++

* ``Response.content`` is now bytes-only. (*Backwards Incompatible*)
* New ``Response.text`` is unicode-only.
* If no ``Response.encoding`` is specified and ``chardet`` is available, ``Respoonse.text`` will guess an encoding.
* Default to ISO-8859-1 (Western) encoding for "text" subtypes.
* Removal of `decode_unicode`. (*Backwards Incompatible*)
* New multiple-hooks system.
* New ``Response.register_hook`` for registering hooks within the pipeline.
* ``Response.url`` is now Unicode.

0.9.3 (2012-01-18)
++++++++++++++++++

* SSL verify=False bugfix (apparent on windows machines).

0.9.2 (2012-01-18)
++++++++++++++++++

* Asynchronous async.send method.
* Support for proper chunk streams with boundaries.
* session argument for Session classes.
* Print entire hook tracebacks, not just exception instance.
* Fix response.iter_lines from pending next line.
* Fix but in HTTP-digest auth w/ URI having query strings.
* Fix in Event Hooks section.
* Urllib3 update.


0.9.1 (2012-01-06)
++++++++++++++++++

* danger_mode for automatic Response.raise_for_status()
* Response.iter_lines refactor

0.9.0 (2011-12-28)
++++++++++++++++++

* verify ssl is default.


0.8.9 (2011-12-28)
++++++++++++++++++

* Packaging fix.


0.8.8 (2011-12-28)
++++++++++++++++++

* SSL CERT VERIFICATION!
* Release of Cerifi: Mozilla's cert list.
* New 'verify' argument for SSL requests.
* Urllib3 update.

0.8.7 (2011-12-24)
++++++++++++++++++

* iter_lines last-line truncation fix
* Force safe_mode for async requests
* Handle safe_mode exceptions more consistently
* Fix iteration on null responses in safe_mode

0.8.6 (2011-12-18)
++++++++++++++++++

* Socket timeout fixes.
* Proxy Authorization support.

0.8.5 (2011-12-14)
++++++++++++++++++

* Response.iter_lines!

0.8.4 (2011-12-11)
++++++++++++++++++

* Prefetch bugfix.
* Added license to installed version.

0.8.3 (2011-11-27)
++++++++++++++++++

* Converted auth system to use simpler callable objects.
* New session parameter to API methods.
* Display full URL while logging.

0.8.2 (2011-11-19)
++++++++++++++++++

* New Unicode decoding system, based on over-ridable `Response.encoding`.
* Proper URL slash-quote handling.
* Cookies with ``[``, ``]``, and ``_`` allowed.

0.8.1 (2011-11-15)
++++++++++++++++++

* URL Request path fix
* Proxy fix.
* Timeouts fix.

0.8.0 (2011-11-13)
++++++++++++++++++

* Keep-alive support!
* Complete removal of Urllib2
* Complete removal of Poster
* Complete removal of CookieJars
* New ConnectionError raising
* Safe_mode for error catching
* prefetch parameter for request methods
* OPTION method
* Async pool size throttling
* File uploads send real names
* Vendored in urllib3

0.7.6 (2011-11-07)
++++++++++++++++++

* Digest authentication bugfix (attach query data to path)

0.7.5 (2011-11-04)
++++++++++++++++++

* Response.content = None if there was an invalid repsonse.
* Redirection auth handling.

0.7.4 (2011-10-26)
++++++++++++++++++

* Session Hooks fix.

0.7.3 (2011-10-23)
++++++++++++++++++

* Digest Auth fix.


0.7.2 (2011-10-23)
++++++++++++++++++

* PATCH Fix.


0.7.1 (2011-10-23)
++++++++++++++++++

* Move away from urllib2 authentication handling.
* Fully Remove AuthManager, AuthObject, &c.
* New tuple-based auth system with handler callbacks.


0.7.0 (2011-10-22)
++++++++++++++++++

* Sessions are now the primary interface.
* Deprecated InvalidMethodException.
* PATCH fix.
* New config system (no more global settings).


0.6.6 (2011-10-19)
++++++++++++++++++

* Session parameter bugfix (params merging).


0.6.5 (2011-10-18)
++++++++++++++++++

* Offline (fast) test suite.
* Session dictionary argument merging.


0.6.4 (2011-10-13)
++++++++++++++++++

* Automatic decoding of unicode, based on HTTP Headers.
* New ``decode_unicode`` setting.
* Removal of ``r.read/close`` methods.
* New ``r.faw`` interface for advanced response usage.*
* Automatic expansion of parameterized headers.


0.6.3 (2011-10-13)
++++++++++++++++++

* Beautiful ``requests.async`` module, for making async requests w/ gevent.


0.6.2 (2011-10-09)
++++++++++++++++++

* GET/HEAD obeys allow_redirects=False.


0.6.1 (2011-08-20)
++++++++++++++++++

* Enhanced status codes experience ``\o/``
* Set a maximum number of redirects (``settings.max_redirects``)
* Full Unicode URL support
* Support for protocol-less redirects.
* Allow for arbitrary request types.
* Bugfixes


0.6.0 (2011-08-17)
++++++++++++++++++

* New callback hook system
* New persistient sessions object and context manager
* Transparent Dict-cookie handling
* Status code reference object
* Removed Response.cached
* Added Response.request
* All args are kwargs
* Relative redirect support
* HTTPError handling improvements
* Improved https testing
* Bugfixes


0.5.1 (2011-07-23)
++++++++++++++++++

* International Domain Name Support!
* Access headers without fetching entire body (``read()``)
* Use lists as dicts for parameters
* Add Forced Basic Authentication
* Forced Basic is default authentication type
* ``python-requests.org`` default User-Agent header
* CaseInsensitiveDict lower-case caching
* Response.history bugfix


0.5.0 (2011-06-21)
++++++++++++++++++

* PATCH Support
* Support for Proxies
* HTTPBin Test Suite
* Redirect Fixes
* settings.verbose stream writing
* Querystrings for all methods
* URLErrors (Connection Refused, Timeout, Invalid URLs) are treated as explicity raised
  ``r.requests.get('hwe://blah'); r.raise_for_status()``


0.4.1 (2011-05-22)
++++++++++++++++++

* Improved Redirection Handling
* New 'allow_redirects' param for following non-GET/HEAD Redirects
* Settings module refactoring


0.4.0 (2011-05-15)
++++++++++++++++++

* Response.history: list of redirected responses
* Case-Insensitive Header Dictionaries!
* Unicode URLs


0.3.4 (2011-05-14)
++++++++++++++++++

* Urllib2 HTTPAuthentication Recursion fix (Basic/Digest)
* Internal Refactor
* Bytes data upload Bugfix



0.3.3 (2011-05-12)
++++++++++++++++++

* Request timeouts
* Unicode url-encoded data
* Settings context manager and module


0.3.2 (2011-04-15)
++++++++++++++++++

* Automatic Decompression of GZip Encoded Content
* AutoAuth Support for Tupled HTTP Auth


0.3.1 (2011-04-01)
++++++++++++++++++

* Cookie Changes
* Response.read()
* Poster fix


0.3.0 (2011-02-25)
++++++++++++++++++

* Automatic Authentication API Change
* Smarter Query URL Parameterization
* Allow file uploads and POST data together
* New Authentication Manager System
    - Simpler Basic HTTP System
    - Supports all build-in urllib2 Auths
    - Allows for custom Auth Handlers


0.2.4 (2011-02-19)
++++++++++++++++++

* Python 2.5 Support
* PyPy-c v1.4 Support
* Auto-Authentication tests
* Improved Request object constructor

0.2.3 (2011-02-15)
++++++++++++++++++

* New HTTPHandling Methods
    - Reponse.__nonzero__ (false if bad HTTP Status)
    - Response.ok (True if expected HTTP Status)
    - Response.error (Logged HTTPError if bad HTTP Status)
    - Reponse.raise_for_status() (Raises stored HTTPError)


0.2.2 (2011-02-14)
++++++++++++++++++

* Still handles request in the event of an HTTPError. (Issue #2)
* Eventlet and Gevent Monkeypatch support.
* Cookie Support (Issue #1)


0.2.1 (2011-02-14)
++++++++++++++++++

* Added file attribute to POST and PUT requests for multipart-encode file uploads.
* Added Request.url attribute for context and redirects


0.2.0 (2011-02-14)
++++++++++++++++++

* Birth!


0.0.1 (2011-02-13)
++++++++++++++++++

* Frustration
* Conception



%prep
%setup -n %{pname}-%{unmangled_version}

%build
python2.7 setup.py build

%install
python2.7 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)