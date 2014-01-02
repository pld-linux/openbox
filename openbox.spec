#
# Conditional build:
%bcond_with	gnome2		# build with support for GNOME2 wm-properties

Summary:	Small and fast window manger for the X Window
Summary(pl.UTF-8):	Mały i szybki zarządca okien dla X Window
Name:		openbox
Version:	3.5.2
Release:	1
Epoch:		1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://openbox.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	93df606606053b7e8578a5c116afb8ec
#Patch0:		%{name}-link.patch
URL:		http://openbox.org/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.15
BuildRequires:	glib2-devel >= 1:2.14.0
BuildRequires:	libtool
BuildRequires:	libuuid-devel
BuildRequires:	libxml2-devel >= 1:2.6.31
BuildRequires:	pango-devel >= 1.18.3
BuildRequires:	pkgconfig
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-theme-base = %{epoch}:%{version}-%{release}
Requires:	dbus-x11
Suggests:	obconf
Provides:	gnome-wm
Obsoletes:	openbox-themes-Allegro
Obsoletes:	openbox-themes-Artwiz
Obsoletes:	openbox-themes-Blah41
Obsoletes:	openbox-themes-Om4Ob
Conflicts:	filesystem < 3.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/gnome/wm-properties

%description
Openbox is a completely new window manager, and is not based upon any
previous window manager code-base. Its primary goals are standards
support/compliance, and intelligent window management.

%description -l pl.UTF-8
Openbox jest całkowicie nowym zarządcą okien i nie bazuje już na
kodzie wcześniejszych wersji. Jego głównymi celami są wsparcie i
zgodność ze standardami oraz inteligentne zarządzanie oknami.

%package libs
Summary:	Openbox libraries
Summary(pl.UTF-8):	Biblioteki Openboksa
Group:		Libraries

%description libs
Openbox libraries.

%description libs -l pl.UTF-8
Biblioteki Openboksa.

%package devel
Summary:	Header files for Openbox
Summary(pl.UTF-8):	Pliki nagłówkowe Openboksa
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	glib2-devel >= 1:2.14.0
Requires:	libxml2-devel >= 1:2.6.31
Requires:	pango-devel >= 1.18.3
Requires:	xorg-lib-libSM-devel

%description devel
Development header files for writing applications based on Openbox.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia oprogramowania opartego o Openboksa.

%package static
Summary:	Static Openbox libraries
Summary(pl.UTF-8):	Statyczne biblioteki Openboksa
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static Openbox libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Openboksa.

%package themes-Artwiz-boxed
Summary:	Artwiz-boxed theme for Openbox
Summary(pl.UTF-8):	Motyw Artwiz-boxed dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Artwiz-boxed
Artwiz-boxed theme for Openbox.

%description themes-Artwiz-boxed -l pl.UTF-8
Motyw Artwiz-boxed dla Openboksa.

%package themes-bear
Summary:	Bear theme for Openbox
Summary(pl.UTF-8):	Motyw Bear dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}
Obsoletes:	openbox-themes-TheBear

%description themes-bear
Bear theme for Openbox.

%description themes-bear -l pl.UTF-8
Motyw Bear dla Openboksa.

%package themes-Clearlooks-Olive
Summary:	Clearlooks-Olive theme for Openbox
Summary(pl.UTF-8):	Motyw Clearlooks-Olive dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Clearlooks-Olive
Clearlooks-Olive theme for Openbox.

%description themes-Clearlooks-Olive -l pl.UTF-8
Motyw Clearlooks-Olive dla Openboksa.

%package themes-Clearlooks
Summary:	Clearlooks theme for Openbox
Summary(pl.UTF-8):	Motyw Clearlooks dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Clearlooks
Clearlooks theme for Openbox.

%description themes-Clearlooks -l pl.UTF-8
Motyw Clearlooks dla Openboksa.

%package themes-Mikachu
Summary:	Mikachu theme for Openbox
Summary(pl.UTF-8):	Motyw Mikachu dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Mikachu
Mikachu theme for Openbox.

%description themes-Mikachu -l pl.UTF-8
Motyw Mikachu dla Openboksa.

%package themes-Natura
Summary:	Natura theme for Openbox
Summary(pl.UTF-8):	Motyw Natura dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Natura
Natura theme for Openbox.

%description themes-Natura -l pl.UTF-8
Motyw Natura dla Openboksa.

%package themes-Onyx-Citrus
Summary:	Onyx-Citrus theme for Openbox
Summary(pl.UTF-8):	Motyw Onyx-Citrus dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Onyx-Citrus
Onyx-Citrus theme for Openbox.

%description themes-Onyx-Citrus -l pl.UTF-8
Motyw Onyx-Citrus dla Openboksa.

%package themes-Onyx
Summary:	Onyx theme for Openbox
Summary(pl.UTF-8):	Motyw Onyx dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Onyx
Onyx theme for Openbox.

%description themes-Onyx -l pl.UTF-8
Motyw Onyx dla Openboksa.

%package themes-Orang
Summary:	Orang theme for Openbox
Summary(pl.UTF-8):	Motyw Orang dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Orang
Orang theme for Openbox.

%description themes-Orang -l pl.UTF-8
Motyw Orang dla Openboksa.

%package themes-Syscrash
Summary:	Syscrash theme for Openbox
Summary(pl.UTF-8):	Motyw Syscrash dla Openboksa
Group:		Themes
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	openbox-theme-base = %{epoch}:%{version}-%{release}

%description themes-Syscrash
Syscrash theme for Openbox.

%description themes-Syscrash -l pl.UTF-8
Motyw Syscrash dla Openboksa.

%prep
%setup -q
#%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomewmfilesdir=%{_wmpropsdir}

%{!?with_gnome2:%{__rm} $RPM_BUILD_ROOT%{_wmpropsdir}/openbox.desktop}

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc/openbox

mv $RPM_BUILD_ROOT%{_datadir}/locale/{no,nb}

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS CHANGELOG COMPLIANCE README
%doc data/{menu.xsd,rc.xsd,xbm/*} doc/rc-mouse-focus.xml
%attr(755,root,root) %{_bindir}/gnome-panel-control
%attr(755,root,root) %{_bindir}/openbox
%attr(755,root,root) %{_bindir}/openbox-gnome-session
%attr(755,root,root) %{_bindir}/openbox-kde-session
%attr(755,root,root) %{_bindir}/openbox-session
%attr(755,root,root) %{_bindir}/gdm-control
%attr(755,root,root) %{_bindir}/obxprop
%{_datadir}/xsessions/openbox-gnome.desktop
%{_datadir}/xsessions/openbox-kde.desktop
%{_datadir}/xsessions/openbox.desktop
%{_mandir}/man1/obxprop.1*
%{_mandir}/man1/openbox-gnome-session.1*
%{_mandir}/man1/openbox-kde-session.1*
%{_mandir}/man1/openbox-session.1*
%{_mandir}/man1/openbox.1*
%dir %{_sysconfdir}/xdg/openbox
%{_sysconfdir}/xdg/openbox/autostart
%{_sysconfdir}/xdg/openbox/environment
%{_sysconfdir}/xdg/openbox/menu.xml
%{_sysconfdir}/xdg/openbox/rc.xml
%{?with_gnome2:%{_wmpropsdir}/openbox.desktop}
%{_desktopdir}/openbox.desktop
%{_pixmapsdir}/openbox.png
%attr(755,root,root) %{_libdir}/openbox-autostart
%attr(755,root,root) %{_libdir}/openbox-xdg-autostart

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libobrender.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libobrender.so.??
%attr(755,root,root) %{_libdir}/libobt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libobt.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libobrender.so
%attr(755,root,root) %{_libdir}/libobt.so
%{_libdir}/libobrender.la
%{_libdir}/libobt.la
%dir %{_includedir}/openbox
%dir %{_includedir}/openbox/3.5
%dir %{_includedir}/openbox/3.5/obrender
%{_includedir}/openbox/3.5/obrender/*.h
%dir %{_includedir}/openbox/3.5/obt
%{_includedir}/openbox/3.5/obt/*.h
%{_pkgconfigdir}/obrender-3.5.pc
%{_pkgconfigdir}/obt-3.5.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libobt.a
%{_libdir}/libobrender.a

%files themes-Artwiz-boxed
%defattr(644,root,root,755)
%{_datadir}/themes/Artwiz-boxed

%files themes-bear
%defattr(644,root,root,755)
%{_datadir}/themes/Bear2

%files themes-Clearlooks-Olive
%defattr(644,root,root,755)
%{_datadir}/themes/Clearlooks-Olive

%files themes-Clearlooks
%defattr(644,root,root,755)
%{_datadir}/themes/Clearlooks

%files themes-Mikachu
%defattr(644,root,root,755)
%{_datadir}/themes/Mikachu

%files themes-Natura
%defattr(644,root,root,755)
%{_datadir}/themes/Natura

%files themes-Onyx-Citrus
%defattr(644,root,root,755)
%{_datadir}/themes/Onyx-Citrus

%files themes-Onyx
%defattr(644,root,root,755)
%{_datadir}/themes/Onyx

%files themes-Orang
%defattr(644,root,root,755)
%{_datadir}/themes/Orang

%files themes-Syscrash
%defattr(644,root,root,755)
%{_datadir}/themes/Syscrash
