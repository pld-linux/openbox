# TODO:
# - better description
# - prepare it to working with GNOME as a replacement for
#   metacity
# - solve /etc/xdg problem
#
Summary:	Small and fast window manger for the X Window
Summary(pl):	Ma�y i szybki zarz�dca okien dla X Window
Name:		openbox
Version:	3.0
%define		_beta	beta6
Release:	1.%{_beta}.0
License:	GPL
Group:		X11/Window Managers
Vendor:		Ben Jansens (ben@orodu.net)
Source0:	http://openbox.org/releases/%{name}-%{version}-%{_beta}.tar.gz
# Source0-md5:	32140b1abf3d0e8701217e6a788aa075
Source1:	%{name}-xsession.desktop
URL:		http://openbox.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gettext-autopoint >= 0.12.1
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRequires:	xft-devel >= 2.0
Requires(post):	/sbin/ldconfig
Requires:	applnk
Requires:	openbox-theme-base = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Openbox3 is a completely new window manager, and is not based upon any
previous window manager code-base. Its primary goals are standards
support/compliance, and intelligent window management.

%description -l pl
Openbox3 jest ca�kowicie nowym zarz�dc� okien i nie bazuje ju� na
kodzie wcze�niejszych wersji. Jego g��wnymi celami s� wsparcie i zgodno��
ze standardami oraz inteligentne zarz�dzanie oknami.

%package devel
Summary:	Header files for openbox
Summary(pl):	Pliki nag��wkowe openbox
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development header files for writing applications based on openbox.

%description devel -l pl
Pliki nag��wkowe do tworzenia oprogramowania opartego o openbox.

%package static
Summary:	Static openbox library
Summary(pl):	Statyczna biblioteka openbox
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static openbox library.

%description static -l pl
Statyczna biblioteka openbox.

%package themes-Allegro
Summary:	Allegro theme for openbox
Summary(pl):	Motyw Allegro dla openboxa
Group:		Themes
Requires:	%{name} = %{version}

%description themes-Allegro
Allegro theme for openbox.

%description themes-Allegro -l pl
Motyw Allegro dla openboxa.

%package themes-Artwiz
Summary:	Artwiz theme for openbox
Summary(pl):	Motyw Artwiz dla openboxa
Group:		Themes
Requires:	%{name} = %{version}

%description themes-Artwiz
Artwiz theme for openbox.

%description themes-Artwiz -l pl
Motyw Artwiz dla openboxa.

%package themes-Blah41
Summary:	Blah41 theme for openbox
Summary(pl):	Motyw Blah41 dla openboxa
Group:		Themes
Requires:	%{name} = %{version}

%description themes-Blah41
Blah41 theme for openbox.

%description themes-Allegro -l pl
Motyw Blah41 dla openboxa.

%package themes-Om4Ob
Summary:	Om4Ob theme for openbox
Summary(pl):	Motyw Om4Ob dla openboxa
Group:		Themes
Requires:	%{name} = %{version}

%description themes-Om4Ob
Om4Ob theme for openbox.

%description themes-Om4Ob -l pl
Motyw Om4Ob dla openboxa.

%package themes-TheBear
Summary:	TheBear theme for openbox
Summary(pl):	Motyw TheBear dla openboxa
Group:		Themes
Requires:	%{name} = %{version}
Provides:	openbox-theme-base = %{version}

%description themes-TheBear
TheBear theme for openbox.

%description themes-Allegro -l pl
Motyw TheBear dla openboxa.

%prep
%setup -q -n %{name}-%{version}-%{_beta}

%build
rm -f missing
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGELOG README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_datadir}/openbox
%{_datadir}/openbox/*
%{_datadir}/xsessions/openbox.desktop
%dir %{_sysconfdir}/xdg/openbox
%{_sysconfdir}/xdg/openbox/*.xml
%{_wmpropsdir}/openbox.desktop

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/openbox
%dir %{_includedir}/openbox/3.0
%dir %{_includedir}/openbox/3.0/openbox
%{_includedir}/openbox/3.0/openbox/*.h
%attr(755,root,root) %{_libdir}/lib*.so
%{_pixmapsdir}/openbox.png
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files themes-Allegro
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Allegro
%dir %{_datadir}/themes/Allegro/openbox-3
%{_datadir}/themes/Allegro/openbox-3/*

%files themes-Artwiz
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Artwiz
%dir %{_datadir}/themes/Artwiz/openbox-3
%{_datadir}/themes/Artwiz/openbox-3/*

%files themes-Blah41
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Blah41
%dir %{_datadir}/themes/Blah41/openbox-3
%{_datadir}/themes/Blah41/openbox-3/*

%files themes-Om4Ob
%defattr(644,root,root,755)
%dir %{_datadir}/themes/Om4Ob
%dir %{_datadir}/themes/Om4Ob/openbox-3
%{_datadir}/themes/Om4Ob/openbox-3/*

%files themes-TheBear
%defattr(644,root,root,755)
%dir %{_datadir}/themes/TheBear
%dir %{_datadir}/themes/TheBear/openbox-3
%{_datadir}/themes/TheBear/openbox-3/*
