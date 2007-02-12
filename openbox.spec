
# todo:
# - update themes
#   - obsolete old ones
#   - subpackages for new ones
# - l10n files listed twice

Summary:	Small and fast window manger for the X Window
Summary(pl.UTF-8):   Mały i szybki zarządca okien dla X Window
Name:		openbox
Version:	3.3.1
Release:	0.1
Epoch:		1
License:	GPL
Group:		X11/Window Managers
Source0:	http://openbox.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	6dc25d5fbff5d6277593b89974f950d8
Source1:	%{name}-xsession.desktop
URL:		http://openbox.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-autopoint >= 0.12.1
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.26
BuildRequires:	pango-devel >= 1.14.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-theme-base = %{epoch}:%{version}-%{release}
Provides:	gnome-wm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Openbox3 is a completely new window manager, and is not based upon any
previous window manager code-base. Its primary goals are standards
support/compliance, and intelligent window management.

%description -l pl.UTF-8
Openbox3 jest całkowicie nowym zarządcą okien i nie bazuje już na
kodzie wcześniejszych wersji. Jego głównymi celami są wsparcie i zgodność
ze standardami oraz inteligentne zarządzanie oknami.

%package libs
Summary:	openbox libraries
Summary(pl.UTF-8):   Biblioteki openboksa
Group:		Libraries

%description libs
openbox libraries.

%description libs -l pl.UTF-8
Biblioteki openboksa.

%package devel
Summary:	Header files for openbox
Summary(pl.UTF-8):   Pliki nagłówkowe openbox
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Development header files for writing applications based on openbox.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia oprogramowania opartego o openbox.

%package static
Summary:	Static openbox library
Summary(pl.UTF-8):   Statyczna biblioteka openbox
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static openbox library.

%description static -l pl.UTF-8
Statyczna biblioteka openbox.

%package themes-Allegro
Summary:	Allegro theme for openbox
Summary(pl.UTF-8):   Motyw Allegro dla openboxa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description themes-Allegro
Allegro theme for openbox.

%description themes-Allegro -l pl.UTF-8
Motyw Allegro dla openboxa.

%package themes-Artwiz
Summary:	Artwiz theme for openbox
Summary(pl.UTF-8):   Motyw Artwiz dla openboxa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description themes-Artwiz
Artwiz theme for openbox.

%description themes-Artwiz -l pl.UTF-8
Motyw Artwiz dla openboxa.

%package themes-Blah41
Summary:	Blah41 theme for openbox
Summary(pl.UTF-8):   Motyw Blah41 dla openboxa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description themes-Blah41
Blah41 theme for openbox.

%description themes-Allegro -l pl.UTF-8
Motyw Blah41 dla openboxa.

%package themes-Om4Ob
Summary:	Om4Ob theme for openbox
Summary(pl.UTF-8):   Motyw Om4Ob dla openboxa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description themes-Om4Ob
Om4Ob theme for openbox.

%description themes-Om4Ob -l pl.UTF-8
Motyw Om4Ob dla openboxa.

%package themes-bear
Summary:	Bear theme for openbox
Summary(pl.UTF-8):   Motyw Bear dla openboxa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}
Obsoletes:	openbox-themes-TheBear

%description themes-bear
Bear theme for openbox.

%description themes-bear -l pl.UTF-8
Motyw Bear dla openboxa.

%prep
%setup -q

%build
%{__autopoint}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	desktopfilesdir=%{_wmpropsdir}

# gdm/kdm support
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/openbox.desktop

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -rf $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CHANGELOG COMPLIANCE README
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/openbox
%{_datadir}/openbox/*
%{_datadir}/xsessions/openbox.desktop
%{_pixmapsdir}/openbox.png
%dir %{_sysconfdir}/xdg/openbox
%{_sysconfdir}/xdg/openbox/*.xml
%{_wmpropsdir}/openbox.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/openbox
%dir %{_includedir}/openbox/3.3
%dir %{_includedir}/openbox/3.3/openbox
%{_includedir}/openbox/3.3/openbox/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

#%files themes-Allegro
#%defattr(644,root,root,755)
#%dir %{_datadir}/themes/Allegro
#%dir %{_datadir}/themes/Allegro/openbox-3
#%{_datadir}/themes/Allegro/openbox-3/*

#%files themes-Artwiz
#%defattr(644,root,root,755)
#%dir %{_datadir}/themes/Artwiz
#%dir %{_datadir}/themes/Artwiz/openbox-3
#%{_datadir}/themes/Artwiz/openbox-3/*

#%files themes-Blah41
#%defattr(644,root,root,755)
#%dir %{_datadir}/themes/Blah41
#%dir %{_datadir}/themes/Blah41/openbox-3
#%{_datadir}/themes/Blah41/openbox-3/*

#%files themes-Om4Ob
#%defattr(644,root,root,755)
#%dir %{_datadir}/themes/Om4Ob
#%dir %{_datadir}/themes/Om4Ob/openbox-3
#%{_datadir}/themes/Om4Ob/openbox-3/*

%files themes-bear
%defattr(644,root,root,755)
%dir %{_datadir}/themes/bear2
%dir %{_datadir}/themes/bear2/openbox-3
%{_datadir}/themes/bear2/openbox-3/*
