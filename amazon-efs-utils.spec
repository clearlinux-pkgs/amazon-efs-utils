#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : amazon-efs-utils
Version  : 1.30.2
Release  : 28
URL      : https://github.com/aws/efs-utils/archive/v1.30.2/efs-utils-1.30.2.tar.gz
Source0  : https://github.com/aws/efs-utils/archive/v1.30.2/efs-utils-1.30.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: amazon-efs-utils-bin = %{version}-%{release}
Requires: amazon-efs-utils-data = %{version}-%{release}
Requires: amazon-efs-utils-license = %{version}-%{release}
Requires: amazon-efs-utils-man = %{version}-%{release}
Requires: amazon-efs-utils-services = %{version}-%{release}
Requires: attrs
Requires: botocore
Requires: funcsigs
Requires: mccabe
Requires: nfs-utils
Requires: openssl
Requires: pbr
Requires: pluggy
Requires: pyflakes
Requires: six
Requires: stunnel
BuildRequires : attrs
BuildRequires : botocore
BuildRequires : funcsigs
BuildRequires : mccabe
BuildRequires : nfs-utils
BuildRequires : openssl
BuildRequires : pbr
BuildRequires : pluggy
BuildRequires : pyflakes
BuildRequires : six
BuildRequires : stunnel
Patch1: 0001-Add-missing-make-install-target.patch

%description
This package provides utilities for simplifying the use of EFS file systems

%package bin
Summary: bin components for the amazon-efs-utils package.
Group: Binaries
Requires: amazon-efs-utils-data = %{version}-%{release}
Requires: amazon-efs-utils-license = %{version}-%{release}
Requires: amazon-efs-utils-services = %{version}-%{release}

%description bin
bin components for the amazon-efs-utils package.


%package data
Summary: data components for the amazon-efs-utils package.
Group: Data

%description data
data components for the amazon-efs-utils package.


%package license
Summary: license components for the amazon-efs-utils package.
Group: Default

%description license
license components for the amazon-efs-utils package.


%package man
Summary: man components for the amazon-efs-utils package.
Group: Default

%description man
man components for the amazon-efs-utils package.


%package services
Summary: services components for the amazon-efs-utils package.
Group: Systemd services

%description services
services components for the amazon-efs-utils package.


%prep
%setup -q -n efs-utils-1.30.2
cd %{_builddir}/efs-utils-1.30.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1618606902
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1618606902
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/amazon-efs-utils
cp %{_builddir}/efs-utils-1.30.2/LICENSE %{buildroot}/usr/share/package-licenses/amazon-efs-utils/b8c10789883a17bc1d0e9f763547f739436dec29
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/amazon-efs-mount-watchdog
/usr/bin/mount.efs

%files data
%defattr(-,root,root,-)
/usr/share/amazon-efs-utils/amazon-efs-mount-watchdog.conf
/usr/share/amazon-efs-utils/efs-utils.conf
/usr/share/amazon-efs-utils/efs-utils.crt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/amazon-efs-utils/b8c10789883a17bc1d0e9f763547f739436dec29

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man8/mount.efs.8

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/amazon-efs-mount-watchdog.service
