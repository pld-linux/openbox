# TODO:
# - need to put rc3 and menu files in a right place (FHS)
#   (but first in beta stage)
# - better description
#
%define         _alpha  alpha8
Summary:	Small and fast window manger for the X Window
Summary(pl):	Ma³y i szybki zarz±dca okien dla X Window
Name:		openbox
Version:	3.0
Release:	0.%{_alpha}.1
License:	GPL
Group:		X11/Window Managers
Vendor:		Ben Jansens (ben@orodu.net)
Source0:	http://openbox.org/releases/%{name}-%{version}-%{_alpha}.tar.gz
# Source0-md5:	af0efee91aaf9801b37eb6dac830fe07
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
Obsoletes:	openbox < 3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_wmpropsdir	/usr/share/wm-properties

%description
Openbox3 is a completely new window manager, and is not based upon any
previous window manager code-base. Its primary goals are standards
support/compliance, and intelligent window management.

%description -l pl
Openbox3 jest ca³kowicie nowym zarz±dc± okien i nie bazuje ju¿ na
kodzie wcze¶niejszych wersji. Jego g³ównymi celami s± wsparcie i zgodno¶æ
ze standardami oraz inteligentne zarz±dzanie oknami.

%prep
%setup -q -n %{name}-%{version}-%{_alpha}

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

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
echo
echo "Remember to copy from /usr/share/openbox *.xml files"
echo "to your ~/.openbox dir."
echo

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README* ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/openbox
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/openbox/*.xml
%{_datadir}/openbox/themes
%{_wmpropsdir}/openbox.desktop
