#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : glance_store
Version  : 0.13.1
Release  : 27
URL      : http://tarballs.openstack.org/glance_store/glance_store-0.13.1.tar.gz
Source0  : http://tarballs.openstack.org/glance_store/glance_store-0.13.1.tar.gz
Summary  : OpenStack Image Service Store Library
Group    : Development/Tools
License  : Apache-2.0
Requires: glance_store-bin
Requires: glance_store-python
BuildRequires : Babel-python
BuildRequires : Jinja2
BuildRequires : PyYAML-python
BuildRequires : Pygments
BuildRequires : Sphinx-python
BuildRequires : boto-python
BuildRequires : coverage-python
BuildRequires : discover-python
BuildRequires : docutils-python
BuildRequires : enum34-python
BuildRequires : eventlet-python
BuildRequires : extras
BuildRequires : extras-python
BuildRequires : fixtures-python
BuildRequires : flake8-python
BuildRequires : futures-python
BuildRequires : greenlet-python
BuildRequires : hacking
BuildRequires : httplib2
BuildRequires : iso8601-python
BuildRequires : jsonschema-python
BuildRequires : linecache2-python
BuildRequires : markupsafe-python
BuildRequires : mccabe-python
BuildRequires : mox3-python
BuildRequires : msgpack-python-python
BuildRequires : netaddr
BuildRequires : netifaces-python
BuildRequires : ordereddict-python
BuildRequires : os-brick
BuildRequires : oslo.concurrency-python
BuildRequires : oslo.config
BuildRequires : oslo.i18n-python
BuildRequires : oslo.serialization-python
BuildRequires : oslo.utils-python
BuildRequires : oslo.vmware-python
BuildRequires : oslosphinx-python
BuildRequires : oslotest-python
BuildRequires : pbr
BuildRequires : pep8
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : posix_ipc
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pyflakes-python
BuildRequires : pyrsistent-python
BuildRequires : pytest
BuildRequires : python-cinderclient-python
BuildRequires : python-dev
BuildRequires : python-keystoneclient-python
BuildRequires : python-mimeparse-python
BuildRequires : python-mock
BuildRequires : python-subunit
BuildRequires : python-swiftclient-python
BuildRequires : python3-dev
BuildRequires : pytz-python
BuildRequires : requests-mock-python
BuildRequires : requests-python
BuildRequires : retrying-python
BuildRequires : setuptools
BuildRequires : simplejson
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : suds-jurko
BuildRequires : testrepository-python
BuildRequires : testscenarios
BuildRequires : testtools
BuildRequires : testtools-python
BuildRequires : tox
BuildRequires : traceback2-python
BuildRequires : unittest2-python
BuildRequires : urllib3-python
BuildRequires : virtualenv

%description
Glance Store Library
=====================
Glance's stores library
* License: Apache License, Version 2.0
* Documentation: http://docs.openstack.org/developer/glance_store
* Source: http://git.openstack.org/cgit/openstack/glance_store
* Bugs: http://bugs.launchpad.net/glance-store

%package bin
Summary: bin components for the glance_store package.
Group: Binaries

%description bin
bin components for the glance_store package.


%package python
Summary: python components for the glance_store package.
Group: Default
Requires: boto-python
Requires: enum34-python
Requires: eventlet-python
Requires: httplib2
Requires: jsonschema-python
Requires: oslo.concurrency-python
Requires: oslo.config
Requires: oslo.i18n-python
Requires: oslo.serialization-python
Requires: oslo.utils-python
Requires: oslo.vmware-python
Requires: python-cinderclient-python
Requires: python-keystoneclient-python
Requires: python-swiftclient-python
Requires: requests-python
Requires: six-python
Requires: stevedore

%description python
python components for the glance_store package.


%prep
cd ..
%setup -q -n glance_store-0.13.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages python2 setup.py test || :
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glance-rootwrap

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
