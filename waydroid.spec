#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v12
# autospec commit: 381dfd8
#
Name     : waydroid
Version  : 1.4.2
Release  : 4
URL      : https://github.com/waydroid/waydroid/archive/refs/tags/1.4.2.tar.gz
Source0  : https://github.com/waydroid/waydroid/archive/refs/tags/1.4.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: waydroid-bin = %{version}-%{release}
Requires: waydroid-data = %{version}-%{release}
Requires: waydroid-services = %{version}-%{release}
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: clearfraction.patch

%description
# Waydroid
Waydroid uses a container-based approach to boot a full Android system on a
regular GNU/Linux system like Ubuntu.

%package bin
Summary: bin components for the waydroid package.
Group: Binaries
Requires: waydroid-data = %{version}-%{release}
Requires: waydroid-services = %{version}-%{release}

%description bin
bin components for the waydroid package.


%package data
Summary: data components for the waydroid package.
Group: Data

%description data
data components for the waydroid package.


%package services
Summary: services components for the waydroid package.
Group: Systemd services
Requires: systemd

%description services
services components for the waydroid package.


%prep
%setup -q -n waydroid-1.4.2
cd %{_builddir}/waydroid-1.4.2
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1719001434
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
make  %{?_smp_mflags}


%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1719001434
rm -rf %{buildroot}
export GOAMD64=v2
GOAMD64=v2
%make_install
## install_append content
cp -a %{buildroot}/opt/3rd-party/bundles/clearfraction/* %{buildroot}/
rm -rf %{buildroot}/opt
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib/waydroid/data/configs/apparmor_profiles/adbd
/usr/lib/waydroid/data/configs/apparmor_profiles/android_app
/usr/lib/waydroid/data/configs/apparmor_profiles/lxc-waydroid
/usr/lib/waydroid/data/configs/config_1
/usr/lib/waydroid/data/configs/config_3
/usr/lib/waydroid/data/configs/config_4
/usr/lib/waydroid/data/configs/config_base
/usr/lib/waydroid/data/configs/waydroid.seccomp
/usr/lib/waydroid/data/scripts/waydroid-net.sh
/usr/lib/waydroid/tools/__init__.py
/usr/lib/waydroid/tools/actions/__init__.py
/usr/lib/waydroid/tools/actions/app_manager.py
/usr/lib/waydroid/tools/actions/container_manager.py
/usr/lib/waydroid/tools/actions/initializer.py
/usr/lib/waydroid/tools/actions/prop.py
/usr/lib/waydroid/tools/actions/session_manager.py
/usr/lib/waydroid/tools/actions/status.py
/usr/lib/waydroid/tools/actions/upgrader.py
/usr/lib/waydroid/tools/config/__init__.py
/usr/lib/waydroid/tools/config/load.py
/usr/lib/waydroid/tools/config/save.py
/usr/lib/waydroid/tools/helpers/__init__.py
/usr/lib/waydroid/tools/helpers/arch.py
/usr/lib/waydroid/tools/helpers/arguments.py
/usr/lib/waydroid/tools/helpers/drivers.py
/usr/lib/waydroid/tools/helpers/gpu.py
/usr/lib/waydroid/tools/helpers/http.py
/usr/lib/waydroid/tools/helpers/images.py
/usr/lib/waydroid/tools/helpers/ipc.py
/usr/lib/waydroid/tools/helpers/logging.py
/usr/lib/waydroid/tools/helpers/lxc.py
/usr/lib/waydroid/tools/helpers/mount.py
/usr/lib/waydroid/tools/helpers/net.py
/usr/lib/waydroid/tools/helpers/props.py
/usr/lib/waydroid/tools/helpers/protocol.py
/usr/lib/waydroid/tools/helpers/run.py
/usr/lib/waydroid/tools/helpers/run_core.py
/usr/lib/waydroid/tools/helpers/version.py
/usr/lib/waydroid/tools/interfaces/IClipboard.py
/usr/lib/waydroid/tools/interfaces/IHardware.py
/usr/lib/waydroid/tools/interfaces/IPlatform.py
/usr/lib/waydroid/tools/interfaces/IStatusBarService.py
/usr/lib/waydroid/tools/interfaces/IUserMonitor.py
/usr/lib/waydroid/tools/services/__init__.py
/usr/lib/waydroid/tools/services/clipboard_manager.py
/usr/lib/waydroid/tools/services/hardware_manager.py
/usr/lib/waydroid/tools/services/user_manager.py
/usr/lib/waydroid/waydroid.py

%files bin
%defattr(-,root,root,-)
/usr/bin/waydroid

%files data
%defattr(-,root,root,-)
/usr/share/applications/Waydroid.desktop
/usr/share/applications/waydroid.app.install.desktop
/usr/share/applications/waydroid.market.desktop
/usr/share/dbus-1/system-services/id.waydro.Container.service
/usr/share/dbus-1/system.d/id.waydro.Container.conf
/usr/share/desktop-directories/waydroid.directory
/usr/share/icons/hicolor/512x512/apps/waydroid.png
/usr/share/metainfo/id.waydro.waydroid.metainfo.xml
/usr/share/polkit-1/actions/id.waydro.Container.policy

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/waydroid-container.service
