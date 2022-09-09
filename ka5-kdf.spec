#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.08.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kdf
Summary:	KDE free disk space utility
Name:		ka5-%{kaname}
Version:	22.08.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	11407d270dabc5ccc445b22655a98df4
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcmutils-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-knotifications-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE free disk space utility.

%description -l pl.UTF-8
Program użytkowy KDE do pokazywania zajętości dysku.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

rm -rf $RPM_BUILD_ROOT%{_kdedocdir}/{ko,sr}
%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdf
%attr(755,root,root) %{_bindir}/kwikdisk
%ghost %{_libdir}/libkdfprivate.so.22
%{_libdir}/libkdfprivate.so.*.*.*
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
%{_datadir}/qlogging-categories5/kdf.categories
