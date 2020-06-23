#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC12B8E73B30F2FC8 (infra-root@openstack.org)
#
Name     : glance_store
Version  : 2.1.0
Release  : 64
URL      : http://tarballs.openstack.org/glance_store/glance_store-2.1.0.tar.gz
Source0  : http://tarballs.openstack.org/glance_store/glance_store-2.1.0.tar.gz
Source1  : http://tarballs.openstack.org/glance_store/glance_store-2.1.0.tar.gz.asc
Summary  : OpenStack Image Service Store Library
Group    : Development/Tools
License  : Apache-2.0
Requires: glance_store-bin = %{version}-%{release}
Requires: glance_store-license = %{version}-%{release}
Requires: glance_store-python = %{version}-%{release}
Requires: glance_store-python3 = %{version}-%{release}
Requires: boto3
Requires: eventlet
Requires: httplib2
Requires: jsonschema
Requires: keystoneauth1
Requires: os-brick
Requires: oslo.concurrency
Requires: oslo.config
Requires: oslo.i18n
Requires: oslo.privsep
Requires: oslo.rootwrap
Requires: oslo.serialization
Requires: oslo.utils
Requires: python-cinderclient
Requires: python-keystoneclient
Requires: python-swiftclient
Requires: requests
Requires: six
Requires: stevedore
BuildRequires : boto3
BuildRequires : buildreq-distutils3
BuildRequires : eventlet
BuildRequires : httplib2
BuildRequires : jsonschema
BuildRequires : keystoneauth1
BuildRequires : os-brick
BuildRequires : oslo.concurrency
BuildRequires : oslo.config
BuildRequires : oslo.i18n
BuildRequires : oslo.privsep
BuildRequires : oslo.rootwrap
BuildRequires : oslo.serialization
BuildRequires : oslo.utils
BuildRequires : pbr
BuildRequires : python-cinderclient
BuildRequires : python-keystoneclient
BuildRequires : python-swiftclient
BuildRequires : requests
BuildRequires : six
BuildRequires : stevedore

%description
Team and repository tags
        ========================

%package bin
Summary: bin components for the glance_store package.
Group: Binaries
Requires: glance_store-license = %{version}-%{release}

%description bin
bin components for the glance_store package.


%package license
Summary: license components for the glance_store package.
Group: Default

%description license
license components for the glance_store package.


%package python
Summary: python components for the glance_store package.
Group: Default
Requires: glance_store-python3 = %{version}-%{release}

%description python
python components for the glance_store package.


%package python3
Summary: python3 components for the glance_store package.
Group: Default
Requires: python3-core
Provides: pypi(glance_store)
Requires: pypi(eventlet)
Requires: pypi(jsonschema)
Requires: pypi(keystoneauth1)
Requires: pypi(oslo.concurrency)
Requires: pypi(oslo.config)
Requires: pypi(oslo.i18n)
Requires: pypi(oslo.serialization)
Requires: pypi(oslo.utils)
Requires: pypi(python_keystoneclient)
Requires: pypi(requests)
Requires: pypi(six)
Requires: pypi(stevedore)

%description python3
python3 components for the glance_store package.


%prep
%setup -q -n glance_store-2.1.0
cd %{_builddir}/glance_store-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1592934571
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/glance_store
cp %{_builddir}/glance_store-2.1.0/LICENSE %{buildroot}/usr/share/package-licenses/glance_store/294b43b2cec9919063be1a3b49e8722648424779
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/glance-rootwrap

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/glance_store/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
