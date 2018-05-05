%define		kdeappsver	18.04.0
%define		qtver		5.3.2
%define		kaname		kdf
Summary:	KDE free disk space utility
Name:		ka5-%{kaname}
Version:	18.04.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	9a933c2f13328fd7ae01bcada43f0646
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
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
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
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
