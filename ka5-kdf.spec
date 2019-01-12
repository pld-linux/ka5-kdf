%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kdf
Summary:	KDE free disk space utility
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	ee6a500cd4c32253ed5cf112a7083011
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.53.0
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdoctools-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE free disk space utility.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
/etc/xdg/kdf.categories
%attr(755,root,root) %{_bindir}/kdf
%attr(755,root,root) %{_bindir}/kwikdisk
%ghost %{_libdir}/libkdfprivate.so.18
%{_libdir}/libkdfprivate.so.18.*.*
%{_libdir}/qt5/plugins/libkcm_kdf.so
%{_desktopdir}/org.kde.kdf.desktop
%{_desktopdir}/org.kde.kwikdisk.desktop
%{_iconsdir}/hicolor/128x128/apps/kdf.png
%{_iconsdir}/hicolor/128x128/apps/kwikdisk.png
%{_iconsdir}/hicolor/16x16/apps/kcmdf.png
%{_iconsdir}/hicolor/16x16/apps/kdf.png
%{_iconsdir}/hicolor/16x16/apps/kwikdisk.png
%{_iconsdir}/hicolor/22x22/apps/kcmdf.png
%{_iconsdir}/hicolor/22x22/apps/kdf.png
%{_iconsdir}/hicolor/22x22/apps/kwikdisk.png
%{_iconsdir}/hicolor/32x32/apps/kcmdf.png
%{_iconsdir}/hicolor/32x32/apps/kdf.png
%{_iconsdir}/hicolor/32x32/apps/kwikdisk.png
%{_iconsdir}/hicolor/48x48/apps/kdf.png
%{_iconsdir}/hicolor/48x48/apps/kwikdisk.png
%{_iconsdir}/hicolor/64x64/apps/kdf.png
%{_iconsdir}/hicolor/64x64/apps/kwikdisk.png
%{_datadir}/kservices5/kcmdf.desktop
%{_datadir}/kxmlgui5/kdf
%{_datadir}/metainfo/org.kde.kdf.appdata.xml
